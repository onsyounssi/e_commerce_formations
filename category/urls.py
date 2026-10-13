from django.urls import path
from . import views 

urlpatterns = [
    path ('all_catergories',views.get_all_catergory, name= "get_all_categories"),
    path('create_categories', views.create_category, name="create a categories"),
    path('get_category_by_id/<int:id>', views.get_category_by_id, name= "get category by id"),
    path('delete_category/<int:category_id>', views.delete_category, name="delete"),
    path('update category/<int:pk>', views.update_category, name="update category"),
    
    path('get_all_subcategories', views.get_all_subcategory, name="get_all_subcategory"),
    path('subcategory_by_id/<int:id>', views.get_subcategory_by_id, name="get_subcategory_by_id"),
    path('create_subCategory',views.create_sub_category, name="create_sub_category"),
    path('update_subcategory/<int:id>', views.update_subcategory, name="update_subcategory"),
    path('delete_subcategory/<int:id>', views.delete_subcategory, name="delete a subCategory"),
    
    path('get_subcategory_by_category', views.get_subcategory_by_category, name="get_subcategory_by_category")
]

