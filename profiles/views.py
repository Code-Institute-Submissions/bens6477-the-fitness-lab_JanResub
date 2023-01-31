from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Newsletter
from .forms import UserProfileForm, NewsletterForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    newsletters = Newsletter.objects.all().filter(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'newsletters': newsletters,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def add_newsletter(request):
    """ Display the user's newsletter page. """
    newsletter = Newsletter(user=request.user)

    if request.method == 'POST':
        form = NewsletterForm(request.POST, request.FILES, instance=newsletter)
        if form.is_valid():
            form.save()
            messages.success(request, 'Newsletter updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure the form is valid.'))
    else:
        form = NewsletterForm(instance=newsletter)

    template = 'profiles/add_newsletter.html'
    context = {
        'form': form,
        'newsletter': newsletter,
    }

    return render(request, template, context)


@login_required
def edit_newsletter(request, newsletter_id):
    """ Display the user's newsletter page. """
    newsletter = Newsletter.objects.get(pk=newsletter_id)

    if request.method == 'POST':
        form = NewsletterForm(request.POST, request.FILES, instance=newsletter)
        if form.is_valid():
            form.save()
            messages.success(request, 'Newsletter updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure the form is valid.'))
    else:
        form = NewsletterForm(instance=newsletter)

    template = 'profiles/edit_newsletter.html'
    context = {
        'form': form,
        'newsletter': newsletter,
    }

    return render(request, template, context)


@login_required
def delete_newsletter(request, newsletter_id):
    """ Display the user's newsletter page. """
    newsletter = get_object_or_404(Newsletter, pk=newsletter_id)
    newsletter.delete()
    messages.success(request, 'Email deleted!')
    return redirect(reverse('profile'))


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
