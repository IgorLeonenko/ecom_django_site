from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    context = { "product_objects": products }

    search = request.GET.get('search')
    if search != '' and search is not None:
        products = Product.objects.filter(title__icontains=search)
        context = { "product_objects": products }
    return render(request, 'shop/index.html', context)

