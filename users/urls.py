from django.urls import include, path
# from .views import CustomObtainAuthToken

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    # path('authenticate/',views.CustomObtainAuthToken.as_view()),
    path('login/', views.login1),
    # path('register/', views.UserViewSet),
]