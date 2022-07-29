from django.shortcuts import render
from django.http import HttpRequest
from Mobiliario.forms import FormularioMobiliario
from Mobiliario.models import Mobiliario

# Create your views here.

class FormularioView(HttpRequest):

    def inicio(request):
        obj = FormularioMobiliario()
        return render(request,"MobiliarioIndex.html",{"form":obj})
    
    def validacion(request):
        obj = FormularioMobiliario(request.POST)
        if obj.is_valid():
            obj.save()
            obj = FormularioMobiliario()
        return render(request, "MobiliarioIndex.html",{"form": obj , "msj": 'ok'})

    def leer(request):
        obj = Mobiliario.objects.all()
        return render(request,"Lista.html",{"lista":obj} )