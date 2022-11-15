from django.contrib import admin
from django.urls import path
from .views import get_customer
from .views import save_customer
from .views import update_customer
from .views import delete_customer
from . import views

urlpattern = [
    path("admin/", admin.site.urls),
    path("customer/", get_customer),
    path("save_customer/", save_customer),
    path("update_customer/<int:id>", update_customer),
    path("delete_customer/<int:id>", delete_customer),

]

urlpatterns = [
    path("",views.index),
    path("new", views.new)
]