from django.urls import path
from .views import item_list

app_name = 'rosies_customs'

urlpatterns = [
    path('', item_list, name='item_list'),
]
