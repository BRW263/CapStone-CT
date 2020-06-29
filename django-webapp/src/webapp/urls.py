from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', include('social_django.urls')), #  responsible for the callback URL that Auth0 calls after the authentication process. 
    path('profile/', views.profile),
    path('', include('django.contrib.auth.urls')),
]