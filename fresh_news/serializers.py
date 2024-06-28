from rest_framework import serializers

from fresh_news.models import News


class FreshNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = "__all__"
