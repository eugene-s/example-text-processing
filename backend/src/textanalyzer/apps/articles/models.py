from django.db import models


class Article(models.Model):
    body = models.TextField()
