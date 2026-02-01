"""
URL configuration for shop_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from shop_app import views
from django.conf.urls.static import static

from shop_app.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop_cart.urls')),
    path('',views.index,name='index'),
    path('search/',views.search,name='search'),
    path('<slug:c_slug>/',views.index,name='prod_cat'),
    path('shop/<int:shop_id>',views.details,name='details'),
    path('add.html',views.add,name='add'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('category/<str:cat>/', views.category, name='category'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


