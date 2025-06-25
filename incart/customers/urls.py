from customers import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('account/',views.show_account, name='account'),
    path('logout/',views.signout, name='logout'),


]

