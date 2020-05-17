from django.contrib import admin
from django.urls import include, path
from django.contrib.flatpages import views


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
