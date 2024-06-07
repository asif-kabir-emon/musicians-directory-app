from django.urls import path
from .views import add_album, delete_album, edit_album

urlpatterns = [
    path("add/", add_album, name="add_album"),
    path("delete/<int:id>/", delete_album, name="delete_album"),
    path("edit/<int:id>/", edit_album, name="edit_album"),
]