from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import User
from . import models


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = ('email', 'token')


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.CustomUser
#         fields = ('email', 'username', )

# class MyRegisterSerializer(RegisterSerializer):
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()

   

#     def get_cleaned_data(self):
#         super(MyRegisterSerializer, self).get_cleaned_data()
#         return {
#             'username': self.validated_data.get('username', ''),
#             'password1': self.validated_data.get('password1', ''),
#             'email': self.validated_data.get('email', ''),
#             'first_name': self.validated_data.get('first_name', ''),
#             'last_name': self.validated_data.get('last_name', '')
#         }
#     def save(self, request):
#         model = models.CustomUser

# # class UserSerializer(serializers.HyperlinkedModelSerializer):
# #     # ff = "sd"
# #     class Meta:
# #         model = User

# #         fields = ['id', 'username', 'email', 'password','is_staff','is_active','token']
# #         extra_kwargs = {'password': {'write_only':True, 'required':True}}

# #     def create(self, validated_data):
# #         # random_str = str(uuid.uuid4())
# #         # random_str = random_str.upper()
# #         # random_str = random_str[:6]
# #         # print(validated_data)
# #         user = User.objects.create_user(**validated_data)
# #         # print(user.pk)
        
# #         # q = User.objects.filter(username=user)
# #         # q.update(is_active=False)
# #         # # q.update(token=random_str)
# #         # myapp.views.email(validated_data,user)
# #         # tt = uuid
# #         # print(user.token)
# #         # print(user)
# #         # print(user.token+"injkn")
# #         return user