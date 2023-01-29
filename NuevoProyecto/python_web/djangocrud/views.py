from django.shortcuts import render
from .models import Registros


# Create your views here.

def home(request):
    registros = Registros.objects.all()
    return render(request, 'index.html', {"Resgistros":registros})
