from app.views import agregar, editar, eliminar, index
from django.urls import path # Se importa el index desde urls del app

urlpatterns = [
    path('', index, name='index'), # Se agrega la ruta
    path('agregar/', agregar, name='agregar'),
    path('editar/<int:id>/', editar, name='editar'),
    path('eliminar/<int:id>/', eliminar, name='eliminar') #Se necesita una url para que funcione
]