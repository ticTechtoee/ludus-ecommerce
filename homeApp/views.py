from django.shortcuts import render

from .models import MainCategory, Product, Color, Size



def ViewIndexPage(request):
    # Fetch all categories
    categories = MainCategory.objects.all()

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
    get_categories = MainCategory.objects.all()

    # Query to retrieve all products
    get_product = Product.objects.all()

    # Create an empty dictionary to store the count of each color
    color_counts = {}
    size_counts = {}

    # Iterate through each product and update the color counts
    for item in get_product:
        color = item.color
        size = item.size
        if color:
            color_code = color.color_code
            if color_code in color_counts:
                color_counts[color_code] += 1
            else:
                color_counts[color_code] = 1
        if size:
            item_size = size.name
            if item_size in size_counts:
                size_counts[item_size] += 1
            else:
                size_counts[item_size] = 1



    context = {'Categories': get_categories, 'Colors': color_counts.items(), "Sizes":size_counts.items()}
    return render(request, 'homeApp/shop_side_version.html', context)