from django.db import models


class Category(models.Model):
    """ Model for categories of items """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    display_name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Item(models.Model):
    """ Model for the details of items """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=25, null=True, blank=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    sku = models.CharField(max_length=250, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=25, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
