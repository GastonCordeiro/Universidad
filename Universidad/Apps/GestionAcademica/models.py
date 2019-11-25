from django.db import models

# Create your models here.

class Alumno(models.Model):
    Apellido = models.CharField(max_length=35)
    Nombre = models.CharField(max_length=35)
    DNI = models.CharField(max_length=10)
    FechaNacimiento = models.DateField()
    GENERO = (('F', 'Femenino'), ('M', 'Masculino'), ('N','NoContesta'))
    Genero=models.CharField(max_length=1, choices=GENERO, default='F')

    def NombreCompleto(self):
        cadena= "{0} {1}"
        return cadena.format(self.Apellido,self.Nombre)
    
    def __str__(self):
        return self.NombreCompleto()


class Curso(models.Model):
    Nombre =models.CharField(max_length=50)
    Creditos=models.PositiveSmallIntegerField()
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.Nombre, self.Creditos)

class Matricula(models.Model):
    Alumno=models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
    Curso=models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    FechaMatricula =models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Alumno, self.Curso)