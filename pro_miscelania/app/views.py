from django.shortcuts import render
from .models import  Cliente,Producto,FacturaVenta,Ciudad
from .service import GestorCliente, GestorCiudad, GestionCategoria, GestionCompra, GestorProducto, GestorProveedor, GestorFacturaVenta, GestorFacturaProducto, EnvioService
from django.http import JsonResponse

# -----------------------------------------
# Vistas de Cliente
def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        GestorCliente.crear_cliente(nombre, email, telefono, direccion)
        return JsonResponse({'message': 'Cliente creado correctamente'})

def editar_cliente(request, email):
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombre')
        nuevo_telefono = request.POST.get('telefono')
        nueva_direccion = request.POST.get('direccion')
        GestorCliente.editar_cliente(email, nuevo_nombre, nuevo_telefono, nueva_direccion)
        return JsonResponse({'message': 'Cliente modificado correctamente'})

def mostrar_cliente(request, email):
    if request.method == 'GET':
        cliente = GestorCliente.mostrar_cliente(email)
        return JsonResponse({'cliente': cliente, 'message': 'Cliente mostrado correctamente'})

def eliminar_cliente(request, email):
    if request.method == 'POST':
        GestorCliente.eliminar_cliente(email)
        return JsonResponse({'message': 'Cliente eliminado correctamente'})

# -----------------------------------------
# Vistas de Ciudad
def crear_ciudad(request):
    if request.method == 'POST':
        nombre_ciudad = request.POST.get('nombre_ciudad')
        GestorCiudad.crear_ciudad(nombre_ciudad)
        return JsonResponse({'message': 'Ciudad creada correctamente'})

def editar_ciudad(request, nombre_ciudad):
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nuevo_nombre')
        GestorCiudad.editar_ciudad(nombre_ciudad, nuevo_nombre)
        return JsonResponse({'message': 'Ciudad modificada correctamente'})

def mostrar_ciudad(request, nombre_ciudad):
    if request.method == 'GET':
        ciudad = GestorCiudad.mostrar_ciudad(nombre_ciudad)
        return JsonResponse({'ciudad': ciudad, 'message': 'Ciudad mostrada correctamente'})

def eliminar_ciudad(request, nombre_ciudad):
    if request.method == 'POST':
        GestorCiudad.eliminar_ciudad(nombre_ciudad)
        return JsonResponse({'message': 'Ciudad eliminada correctamente'})

# -----------------------------------------
# Vistas de Categoria
def crear_categoria(request):
    if request.method == 'POST':
        nombre_categoria = request.POST.get('nombre')
        GestionCategoria.crear_categoria(nombre_categoria)
        return JsonResponse({'message': 'Categoría creada correctamente'})

def editar_categoria(request, nombre_categoria):
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nuevo_nombre')
        GestionCategoria.editar_categoria(nombre_categoria, nuevo_nombre)
        return JsonResponse({'message': 'Categoría modificada correctamente'})

def mostrar_categoria(request, nombre_categoria):
    if request.method == 'GET':
        categoria = GestionCategoria.mostrar_categoria(nombre_categoria)
        return JsonResponse({'categoria': categoria, 'message': 'Categoría mostrada correctamente'})

def eliminar_categoria(request, nombre_categoria):
    if request.method == 'POST':
        GestionCategoria.eliminar_categoria(nombre_categoria)
        return JsonResponse({'message': 'Categoría eliminada correctamente'})

# -----------------------------------------
# Vistas de Compra
def crear_compra(request):
    if request.method == 'POST':
        fecha_compra = request.POST.get('fecha')
        GestionCompra.crear_fecha_compra(fecha_compra)
        return JsonResponse({'message': 'Compra creada correctamente'})

def editar_compra(request, fecha_compra):
    if request.method == 'POST':
        nueva_fecha = request.POST.get('nueva_fecha')
        GestionCompra.editar_fecha_compra(fecha_compra, nueva_fecha)
        return JsonResponse({'message': 'Compra modificada correctamente'})

def mostrar_compra(request, fecha_compra):
    if request.method == 'GET':
        compra = GestionCompra.mostrar_fecha_compra(fecha_compra)
        return JsonResponse({'compra': compra, 'message': 'Compra mostrada correctamente'})

def eliminar_compra(request, fecha_compra):
    if request.method == 'POST':
        GestionCompra.eliminar_fecha_compra(fecha_compra)
        return JsonResponse({'message': 'Compra eliminada correctamente'})

# -----------------------------------------
# Vistas de Producto
def crear_producto(request):
    if request.method == 'POST':
        nombre_producto = request.POST.get('nombre')
        precio_producto = request.POST.get('precio')
        GestorProducto.crear_producto(nombre_producto, precio_producto)
        return JsonResponse({'message': 'Producto creado correctamente'})

