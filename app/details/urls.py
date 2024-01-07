from django.urls import include, path, re_path, register_converter
from . import views, converter

register_converter(converter.ACLNConverter, "acln")
urlpatterns = [
    path('', views.details),
    path('list/', views.details),
    path('<acln:specification>/', views.number, name='number'),
    
]