from django.urls import path
from .views import list_customers, list_menus, menu_details

urlpatterns = [
    path('',list_customers, name='list_customers'),
    path('<customer_id>/',list_menus, name='list_menus'),
    #path('<customer_id>/<menu_id>/', menu_details, name='menu_details'),
]