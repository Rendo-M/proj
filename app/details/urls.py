from django.urls import include, path, re_path, register_converter
from . import views, converter

register_converter(converter.ACLNConverter, "acln")
urlpatterns = [
    path('', views.index),
    path('list/', views.details, name='details'),
    path('data/', views.load, name='load'),
    path('<acln:specification>/', views.number, name='number'),
    path('upload/', views.image_upload, name='upload'),
]