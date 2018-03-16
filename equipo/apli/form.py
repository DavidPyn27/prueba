from django import forms
from .models import *


class agregar_jugador_form(forms.ModelForm):
	class Meta:
		model = jugador
		fields = '__all__'