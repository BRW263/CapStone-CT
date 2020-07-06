from django.urls import include, path
from .views import item_list

from . import views

app_name = 'rosies_customs'

urlpatterns = [
    path('', item_list, name='item_list'),
    path('', views.index, name='index'),
    path('', include('allauth.urls'))
]
