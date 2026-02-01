from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/',views.cart,name='cart'),
    path('add/<int:product_id>/',views.add_item,name='addtocart'),
    path('minus/<int:product_id>/',views.min_cart,name='minuscart'),
    path('del/<int:product_id>/',views.delete_cart,name='deletecart'),
    ]