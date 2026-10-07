from django.urls import path
from . import views 

urlpatterns = [
    path ('signin',views.sign_in, name= "login"),
    path ('logout',views.logout_view, name= "logout")
]
