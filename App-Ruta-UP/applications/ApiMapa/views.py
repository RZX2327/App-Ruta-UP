from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ComentarioTransito

def home(request):
    """Vista para la página principal"""
    return render(request, "home.html")

def mapa(request):
    """Vista del mapa con comentarios de tránsito"""
    # Obtener últimos 20 comentarios ordenados por más recientes
    comentarios = ComentarioTransito.objects.all()[:20]
    
    context = {
        "google_maps_api_key": "AIzaSyA7izHCdS0uL3kWzoqgs-d7nFXmcU8Vgcs",
        "latitud": 7.3757,    
        "longitud": -72.648,
        "comentarios": comentarios,
        "categorias": ComentarioTransito.CATEGORIAS,
    }
    return render(request, "ApiMapa/mapa.html", context)

# @login_required  # DESCOMENTAR cuando se implemente autenticación
def crear_comentario(request):
    """
    Vista para crear un nuevo comentario de tránsito.
    
    NOTA: Por ahora permite comentarios anónimos.
    Cuando se implemente autenticación, descomentar @login_required arriba
    y asignar request.user al campo usuario del comentario.
    """
    if request.method == 'POST':
        contenido = request.POST.get('contenido', '').strip()
        categoria = request.POST.get('categoria', 'consejo')
        nombre = request.POST.get('nombre', 'Anónimo').strip() or 'Anónimo'
        
        if contenido:
            if len(contenido) > 500:
                messages.error(request, 'El comentario no puede exceder 500 caracteres.')
            else:
                # Por ahora creamos comentario anónimo
                # FUTURO: Cuando haya autenticación, hacer: usuario=request.user
                ComentarioTransito.objects.create(
                    nombre_anonimo=nombre,
                    contenido=contenido,
                    categoria=categoria
                )
                messages.success(request, '¡Comentario publicado exitosamente!')
        else:
            messages.error(request, 'El comentario no puede estar vacío.')
        
        return redirect('apimapa:mapa')
    
    return redirect('apimapa:mapa')
