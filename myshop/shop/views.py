
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.template.loader import render_to_string, get_template

# home page
# localhost/
def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    context = {
        'title': 'ICU',
        'categories': categories,
        'products': products 
    }
    return HttpResponse(render_to_string('index.html', context))


# product detail page
# localhost/product/product_name
def product_detail(request, slug):
    categories = Category.objects.all()
    product = Product.objects.get(slug = slug)
    context = {
        'product': product, 
        'categories': categories
    }
    return HttpResponse(render_to_string('detail.html', context))
    

# page with products within category
# localhost/category/category_name
def category_list(request, slug):
    category = slug
    category_id = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=category_id, available = True)
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return HttpResponse(render_to_string('index.html', context))