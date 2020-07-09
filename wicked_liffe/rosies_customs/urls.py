from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import item_list


from . import views

app_name = 'rosies_customs'

urlpatterns = [
    path('', item_list, name='item_list'),
    path('', views.index, name='index'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
