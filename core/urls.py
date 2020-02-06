from django.urls import path
from .views import index, product, about


app_name = "core"

urlpatterns = [
    path('', index, name='index'),
    path('product/', product, name='product'),
    path('about/', about, name='about'),

]
