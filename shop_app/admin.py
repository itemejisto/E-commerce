from django.contrib import admin
from .models import shop,categories

# Register your models here.

class catadmin(admin.ModelAdmin):
    # list_display = ['name', 'price', 'stock', 'img', 'category']
    # list_editable = ('price', 'stock', 'img')
    prepopulated_fields = {'slug':('name',)}
admin.site.register(categories,catadmin)
class shopadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','img','category']
    list_editable = ('price','stock','img')
    prepopulated_fields = {'slug':('name',)}
admin.site.register(shop,shopadmin)