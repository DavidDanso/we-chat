from django.urls import path
from . import views

urlpatterns = [
    path('user-info/<str:pk>', views.userInfo, name='info'),
    path('profile', views.profilePage, name='profile'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('signup', views.signupPage, name='signup'),
]