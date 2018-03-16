from django.shortcuts import render, redirect
from .models import *
from .form import *

# Create your views here.


def vista_jugador(request):
	lista = jugador.objects.filter()

	return render(request, 'jugador.html', locals())	

def vista_equipo(request):
	equi = equipo.objects.filter()

	return render(request, 'equipo.html', locals())

def vista_torneo(request):
	torne= torneo.objects.filter()

	return render(request, 'torneo.html', locals())	


def agregar_jugador(request):
	if request.method == 'POST':
		formulario = agregar_jugador_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.save()
			formulario.save_m2m()
			return redirect('/jugador/')
	else:
		formulario = agregar_jugador_form()
	return render(request, 'agregar.html', locals())

def editar_jugador(request, id_jug):
	jug = jugador.objects.get(id=id_jug)
	if request.method == 'POST':
		formulario = agregar_jugador_form(request.POST, request.FILES,instance= jug)
		if formulario.is_valid():
			jug = formulario.save()
			return redirect('/jugador/')
	else:
		formulario = agregar_jugador_form(instance = jug)
	return render(request, 'editar_jugador.html', locals())

