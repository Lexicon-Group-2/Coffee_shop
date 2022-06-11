from django.contrib.auth.decorators import login_required
from coffee_store.models import Product

# This will be updated once we have our db
def items_processor(request):
    if request.user.is_authenticated:
        num_items = 80
    else:
        num_items = 0
    return {
        'num_items' : num_items
    }

def arrow(request):
    arrow = "&#10140;"
    return {'arrow': arrow}


def favorite_items(request):
    favorite_items = 0
    image = "/media/wish_list_empty.png"
    if request.user.is_authenticated:
        products = Product.objects.filter(favourites=request.user)
        favorite_items = len(products)
        if favorite_items == 0:
            image = "/media/wish_list_empty.png"
        else:
            image = "/media/wish_list.png"
    return {'favorite_items': favorite_items, 'favorite_items_image': image}