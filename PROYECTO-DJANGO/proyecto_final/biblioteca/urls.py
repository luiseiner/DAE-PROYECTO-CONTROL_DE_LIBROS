from django.urls import path
from . import views

urlpatterns = [
    path('prestamos/', views.lista_prestamos),
    # Agrega más rutas URL para tus modelos si es necesario
]
