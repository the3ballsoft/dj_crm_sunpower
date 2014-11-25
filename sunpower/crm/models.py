from django.db import models
from django.contrib.auth.models import User

ESTADOS_TAREAS = (
        ('REALIZADA', 'REALIZADA'),
        ('PENDIENTE', 'PENDIENTE'),
        ('APLAZADA', 'APLAZADA'),
        ('CANCELADA', 'CANCELADA'),
    )

PRIORIDAD_TAREAS = (
        ('URGENTE', 'URGENTE'),
        ('NORMAL', 'NORMAL'),
        ('OPCIONAL', 'OPCIONAL'),
    )


class TipoProducto(models.Model):
	nombre = models.CharField(max_length="250")
	def __str__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length="250")
	descripcion = models.CharField(max_length="500")
	stock = models.IntegerField(default=0);
	tipo_producto = models.ForeignKey(TipoProducto)

	def __str__(self):
		return self.nombre



class Solucion(models.Model):
	nombre = models.CharField(max_length="250")
	descripcion = models.CharField(max_length="500")
	productos = models.ManyToManyField("Producto")

	def __str__(self):
		return self.nombre

class Servicio(models.Model):
	nombre = models.CharField(max_length="250")
	descripcion = models.CharField(max_length="500")
	
	def __str__(self):
		return self.nombre

class Notificacion(models.Model):
	mensaje = models.CharField(max_length="500")
	usuario = models.ForeignKey(User)

	def __str__(self):
		return ("% - %")%(self.usaurio, self.mensaje)


class Descuento(models.Model):
	porcentaje = models.DecimalField(max_digits=19, decimal_places=6)
	servicio = models.ForeignKey(Servicio)
	solucion = models.ForeignKey(Solucion)
	producto = models.ForeignKey(Producto)

	def __str__(self):
		return self.porcentaje


class Medio(models.Model):
	nombre = models.CharField(max_length="250")

	def __str__(self):
		return self.nombre;        
    

class Cliente(models.Model):
	nombre = models.CharField(max_length="250")
	emails = models.EmailField()
	direccion =  models.CharField(max_length="250")
	telefono =  models.CharField(max_length="50")
	asesor = models.ForeignKey(User)
	medio = models.ForeignKey(Medio)

	def __str__(self):
		return self.nombre


class TipoTarea(models.Model):

	nombre = models.CharField(max_length="250")

	def __str__(self):
		return self.nombre



class Tarea(models.Model):
	titulo = models.CharField(max_length="250")
	descripcion = models.CharField(max_length="250")
	estado = models.CharField(choices=ESTADOS_TAREAS, max_length="30")
	fecha_creacion = models.DateField(auto_now_add=True)
	fecha_fin = models.DateField()
	seguimiento = models.ForeignKey('Seguimiento', related_name="TareaSeg")
	prioridad = models.CharField(choices=PRIORIDAD_TAREAS, max_length="10")

	def __str__(self):
		return self.titulo


class Seguimiento(models.Model):
	fecha_inicio = models.DateField(auto_now_add=True);
	fecha_fin = models.DateField()
	cliente = models.ForeignKey(Cliente)
	producto = models.ForeignKey(Producto)
	solucion = models.ForeignKey(Solucion)
	servicio = models.ForeignKey(Servicio)
	tareas = models.ManyToManyField('Tarea', related_name="TareaSeg")

	def __str__(self): 
		return self.fecha_inicio

