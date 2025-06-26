from orders import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('cart/',views.show_cart, name='cart'),
    path('add_to_cart/',views.add_to_cart, name='add_to_cart'),
    path('remove_item_cart/<pk>',views.remove_item_cart,name="remove_item"),
    path('check_out/',views.check_out,name="checkout"),
    path('orders/',views.show_orders,name="orders"),


]

