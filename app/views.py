from app.models import Sistema, Smartphone
from django.shortcuts import redirect, render

# Create your views here.

#Renderizar el HTML

def index(request):
    smartphones = Smartphone.objects.all()
    sistemas = Sistema.objects.all()

    contexto = { 'smartphones': smartphones, 'sistemas': sistemas }

    return render(request, 'index.html', contexto)

def agregar(request):
    modelo = request.POST.get('modelo', '')
    id_sistema = request.POST.get('sistema', '')

    sistema = Sistema.objects.get(id = id_sistema)

    smartphone = Smartphone(modelo = modelo, sistema = sistema)
    smartphone.save()

    return redirect('index')

def editar(request, id):
    modelo = request.POST.get('modelo', '')
    id_sistema = request.POST.get('sistema', '') # Para obtener el valor mediante el name

    sistema = Sistema.objects.get(id = id_sistema)

    smartphone = Smartphone.objects.get(id=id) # Para obtener el objeto mediante la id

    smartphone.modelo = modelo       
    smartphone.sistema = sistema    # Para sobrescribir

    smartphone.save()

    return redirect('index') 

def eliminar(request, id):
    smartphone = Smartphone.objects.get(id=id)
    smartphone.delete() 

    return redirect('index')