from django.shortcuts import render

from .models import Category, Subcategory, Product, Color, Size



def ViewIndexPage(request):
    # Fetch all categories
    categories = Category.objects.all()

    # Dictionary to store products for each category
    category_products = {}

    # Loop through categories and get products for each category
    for category in categories:
        # Get products for the current category and order them as needed
        products = Product.objects.filter(subcategory__category=category)

        latest_products = products.order_by('-created_at')[:3]
        best_selling_products = products.order_by('-sales_count')[:3]
        top_rated_products = products.order_by('-rating')[:3]
        featured_products = products.filter(is_featured=True)[:3]

        # Store the product lists in the dictionary
        category_products[category] = {
            'latest_products': latest_products,
            'best_selling_products': best_selling_products,
            'top_rated_products': top_rated_products,
            'featured_products': featured_products,
        }

    context = {
        'categories': categories,
        'category_products': category_products,
    }
    return render(request, 'homeApp/index.html', context)


def ViewShopSideVersion(request):
    get_categories = Category.objects.all()
    get_color = Product.objects.values('color__color_code').distinct()

    get_size = Product.objects.values('name').distinct()


    context = {'Categories': get_categories, 'Colors': get_color, 'Sizes': get_size}
    return render(request, 'homeApp/shop_side_version.html', context)