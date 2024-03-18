from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
 #   author = models.ForeignKey(
 #       "auth.User",
 #       on_delete=models.CASCADE,
 #   )
    author = models.CharField(max_length=20)
    nazwa = models.TextField()
    smiles = models.TextField()
    cieplo = models.FloatField()
    energia = models.FloatField()
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
