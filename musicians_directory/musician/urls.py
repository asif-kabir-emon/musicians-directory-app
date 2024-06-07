from django.urls import path
from .views import add_musician

urlpatterns = [
    path("add/", add_musician, name="add_musician"),
]