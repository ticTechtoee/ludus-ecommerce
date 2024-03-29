from django.contrib import admin
from .models import Size, Color, MainCategory, Subcategory, Product

# List of models to register
models_to_register = [Size, Color, MainCategory, Subcategory,Product]

# Register all models in the list
for model in models_to_register:
    admin.site.register(model)