from django.contrib import admin
from django.urls import path
from .views import get_employee
from .views import save_employee
from .views import update_employee
from .views import delete_employee
from . import views

urlpattern = [
    path("admin/", admin.site.urls),
    path("employee/", get_employee),
    path("save_employee/", save_employee),
    path("update_employee/<int:id>", update_employee),
    path("delete_employee/<int:id>", delete_employee),
]

urlpatterns = [
    path("",views.index),
    path("new", views.new)
]