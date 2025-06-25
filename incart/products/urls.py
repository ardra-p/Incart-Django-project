from products import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name = 'home'),
    path('products_list',views.products_list, name='list_product'),
    path('products_details/<pk>',views.products_detail, name='detail_product'),


]

