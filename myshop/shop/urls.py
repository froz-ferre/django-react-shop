from django.urls import path, re_path
from . import views

urlpatterns = [
    #home page 'www.example.com'
    path('', views.home, name='index'),
    #product page 'www.example.com/product/product_name'
    re_path(r'product/(?P<slug>[^/]+)', views.product_detail, name='product'),
    #category page 'www.example.com/category/category_slug'
    re_path(r'category/(?P<slug>[^/]+)', views.category_list, name='product'),
]