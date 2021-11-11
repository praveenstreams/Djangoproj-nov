
from django.contrib import admin
from django.urls import path,include
from student_admin import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(urls),name="urls")
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)