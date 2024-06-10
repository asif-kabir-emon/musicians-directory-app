from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("musician/", include("musician.urls")),
    path("album/", include("album.urls")),
    path("user/", include("user.urls")),
]
