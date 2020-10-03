from django.urls import path
from django.contrib.auth import views
from .views import register


app_name = 'account'
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    # path("logout/", None, name="logout"),
]