from django.db import models


class ListItem(models.Model):
    name = models.CharField(max_length=200)
