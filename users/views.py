from rest_framework import generics
from rest_framework.authentication import SessionAuthentication

from users.models import User
from users.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]

    def get_object(self):
        return self.request.user
