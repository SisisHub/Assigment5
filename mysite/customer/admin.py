from django.contrib import admin
from .models import Customer

#class OfferAdmin(admin.ModelAdmin):
  #  list_display = ("code", "price")


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name","age", "address")

#admin.site.register(Offer, OfferAdmin)
admin.site.register(Customer, CustomerAdmin)
