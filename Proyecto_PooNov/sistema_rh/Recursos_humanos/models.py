

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
#Modelo de Usuario de RH
class Usuario(AbstractUser):
    cedula= models.CharField(max_length=10, blank=False, unique=True)
    nombre= models.CharField(max_length=100, blank=False)
    apellido= models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=30, unique=True, blank=False)
    telefono = models.CharField(max_length=10, blank=False, unique=True)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=False)
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido', 'telefono', 'fecha_nacimiento', 'direccion', 'cedula']

    def __str__(self):
        return f"{self.username} ({self.nombre} {self.apellido})"











class Departamento(models.Model):
   nombre = models.CharField(max_length=100,unique=True)
   descripcion = models.TextField(blank=True)

   def __str__(self):
        return self.nombre

class Cargo(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    salario_base=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.nombre



class Contrato(models.Model):
    TIPO_CHOICES = [
        ('indefinido','Indefinido'),
        ('plazo fijo','Plazo Fijo'),
        ('temporal','Temporal'),
    ]


    codigo=models.CharField(max_length=30,unique=True)
    tipo=models.CharField(max_length=30,choices=TIPO_CHOICES)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField(null=True,blank=True)
    detalles=models.TextField(blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.tipo}"


class Empleado(models.Model):
    cedula=models.CharField(max_length=10,unique=True)
    nombres=models.CharField(max_length=150)
    apellidos=models.CharField(max_length=150)
    correo=models.EmailField(unique=True)
    telefono=models.CharField(max_length=20,blank=True)
    fecha_nacimiento=models.DateField(null=True,blank=True)
    direccion=models.CharField(max_length=255,blank=True)

    #relaciones

    departamento=models.ForeignKey(Departamento,on_delete=models.PROTECT,related_name='empleados')
    cargo=models.ForeignKey(Cargo,on_delete=models.PROTECT,related_name='empleados')
    contrato=models.ForeignKey(Contrato,on_delete=models.PROTECT,related_name='empleados')

    fecha_ingreso=models.DateField(auto_now_add=False,null=True,blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f" ({self.cedula})  {self.nombres} {self.apellidos}"


class Asistencia(models.Model):
    empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE,related_name='asistencias')
    fecha=models.DateField()
    hora_entrada=models.TimeField(null=True,blank=True)
    hora_salida=models.TimeField(null=True,blank=True)
    observaciones=models.TextField(blank=True)

    class Meta:
        unique_together=('empleado','fecha')
        ordering=  ['fecha']

    def __str__(self):
        return f"Asistencia {self.empleado} - {self.fecha}"





