from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item_view', views.item_view, name='item')
]