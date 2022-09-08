from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        'listaralumnos/',
        views.ListAllPersonas.as_view(),
        name="listar_alumnos"
    ),
    path(
        'area/<shortname>',
        views.ListByAreaPersonas.as_view(),
        name = 'empleados_area'
    ),
    path(
        'empleados/buscar/',
        views.ListPersonasKword.as_view(),
    ),
    path(
        'success/',
        views.SuccessView.as_view(),
    ),
    path(
        'personas/habilidades/',
        views.as_view(),
    ),
    path(
        'personas/<pk>',
        views.PersonaDetailView.as_view(),
        name='empleado_detail'
    ),
]