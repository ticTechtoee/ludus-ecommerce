from django.shortcuts import render
from .models import Category, Subcategory, Product

def ViewIndexPage(request):
    return render(request, 'homeApp/index.html')

def ViewShopSideVersion(request):
    categories = Category.objects.all()
    subcategory = Subcategory.objects.all()
    products = Product.objects.all()

    context = {'categories': categories, 'subcategories': subcategory, 'products':products}
    return render(request, 'homeApp/shop_side_version.html', context)