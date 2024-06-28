from django.db import models


class News(models.Model):
    title = models.TextField()
    text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True, null=True)
    from_source = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ["publish_date"]

    def __str__(self) -> str:
        return str(self.title)
