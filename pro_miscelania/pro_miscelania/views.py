from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente
from .service import ClienteFuncionalidad 

def crear_cliente_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        ClienteFuncionalidad.crear_cliente(nombre, email, telefono, direccion)
        return redirect('cliente_creado')

    return render(request, 'clientes/crear_cliente.html')

def modificar_cliente_view(request, email):
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombre')
        nuevo_telefono = request.POST.get('telefono')
        nueva_direccion = request.POST.get('direccion')
        
        ClienteFuncionalidad.modificar_cliente(email, nuevo_nombre, nuevo_telefono, nueva_direccion)
        return HttpResponse("Cliente modificado correctamente")

    cliente = Cliente.objects.get(cliente_mail=email)
    return render(request, 'clientes/modificar_cliente.html', {'cliente': cliente})

def mostrar_cliente_view(request, email):
    cliente = Cliente.objects.filter(cliente_mail=email).first()
    if cliente:
        return render(request, 'clientes/mostrar_cliente.html', {'cliente': cliente})
    else:
        return HttpResponse("Cliente no encontrado", status=404)

def eliminar_cliente_view(request, email):
    ClienteFuncionalidad.eliminar_cliente(email)
    return HttpResponse(f"Cliente {email} eliminado (si existía)")

