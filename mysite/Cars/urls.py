from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from .views import get_cars
from .views import save_car
from .views import update_car
from .views import delete_car

urlpatterns = [
    path("",views.index),
    path("new", views.new)
]
urlpattern = [
    path("admin/", admin.site.urls),
    path("cars/", get_cars),
    path("save_car/", save_car),
    path("update_car/<int:id>", update_car),
    path("delete_car/<int:id>", delete_car),

]