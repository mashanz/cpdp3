from django.urls import path
from . import views

urlpatterns = [
    path("", views.list.view),
    path("create/", views.create.view),
    path("id/<str:id>", views.read.view)
]