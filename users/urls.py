from django.urls import path

from users.views import UserActivationView, UserMeView, CreateUserView, UserPasswordView, UserUsernameView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("", CreateUserView.as_view({"post": "perform_create"}), name="create_user"),
    path("me/", UserMeView.as_view(), name="manage"),

    path("activation/<uid>/<token>/", UserActivationView.as_view({"post": "activation"}), name="user-activation"),
    path("resend_activation/", UserActivationView.as_view({"post": "resend_activation"}), name="user-resend-activation"),

    path("set_password/", UserPasswordView.as_view({"post": "set_password"}), name="user-set-password"),
    path("reset_password/", UserPasswordView.as_view({"post": "reset_password"}), name="user-reset-password"),
    path("reset_password_confirm/<uid>/<token>/", UserPasswordView.as_view({"post": "reset_password_confirm"}), name="user-reset-password-confirm"),

    path("set_username/", UserUsernameView.as_view({"post": "set_username"}), name="user-set-username"),
    path("reset_username/", UserUsernameView.as_view({"post": "reset_username"}), name="user-reset-username"),
    path("reset_username_confirm/<uid>/<token>/", UserUsernameView.as_view({"post": "reset_username_confirm"}), name="user-reset-username-confirm"),
    path("logout/", LogoutView.as_view(), name="logout")
]

app_name = "user"
