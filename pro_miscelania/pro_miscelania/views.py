from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Categoria
from .service import GestonCliente, GestionCategoria

# Vista para crear un cliente
def crear_cliente_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        GestonCliente.crear_cliente(nombre, email, telefono, direccion)
        return redirect('cliente_creado')

    return render(request, 'clientes/crear_cliente.html')

# Vista para editar un cliente
def editar_cliente_view(request, email):
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombre')
        nuevo_telefono = request.POST.get('telefono')
        nueva_direccion = request.POST.get('direccion')

        GestonCliente.editar_cliente(email, nuevo_nombre, nuevo_telefono, nueva_direccion)
        return HttpResponse("Cliente modificado correctamente")

    cliente = Cliente.objects.get(cliente_mail=email)
    return render(request, 'clientes/modificar_cliente.html', {'cliente': cliente})

# Vista para mostrar un cliente
def mostrar_cliente_view(request, email):
    cliente = Cliente.objects.filter(cliente_mail=email).first()
    if cliente:
        return render(request, 'clientes/mostrar_cliente.html', {'cliente': cliente})
    else:
        return HttpResponse("Cliente no encontrado", status=404)

# Vista para eliminar un cliente
def eliminar_cliente_view(request, email):
    GestonCliente.eliminar_cliente(email)
    return HttpResponse("Cliente eliminado correctamente")

# Vista para crear una categoría
def crear_categoria_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        GestionCategoria.crear_categoria(nombre)
        return redirect('categoria_creada')

    return render(request, 'categorias/crear_categoria.html')

# Vista para editar una categoría
def editar_categoria_view(request, nombre):
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nuevo_nombre')
        GestionCategoria.editar_categoria(nombre, nuevo_nombre)
        return HttpResponse("Categoría modificada correctamente")

    categoria = Categoria.objects.get(cate_nom=nombre)
    return render(request, 'categorias/modificar_categoria.html', {'categoria': categoria})

# Vista para mostrar una categoría
def mostrar_categoria_view(request, nombre):
    categoria = Categoria.objects.filter(cate_nom=nombre).first()
    if categoria:
        return render(request, 'categorias/mostrar_categoria.html', {'categoria': categoria})
    else:
        return HttpResponse("Categoría no encontrada", status=404)

# Vista para eliminar una categoría
def eliminar_categoria_view(request, nombre):
    GestionCategoria.eliminar_categoria(nombre)
    return HttpResponse("Categoría eliminada correctamente")
