from django.urls import path
from .views import RegisterAPIView, LoginAPIView, HomeAPIView

urlpatterns = [
    path("auth/register/", RegisterAPIView.as_view(), name="register_view"),
    path("auth/login/", LoginAPIView.as_view(), name="login_view"),
    path("home/", HomeAPIView.as_view(), name="home_view"),

]