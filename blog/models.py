from django.db import models

from main.models import Post


class Comment (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


# Create your models here.
