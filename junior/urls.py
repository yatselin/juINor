from django.contrib import admin
from django.urls import include, path
from django.contrib.flatpages import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("about/", include("django.contrib.flatpages.urls")),
    path("", include("jobs.urls")),
]

urlpatterns += [
        path(
            'about-project/',
            views.flatpage,
            {'url': '/about-project/'},
            name='about'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)