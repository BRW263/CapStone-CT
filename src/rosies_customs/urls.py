from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # need to add auth for login
    # path('', include(''))
]