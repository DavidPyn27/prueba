from django.urls import path
from .views import *

urlpatterns = [

	path('',vista_jugador, name= 'vista_jugador'),
	path('jugador/',vista_jugador, name= 'vista_jugador'),
	path('equipo/',vista_equipo, name= 'vista_equipo'),
	path('torneo/',vista_torneo, name= 'vista_torneo'),
	path('agregar_jugador/', agregar_jugador, name='vista_agregar_jugador'),
	path('editar_jugador/<int:id_jug>/', editar_jugador, name='editar_jugador'),
]	