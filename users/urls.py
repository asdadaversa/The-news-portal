from django.urls import path

from users.views import CreateUserView, ManageUserView


urlpatterns = [
    path("", CreateUserView.as_view(), name="register"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

app_name = "user"
