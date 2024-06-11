from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, Order

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

def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address_1 = request.POST.get('address_1', '')
        address_2 = request.POST.get('address_2', '')
        address = f"{address_1} {address_2}"
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        items = request.POST.get('items', '')
        total = request.POST.get('total', '')

        print(f"Total: {items}")

        order = Order(name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, items=items, total=float(total))
        order.save()

    return render(request, 'shop/checkout.html')

