from django.shortcuts import render
from wishlist.models import ItemWishlist

# Create your views here.
def show_wishlist(request):
    data_wishlist_item = WishlistItem.objects.all()
    context = {
    'list_item': data_wishlist_item,
    'name': 'Nataya'
    }
    return render(request, "wishlist.html", context)