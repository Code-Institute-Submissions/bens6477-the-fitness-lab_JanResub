from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('items'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51M5beOEwQb125L9hmnxfCmUx11zmTccHLCBjiLjjEm8HCuVgWDWByxd4q4zkJThsUU2i5kCik0wE3pvyBwwDvFJc00xAo4CsEY',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)