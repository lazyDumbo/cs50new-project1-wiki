from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.title,name="title"),
    path("search",views.search,name="search"),
    path("new",views.new,name="new"),
    path("random",views.random1,name="random"),
    path("edit/<str:title>",views.edit,name="edit")
]
