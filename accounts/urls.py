from django.urls import path, include
from .views import RegisterAPIView, LoginAPIView, UserAPIView
from drf_spectacular.utils import extend_schema
from knox import views as knox_views

app_name = 'accounts'
urlpatterns = [
    path("auth", include("knox.urls")),
    path("auth/register", RegisterAPIView.as_view()),
    path("auth/login", LoginAPIView.as_view()),
    path("auth/user", UserAPIView.as_view()),
    path("auth/logout", knox_views.LogoutView.as_view(), name="knox_logout"),
]
