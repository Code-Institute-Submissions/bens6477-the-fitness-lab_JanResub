from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Item, Category, Review
from .forms import ItemForm, ReviewForm


def all_items(request):
    """ A view to show all items, including sorting and search queries """
    items = Item.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                items = items.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            items = items.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            items = items.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('items'))

            queries = (Q(name__icontains=query)
                       | Q(description__icontains=query))
            items = items.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'items': items,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'items/items.html', context)


def item_detail(request, item_id):
    """ A view to show individual item details """
    item = get_object_or_404(Item, pk=item_id)
    category = item.category
    user_id = request.user
    similar_items = Item.objects.all().filter(
        category=category).exclude(id=item_id)
    reviews = item.item_review.order_by('review_date')
    form = ReviewForm()
    template = 'items/item_detail.html'
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=item)
        if form.is_valid():
            review = Review()
            review.item = item
            review.user = request.user
            review.body = form.cleaned_data["body"]
            review.save()
            return redirect('item_detail', item_id=item_id)

    context = {
        'item': item,
        'similar_items': similar_items,
        'reviews': reviews,
        'form': form,
    }
    return render(request, template, context)


@login_required
def add_item(request):
    """ Add a item to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse('add_item'))
        else:
            messages.error(request,
                           ('Failed to add item. '
                            'Please ensure the form is valid.'))
    else:
        form = ItemForm()

    template = 'items/add_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_item(request, item_id):
    """ Edit a item in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse('item_detail', args=[item.id]))
        else:
            messages.error(request,
                           ('Failed to update item. '
                            'Please ensure the form is valid.'))
    else:
        form = ItemForm(instance=item)
        messages.info(request, f'You are editing {item.name}')

    template = 'items/edit_item.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


@login_required
def delete_item(request, item_id):
    """ Delete a item from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    messages.success(request, 'Item deleted!')
    return redirect(reverse('items'))


def edit_review(request, review_id):
    """ A view to show individual item details """
    review = get_object_or_404(Review, pk=review_id)
    item_id = review.item_id
    item = get_object_or_404(Item, pk=item_id)
    user_id = request.user
    form = ReviewForm()
    template = 'items/item_detail.html'
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=item)
        if form.is_valid():
            review = Review()
            review.item = item
            review.user = request.user
            review.body = form.cleaned_data["body"]
            review.save()
            # return redirect('item_detail', item_id=item_id)

    context = {
        'item': item,
        'item_id': item_id,
        'form': form,
    }
    return render(request, template, context)


def delete_review(request, review_id):
    """
    Deletes a users review from the 'Review' model
    """
    review = get_object_or_404(Review, pk=review_id)
    item_id = review.item_id
    review.delete()
    return redirect('item_detail', item_id=item_id)
