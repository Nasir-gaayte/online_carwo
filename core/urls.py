from django.urls import path
from core import views




urlpatterns = [
    path('',views.home,name='home'),
    path('add_shop/',views.add_shop,name='add_shop'),
]
