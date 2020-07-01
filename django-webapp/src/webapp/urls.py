from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.conf.urls import url

from . import views

admin.autodiscover()
admin.site.login = login_required(admin.site.login)


urlpatterns = [
    path('', views.index, name='index'),
    path('', include('social_django.urls')), #  responsible for the callback URL that Auth0 calls after the authentication process. 
    path('profile/', views.profile),
    path('logout/', views.logout),
]

app_name = 'cart'

urlpatterns = [
    url(r'^$', views.cart_detail, name = 'cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name = 'cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name = 'cart_remove')
]