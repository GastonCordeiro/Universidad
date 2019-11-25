from django.contrib import admin
from Universidad.Apps.GestionAcademica.models import Alumno, Curso, Matricula

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Matricula)
