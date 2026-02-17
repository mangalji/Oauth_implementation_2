from django.urls import path
from .views import RegistrationView, LoginView, profile_view, LogoutView, GoogleLoginSuccessView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/',RegistrationView.as_view(),name='register'),
    path("login/",LoginView.as_view(),name='login'),
    path("profile/",profile_view,name='profile-view'),
    path("token/refresh/",TokenRefreshView.as_view(),name='token-refresh'),
    path("logout/",LogoutView.as_view(),name='logout'),
    path("google/success/",GoogleLoginSuccessView.as_view(),name="success-redirect"),
]

