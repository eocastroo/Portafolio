from django.shortcuts import render

# Create your views here.

def about(request):
    """Renderiza la página de contacto."""
    return render(request, "core/about.html")

def contact(request):
    """Renderiza la página de contacto."""
    return render(request, "core/contact.html")

