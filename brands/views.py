from django.views import generic

from .models import Brand


class Brands(generic.ListView):
    """
    A view to return the list of brands
    """

    model = Brand
    context_object_name = "brands"
    template_name = "brands/brands.html"
