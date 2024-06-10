from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserPasswordChangeView
from .views import user_logout, user_profile

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("signup/", UserRegistrationView.as_view(), name="signup"),
    path("logout/", user_logout, name="logout"),
    path("profile/", user_profile, name="profile"),
    path("profile/change_password/", UserPasswordChangeView.as_view(), name="change_password"),
]

