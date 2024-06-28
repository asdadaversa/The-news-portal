from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from fresh_news.models import News
from fresh_news.permissions import IsAdminOrReadOnly
from fresh_news.serializers import FreshNewsSerializer
from pagination import NewsPagination


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = FreshNewsSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = NewsPagination

    def list(self, request, *args, **kwargs):
        title = request.query_params.get("title")
        text = request.query_params.get("text")
        publish_date = request.query_params.get("publish_date")
        from_source = request.query_params.get("from_source")
        image_url = request.query_params.get("image_url")
        queryset = self.get_queryset()

        if title:
            queryset = queryset.filter(title__icontains=title)
        if text:
            queryset = queryset.filter(text__icontains=text)
        if publish_date:
            queryset = queryset.filter(publish_date__date=publish_date)
        if from_source:
            queryset = queryset.filter(from_source__icontains=from_source)
        if image_url:
            image_url_bool = True if image_url.lower() == 'true' else False
            if image_url_bool:
                queryset = queryset.filter(image_url__isnull=False)
            else:
                queryset = queryset.filter(image_url__isnull=True)

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
