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
from .serializers import UserInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from.models import UserInfo

@api_view(['GET', 'POST', 'PUT'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        # print(serializer.initial_data)
        print("effgew")
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e,"dfdgdgdf")
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        queryset = UserInfo.objects.all()
        serializer = UserInfoSerializer(queryset, many=True)
        return Response(serializer.data)