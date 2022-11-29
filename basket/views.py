from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from items.models import Item


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified item to the basket """

    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'item_size' in request.POST:
        size = request.POST['item_size']
    basket = request.session.get('basket', {})

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 (f'Updated size {size.upper()} '
                                  f'{item.name} quantity to '
                                  f'{basket[item_id]["items_by_size"][size]}'))
            else:
                basket[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 (f'Added size {size.upper()} '
                                  f'{item.name} to your basket'))
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             (f'Added size {size.upper()} '
                              f'{item.name} to your basket'))
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request,
                             (f'Updated {item.name} '
                              f'quantity to {basket[item_id]}'))
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {item.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust the quantity of the specified item to the specified amount"""

    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'item_size' in request.POST:
        size = request.POST['item_size']
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             (f'Updated size {size.upper()} '
                              f'{item.name} quantity to '
                              f'{basket[item_id]["items_by_size"][size]}'))
        else:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
                messages.success(request,
                                 (f'Removed size {size.upper()} '
                                  f'{item.name} from your basket'))
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request,
                             (f'Updated {item.name} '
                              f'quantity to {basket[item_id]}'))
        else:
            basket.pop(item_id)
            messages.success(request,
                             (f'Removed {item.name} '
                              f'from your basket'))

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        print('remove_from_basket')
        item = get_object_or_404(Item, pk=item_id)
        size = None
        if 'item_size' in request.POST:
            size = request.POST['item_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{item.name} from your basket'))
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {item.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
