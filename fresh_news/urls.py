from rest_framework import routers

from fresh_news.views import NewsViewSet


router = routers.DefaultRouter()
router.register("", NewsViewSet, basename="fresh_news")


urlpatterns = router.urls


app_name = "fresh_news"
