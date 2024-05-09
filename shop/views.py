from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

def index(request):
    products = Product.objects.all()
    context = { "product_objects": products }

    search = request.GET.get('search')
    if search != '' and search is not None:
        products = Product.objects.filter(title__icontains=search)


    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = { "product_objects": products }
    return render(request, 'shop/index.html', context)

def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', { "product": product })

