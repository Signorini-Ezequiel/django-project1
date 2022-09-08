from django.shortcuts import render
from django.views.generic import TemplateView #, UpdateView, DeleteView, CreateView

# Create your views here.
class InicioView(TemplateView):
    # Vista para cargar la página de inicio
    template_name = "principal/inicio.html"