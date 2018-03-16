from django.db import models

# Create your models here.
class equipo(models.Model):
	nombre = models.CharField(max_length = 100)
	pais = models.CharField(max_length = 30)
	ciudad = models.CharField(max_length = 30)

	def __str__(self):
		return self.nombre

class torneo(models.Model):
	nombre = models.CharField(max_length = 100)
	lugar = models.CharField(max_length = 50)
	fecha = models.DateField()
	equipo = models.ManyToManyField(equipo, null =True, blank= True)

	def __str__(self):
		return self.nombre

class jugador(models.Model):
	nombre=models.CharField(max_length = 100)
	edad=models.IntegerField()
	estatura=models.DecimalField(max_digits=3,decimal_places=2)
	pais=models.CharField(max_length = 100)
	equipo=models.ForeignKey(equipo, on_delete = models.CASCADE)
	imagen=models.ImageField(upload_to='foto', null=True, blank=True)

	def __str__(self):
		return self.nombre


