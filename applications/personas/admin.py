from django.contrib import admin
from .models import Personas

#  Decoradores, hacen consultas en base a lo que pedimos (consulta de la App en el Admin)
#  Definición: clase que cumple con un fin. En este caso, un decorador vinculado, pues lo trae al admin por tenerlo en Admin

class PersonasAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombres',
        'dni',
        'telefono',
        'correo_electronico',
        'curso',
    )
    # ordering = ['-correo_electronico'] #  Ordena desde correo electrónico (con - lo hace descendente)
    ordering = ['correo_electronico']
    search_fields = ('nombres', 'correo_electronico') #  Permite la busqueda en los datos
    list_filter = ['curso',] #  Filtra la información

# Register your models here.
admin.site.register(Personas, PersonasAdmin)