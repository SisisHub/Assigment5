from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ("make","carmodel", "year", "location", "status")


admin.site.register(Car, CarAdmin)
#we are using the admin that is importet form top line
# and using attrivute site. witch is an object itself.
#and site /object has a method called register
# we are calling that method and passing our Cars class as an argument
# with this we are telling django. that we wanna manage our products.
#in the admin area