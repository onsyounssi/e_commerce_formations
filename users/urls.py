from django.urls import path
from . import views
urlpatterns = [
    path("create_user", views.add_user, name="add_user"),
    path("get_users", views.get_users, name="all_users"),
    path("delete_users/<int:pk>", views.delete_users,name="delete_users"),
    path("update_users/<int:pk>", views.update_user,name="update_user"),
    path("disable_user/<int:user_id>", views.disable_user, name="disable_user"),
    path("toggle_user/<int:user_id>", views.toggle_user, name="toggle_user"),
    path("change_password/<int:user_id>", views.change_password, name="change_password")
    
    
]
