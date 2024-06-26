from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
 #   author = models.ForeignKey(
 #       "auth.User",
 #       on_delete=models.CASCADE,
 #   )
    author = models.CharField(max_length=20)
    body = models.TextField()
    liczby = models.TextField()
    suma = models.IntegerField()
    URL = models.URLField()
    time = models.TimeField()
    decimal = models.DecimalField(max_digits = 5, decimal_places = 3)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
