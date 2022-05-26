from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]