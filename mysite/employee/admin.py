from django.contrib import admin
from .models import Employee#, Offer


#class OfferAdmin(admin.ModelAdmin):
   # list_display = ("code", "price")


class EmAdmin(admin.ModelAdmin):
    list_display = ("name","address", "branch")

#admin.site.register(Offer, OfferAdmin)
admin.site.register(Employee, EmAdmin)