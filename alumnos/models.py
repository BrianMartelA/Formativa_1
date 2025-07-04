from django.db import models
from django.contrib.auth.models import User
import datetime
from django.contrib.auth import get_user_model
from django.conf import settings
from distutils.command.upload import upload

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoria")
    nombreCategoria=models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoria")

    def __str__(self):
        return self.nombreCategoria


class cliente(models.Model):
    user = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(blank=False, null=False, max_length=20)
    confirmpassword = models.CharField(
        blank=False, null=False, max_length=20, default='ExamplePassword')
    mail = models.CharField(blank=False, null=False, max_length=20)
    confirmmail = models.CharField(
        blank=False, null=False, max_length=20, default='default@example.com')

    def __str__(self):
        return self.user


# MODELO DE REGISTRO DE CLIENTE
class Registro_cliente(models.Model):
    # RELACIÓN UNO A UNO CON USER
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    # OneToOneField: Cada usuario de Django tiene exactamente un registro de cliente
    # User: Modelo built-in de Django para autenticación
    # on_delete=models.CASCADE: Si se elimina el User, se elimina automáticamente este registro
    # default="": Valor por defecto (aunque debería ser None o no tener default)

    # REPRESENTACIÓN EN STRING
    def __str__(self):
        return self.user.username
        # Cuando se imprime este objeto, muestra el nombre de usuario
        # Ejemplo: Si user.username = "juan123", __str__ devuelve "juan123"


class BoletaModel(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    fecha_boleta = models.DateField(auto_now_add=True)
    desc_boleta = models.CharField(max_length=255)
    cant = models.DecimalField(max_digits=10, decimal_places=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    id_person = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Boleta {self.id_boleta} - {self.id_person.username} - {self.fecha_boleta}'

    def save(self, *args, **kwargs):
        self.total = self.cant * self.precio
        super(BoletaModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Boleta'
        verbose_name_plural = 'Boletas'
class Articulo(models.Model):
    codigo=models.CharField(primary_key=True, max_length=8, verbose_name="Codigo")
    marca= models.CharField(max_length=50, verbose_name="Marca")
    imagen=models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    precio=models.IntegerField(blank=True, null=True, verbose_name="Precio")
    
    def __str__(self):
        return self.codigo

class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    
    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Articulo', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)


class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    id = models.CharField(primary_key=True, max_length=7)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField()
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    def __str__(self):
        return self.nombre


class proveedores(models.Model):
    nombre = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    numero = models.IntegerField()
    fecha_contrato = models.DateField()
    def __str__(self):
        return self.nombre

class amigos(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_conocido = models.DateField()
    def __str__(self):
        return self.nombre