# # from rest_framework.authtoken.views import ObtainAuthToken
# # from rest_framework.authtoken.models import Token
# # from rest_framework.response import Response
# # from rest_framework import generics

# # from . import models
# # from . import serializers

# # class UserListView(generics.ListAPIView):
# #     queryset = models.CustomUser.objects.all()
# #     serializer_class = serializers.UserSerializer


# # class CustomObtainAuthToken(ObtainAuthToken):
# #     def post(self, request, *args, **kwargs):
# #         response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
# #         token = Token.objects.get(key=response.data['token'])
# #         return Response({'token': token.key, 'id': token.user_id})
# from rest_framework import generics
# from . import serializers
# from . import models
# from rest_auth.registration.views import RegisterView
# from .serializers import UserSerializer
# from django.contrib.auth import authenticate
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from django.contrib.auth.models import User
# from rest_framework.status import (
#     HTTP_400_BAD_REQUEST,
#     HTTP_404_NOT_FOUND,
#     HTTP_200_OK
# )
# from rest_framework.response import Response


# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login1(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     email = request.data.get("email")

#     user = authenticate(email=email, password=password)
#     if not user:
#         return Response({'token': '', 'error': 'Invalid Credentials', 'status': 401})
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({
#                     'token': token.key,
#                     'first_name': user.first_name,
#                     'last_name': user.last_name,
#                     'email': user.email,
#                     'status': HTTP_200_OK
#                     }, status=HTTP_200_OK)

# from rest_auth.registration.views import RegisterView


# # class CustomRegisterView(RegisterView):
# #     def create(self, request, *args, **kwargs):
# #         response = super().create(request, *args, **kwargs)
# #         custom_data = {"message": "some message", "status": "ok"}
# #         response.data.update(custom_data)
# #         return response


# # class UserViewSet(viewsets.ModelViewSet):
# #     """
# #     API endpoint that allows users to be viewed or edited.
# #     """
# #     queryset = User.objects.all().order_by('-date_joined')
# #     serializer_class = UserSerializer
# #     # authentication_classes = (TokenAuthentication,)
# #     # permission_classes = (IsAuthenticatedOrReadOnly,)


# class UserListView(generics.ListAPIView):
#     queryset = models.CustomUser.objects.all()
#     serializer_class = serializers.UserSerializer



from rest_framework.decorators import api_view
from django.http import HttpResponse
from .serializers import UserInfoSerializer, UserInfoLoginSerializer, UserInfoViewSerializer
from rest_framework.response import Response
from rest_framework import status
from.models import UserInfo
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
import uuid


@api_view(['GET', 'POST', 'PUT'])
def create_user(request):
    if request.method == 'POST':
        request.data['token'] = int(uuid.uuid4())
        serializer = UserInfoSerializer(data=request.data)
        if UserInfo.objects.filter(email = request.data['email']).exists():
            return Response({"alert":"Email Already Exists","status": 409})
        if serializer.is_valid():
            email(request)
            serializer.save()
            return Response({'token':serializer.data['token'],'status':200,'message':'User added successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT'])
def login_user(request):

    if request.method == 'POST':
        queryset = UserInfo.objects.all()
        print(request.data)
        if UserInfo.objects.filter(email = request.data['email']).exists():
            queryset = UserInfo.objects.filter(email=request.data['email'])
            if(queryset.values('password')[0]['password'] == request.data['password']):
                serializer = UserInfoSerializer(queryset.values(), many=True)
                if(queryset.values('is_verified')[0]['is_verified'] == False):
                    return Response({"alert":"Email verification pending","status":404})
                else:
                    return Response({"data":serializer.data,"status":200})
            else:
                return Response({"alert":"Incorrect password","status":403})
        else:
            return Response({"alert":"Email is not registered yet","status":403})
        return Response({"error":"Invalid Request","status":404})

@api_view(['GET', 'POST', 'PUT'])
def user_view(request):
    if request.method == 'GET':
        queryset = UserInfo.objects.filter(is_deleted=False)
        serializer = UserInfoViewSerializer(queryset.values(), many=True)
        return Response(serializer.data)
    return Response({'error':'Please use GET method'})


def email(request):
    queryset = UserInfo.objects.filter(email = request.data['email'])
    text_content = 'Account Activation Email'
    subject = 'Email Activation'
    template_name = "email.html"
    context = {
        'token': request.data['token'],
        'name' : request.data['username']
    }
    from_email = 'kampuskonnect.kk@gmail.com'
    recipients = [request.data['email']]
    html_content = render_to_string(template_name, context)
    email = EmailMultiAlternatives(subject, text_content, from_email, recipients)
    email.attach_alternative(html_content, "text/html")
    email.send()


def mail_view(request,token):
    UserInfo.objects.filter(token=token).update(is_verified=True)
    return HttpResponse("Email Successfully Verified")