from django import template

register = template.Library()

@register.filter(name='top_rated')
def top_rated(products, count=4):
    if products is not None:
        return products.order_by('-rating')[:count]
    return []

@register.filter(name='high_sales_count')
def high_sales_count(products, count=4):
    if products is not None:
        return products.order_by('-sales_count')[:count]
    return []
