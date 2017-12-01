from django.conf.urls import url
from . import views
from django.views import static
from django.conf import settings
from .upoads import upload_image

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r"^uploads/(?P<path>.*)$", static.serve, {"document_root": settings.MEDIA_ROOT},),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
]
