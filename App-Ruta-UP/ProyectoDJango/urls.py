from django.contrib import admin
from django.urls import path, include
from applications.ApiMapa.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("apimapa/", include("applications.ApiMapa.urls")),
    path("", home, name="home"),
    path("usuarios/", include("applications.usuarios.urls", namespace="usuarios")),
]
