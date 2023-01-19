from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Brand


class Brands(generic.ListView):
    """
    A view to return the list of brands
    """

    model = Brand
    context_object_name = "brands"
    template_name = "brands/brands.html"