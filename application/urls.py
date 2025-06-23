from django.urls import path
from .views import (
    Homepage,
    LoginView,
)

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("login/", LoginView.as_view(), name="login"),
]
