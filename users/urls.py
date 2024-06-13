from django.urls import path

from users.views import UserActivationView, UserMeView, CreateUserView, UserPasswordView, UserUsernameView

urlpatterns = [
    path("", CreateUserView.as_view({"post": "perform_create"}), name="your_create_user"),
    path("me/", UserMeView.as_view(), name="manage"),

    path("activation/<uid>/<token>/", UserActivationView.as_view({"post": "activation"}), name="user-activation"),
    path("resend_activation/", UserActivationView.as_view({"post": "resend_activation"}), name="user-resend-activation"),

    path("set_password/", UserPasswordView.as_view({"post": "set_password"}), name="user-set-password"),
    path("reset_password/", UserPasswordView.as_view({"post": "reset_password"}), name="user-reset-password"),
    path("reset_password_confirm/<uid>/<token>/", UserPasswordView.as_view({"post": "reset_password_confirm"}), name="user-reset-password-confirm"),

    path("set_username/", UserUsernameView.as_view({"post": "set_username"}), name="user-set-username"),
    path("reset_username/", UserUsernameView.as_view({"post": "reset_username"}), name="user-reset-username"),
    path("reset_username_confirm/<uid>/<token>/", UserUsernameView.as_view({"post": "reset_username_confirm"}), name="user-reset-username-confirm"),
]

app_name = "user"
