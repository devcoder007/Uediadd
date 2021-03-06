from django.urls import include, path
# from .views import CustomObtainAuthToken

from . import views

urlpatterns = [
    # path('', views.UserListView.as_view()),
    # path('authenticate/',views.CustomObtainAuthToken.as_view()),
    # path('login/', views.login1),
    # path('register/', views.UserViewSet),
    path('register/', views.create_user),
    path('login/',views.login_user),
    path('',views.user_view), 
    path('verify/<slug:token>', views.mail_view, name="mail_view")
]