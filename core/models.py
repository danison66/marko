from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
