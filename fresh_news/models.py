from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["publish_date"]

    def __str__(self) -> str:
        return str(self.title)
