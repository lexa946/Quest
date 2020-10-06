from django.urls import path
from django.contrib.auth import views
from .views import register, personal


app_name = 'account'
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("personal/", personal, name="personal_area"),
]