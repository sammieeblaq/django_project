from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="user-home"),
    path("add/", views.add, name="add-user"),
    path("add_form_submission/", views.add_form_submission, name="add_form_submission"),
    path("list/", views.list, name="list-user")
]