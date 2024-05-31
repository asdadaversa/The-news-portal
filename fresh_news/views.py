from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from fresh_news.models import News
from fresh_news.permissions import IsAdminOrReadOnly
from fresh_news.serializers import FreshNewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = FreshNewsSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = IsAdminOrReadOnly
