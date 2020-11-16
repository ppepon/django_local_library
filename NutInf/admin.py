from django.contrib import admin
from NutInf.models import Nutinf, Products, NutProduct

class NutinfAdmin(admin.ModelAdmin):
    list_display=("name", "unit")
    
class ProductsAdmin(admin.ModelAdmin):
    list_display=("name_product", "description", "active")

class NutProductAdmin(admin.ModelAdmin):
    list_display=("product_id", "nut_id", "quantity")
    

admin.site.register(Nutinf, NutinfAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(NutProduct, NutProductAdmin)