def editar_producto(request, nombre_producto):
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nuevo_nombre')
        nuevo_precio = request.POST.get('nuevo_precio')
        GestorProducto.editar_producto(nombre_producto, nuevo_nombre, nuevo_precio)
        return JsonResponse({'message': 'Producto modificado correctamente'})

def mostrar_producto(request, nombre_producto):
    if request.method == 'GET':
        producto = GestorProducto.mostrar_producto(nombre_producto)
        return JsonResponse({'producto': producto, 'message': 'Producto mostrado correctamente'})

def eliminar_producto(request, nombre_producto):
    if request.method == 'POST':
        GestorProducto.eliminar_producto(nombre_producto)
        return JsonResponse({'message': 'Producto eliminado correctamente'})

# -----------------------------------------
# Vistas de Proveedor
def crear_proveedor(request):
    if request.method == 'POST':
        nombre_proveedor = request.POST.get('nombre')
        email_proveedor = request.POST.get('email')
        telefono_proveedor = request.POST.get('telefono')
        direccion_proveedor = request.POST.get('direccion')
        GestorProveedor.crear_proveedor(nombre_proveedor, email_proveedor, telefono_proveedor, direccion_proveedor)
        return JsonResponse({'message': 'Proveedor creado correctamente'})

def editar_proveedor(request, email_proveedor):
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nuevo_nombre')
        nuevo_telefono = request.POST.get('nuevo_telefono')
        nueva_direccion = request.POST.get('nueva_direccion')
        GestorProveedor.editar_proveedor(email_proveedor, nuevo_nombre, nuevo_telefono, nueva_direccion)
        return JsonResponse({'message': 'Proveedor modificado correctamente'})

def mostrar_proveedor(request, email_proveedor):
    if request.method == 'GET':
        proveedor = GestorProveedor.mostrar_proveedor(email_proveedor)
        return JsonResponse({'proveedor': proveedor, 'message': 'Proveedor mostrado correctamente'})

def eliminar_proveedor(request, email_proveedor):
    if request.method == 'POST':
        GestorProveedor.eliminar_proveedor(email_proveedor)
        return JsonResponse({'message': 'Proveedor eliminado correctamente'})

# -----------------------------------------
# Vistas de FacturaVenta
def crear_factura_venta(request):
    if request.method == 'POST':
        fecha_venta = request.POST.get('fecha_venta')
        cliente = Cliente.objects.get(cliente_mail=request.POST.get('cliente'))
        GestorFacturaVenta.crear_factura_venta(fecha_venta, cliente)
        return JsonResponse({'message': 'Factura de venta creada correctamente'})

def mostrar_factura_venta(request, id_factura):
    if request.method == 'GET':
        factura_venta = GestorFacturaVenta.mostrar_factura_venta(id_factura)
        return JsonResponse({'factura_venta': factura_venta, 'message': 'Factura de venta mostrada correctamente'})

# -----------------------------------------
# Vistas de FacturaProducto
def crear_factura_producto(request):
    if request.method == 'POST':
        producto = Producto.objects.get(producto_nom=request.POST.get('producto'))
        cantidad = request.POST.get('cantidad')
        GestorFacturaProducto.crear_factura_producto(producto, cantidad)
        return JsonResponse({'message': 'Factura producto creada correctamente'})

def mostrar_factura_producto(request, id_factura_producto):
    if request.method == 'GET':
        factura_producto = GestorFacturaProducto.mostrar_factura_producto(id_factura_producto)
        return JsonResponse({'factura_producto': factura_producto, 'message': 'Factura producto mostrada correctamente'})

# -----------------------------------------
# Vistas de Envios
def crear_envio(request):
    if request.method == 'POST':
        fecha_envio = request.POST.get('fecha_envio')
        factura = FacturaVenta.objects.get(id=request.POST.get('factura'))
        cliente = Cliente.objects.get(cliente_mail=request.POST.get('cliente'))
        ciudad = Ciudad.objects.get(ciud_nom=request.POST.get('ciudad'))
        EnvioService.crear_envio(fecha_envio, factura, cliente, ciudad)
        return JsonResponse({'message': 'Envío creado correctamente'})

def mostrar_envio(request, id_envio):
    if request.method == 'GET':
        envio = EnvioService.mostrar_envio(id_envio)
        return JsonResponse({'envio': envio, 'message': 'Envío mostrado correctamente'})

def actualizar_estado_envio(request, id_envio):
    if request.method == 'POST':
        nuevo_estado = request.POST.get('nuevo_estado')
        EnvioService.actualizar_estado_envio(id_envio, nuevo_estado)
        return JsonResponse({'message': 'Estado del envío actualizado correctamente'})

def eliminar_envio(request, id_envio):
    if request.method == 'POST':
        EnvioService.eliminar_envio(id_envio)
        return JsonResponse({'message': 'Envío eliminado correctamente'})
