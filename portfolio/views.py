from django.shortcuts import render
from .models import Project

# Create your views here.

def portafolio(request):
    """Renderiza la página del portafolio."""
    projects = Project.objects.all() # pylint: disable=E1101
    return  render(request, "porfolio/portafolio.html", {'projects':projects})