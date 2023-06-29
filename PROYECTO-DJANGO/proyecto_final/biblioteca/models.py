from django.db import models
from django.db import models

class Categoria(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Editorial(models.Model):
    ideditorial = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    idautor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=20)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    idlibro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    año_publicacion = models.PositiveIntegerField()
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Prestamo(models.Model):
    idprestamo = models.AutoField(primary_key=True)
    encargado = models.ForeignKey('Encargado', on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()

    def __str__(self):
        return f"Prestamo {self.idprestamo}"


class Devolucion(models.Model):
    iddevolucion = models.AutoField(primary_key=True)
    prestamo = models.OneToOneField(Prestamo, on_delete=models.CASCADE)
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Devolucion {self.iddevolucion}"


class Penalizacion(models.Model):
    idpenalizacion = models.AutoField(primary_key=True)
    estudiante = models.OneToOneField('Estudiante', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Penalizacion {self.idpenalizacion}"


class Estudiante(models.Model):
    idestudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre


class Encargado(models.Model):
    idencargado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    credenciales = models.OneToOneField('Credenciales', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Credenciales(models.Model):
    idcredenciales = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario
