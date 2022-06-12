from coffee_store.models import Product
from shopping_cart.models import Order

# This will be updated once we have our db
def items_processor(request):
    order = ""
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, completed=False)
            num_items = order.get_cart_items
        except:
            num_items = 0
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
            favorite_items = ""
        else:
            image = "/media/wish_list.png"
    return {'favorite_items': favorite_items, 'favorite_items_image': image}