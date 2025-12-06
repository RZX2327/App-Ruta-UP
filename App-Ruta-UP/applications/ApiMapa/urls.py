from django.urls import path
from .views import mapa, crear_comentario

app_name = "apimapa"

urlpatterns = [
    path("mapa/", mapa, name="mapa"),
    path("comentario/crear/", crear_comentario, name="crear_comentario"),
]
