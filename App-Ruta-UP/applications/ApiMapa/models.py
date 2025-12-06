from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ComentarioTransito(models.Model):
    """
    Modelo para almacenar comentarios y consejos sobre tránsito
    que los usuarios pueden compartir.
    
    NOTA: El campo usuario es opcional por ahora para permitir comentarios anónimos.
    Cuando se implemente la autenticación, se puede hacer obligatorio.
    """
    CATEGORIAS = [
        ('trafico', 'Tráfico'),
        ('seguridad', 'Seguridad'),
        ('ruta_alt', 'Ruta Alternativa'),
        ('consejo', 'Consejo General'),
        ('otro', 'Otro'),
    ]
    
    # Usuario opcional - preparado para autenticación futura
    usuario = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        related_name='comentarios_transito',
        null=True,
        blank=True,
        help_text="Opcional por ahora - se hará obligatorio al implementar autenticación"
    )
    nombre_anonimo = models.CharField(
        max_length=100,
        default='Anónimo',
        help_text="Nombre mostrado cuando no hay usuario registrado"
    )
    contenido = models.TextField(max_length=500, help_text="Máximo 500 caracteres")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='consejo')
    
    # Ubicación opcional para comentarios específicos de un lugar
    ubicacion_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    ubicacion_lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    # Fechas automáticas
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha_creacion']  # Más recientes primero
        verbose_name = 'Comentario de Tránsito'
        verbose_name_plural = 'Comentarios de Tránsito'
    
    def get_nombre_usuario(self):
        """Retorna el nombre del usuario o 'Anónimo'"""
        if self.usuario:
            return self.usuario.username
        return self.nombre_anonimo
    
    def __str__(self):
        return f"{self.get_nombre_usuario()} - {self.get_categoria_display()} - {self.fecha_creacion.strftime('%Y-%m-%d %H:%M')}"
