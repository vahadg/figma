from django.contrib.auth import views
from django.urls import path

from . import views

#urlpatterns = [
#    path('login/', views.LoginView.as_view(), name='login'),
#]

urlpatterns = [
    path('', views.home, name = "home"),
    path("signup/", views.SignUp.as_view(), name="signup"),        
    path('register/', views.RegisterFormView.as_view(), name="reg"),
    path('add/', views.PersonCreateView.as_view(), name="add"),
    path('create/', views.create, name = "create"),
]
