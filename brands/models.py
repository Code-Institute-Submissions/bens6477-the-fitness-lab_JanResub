from django.db import models


class Brand(models.Model):
    """
    Class for the brand model
    """

    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
