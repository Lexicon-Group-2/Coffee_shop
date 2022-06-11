

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