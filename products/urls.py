from django.urls import path
from . import views

urlpatterns =  [
    path('create', views.add_product, name="add_product"),
    path('all_products',views.all_products, name="all_products"),
    path('delete_products/<int:product_id>',views.delete_products,name="delete_products"),
    path('product_details/<int:pk>',views.product_details, name="product_details"),
    
    path('update_product/<int:product_id>',views.update_product, name="update_product"),
    path('get_product_by_subcategory', views.get_product_by_subcategory, name="get_product_by_subcategory"),
    path('search_product', views.search_product, name="search_product"),
    path('filter_products',views.filter_products,name="filter_products"),
    path('init_categories_and_subcategories',views.init_categories_and_subcategories,name="init_categories_and_subcategories")

 ]