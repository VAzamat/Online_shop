from itertools import product

from django.shortcuts import render

from dealer.models import Product


# Create your views here.

def index(request):
    products = Product.objects.all()
    for product_item in products:
        max_lenght = 100
        if len(product_item.description)>max_lenght:
            product_item.description = product_item.description[0:max_lenght] + "..."


    context = {
        'product_list': products
    }

    return render(request, 'dealer/mainpage.html', context)

