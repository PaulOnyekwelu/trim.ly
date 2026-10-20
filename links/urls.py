from django.urls import path
from .views import index, root_link, create_link

urlpatterns = [
    path("", index, name="home"),
    path("<str:slug>/", root_link, name="root-link"),
    path("link/create/", create_link, name="create-link"),
]
