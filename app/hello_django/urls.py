from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    #path("upload/", image_upload, name="upload"),
    path("admin/", admin.site.urls),
     path('details/', include('details.urls'), name='details'),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
