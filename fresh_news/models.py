from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    from_source = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ["publish_date"]

    def __str__(self) -> str:
        return str(self.title)
