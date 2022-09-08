from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

class ListAllPersonas(ListView):
    model = ListAllPersonas
    template_name = "persona/list_all.html"
    paginate_by = 10
    ordering = "first_name"
    context_object_name = "lista"