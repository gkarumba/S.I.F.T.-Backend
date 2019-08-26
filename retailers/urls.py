from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^products/(?P<search_term>.+)/$', ProductsList.as_view() )
    url(r'^products/', ProductsList.as_view() ),
    url(r'^location/', GetSearcherLocation.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)