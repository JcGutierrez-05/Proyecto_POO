from pro_miscelania.models import Categoria
from pro_miscelania.models import Ciudad
from pro_miscelania.models import Cliente
from pro_miscelania.models import Compra
from pro_miscelania.models import Envios
from pro_miscelania.models import FacturaCompraProducto
from pro_miscelania.models import FacturaProducto
from pro_miscelania.models import FacturaVenta
from pro_miscelania.models import Producto
from pro_miscelania.models import Proveedor

class GestonCliente:
    @staticmethod
    def crear_cliente(nombre, email, telefono, direccion):
        if Cliente.objects.filter(cliente_mail=email).exists():
            print("Error: El correo ya está registrado")
        else:
            cliente = Cliente.objects.create(
                cliente_nom=nombre,
                cliente_mail=email,
                cliente_tel=telefono,
                cliente_direc=direccion
            )
            cliente.save()
            print(f"Usuario {nombre} fue creado exitosamente")
    
    @staticmethod
    def editar_cliente(email, nuevo_nombre=None, nuevo_telefono=None, nueva_direccion=None):
        try:
            cliente = Cliente.objects.get(cliente_mail=email)
            if nuevo_nombre:
                cliente.cliente_nom = nuevo_nombre
            if nuevo_telefono:
                cliente.cliente_tel = nuevo_telefono
            if nueva_direccion:
                cliente.cliente_direc = nueva_direccion
            cliente.save()
            print(f"Usuario {email} ha sido modificado correctamente")
        except Cliente.DoesNotExist:
            print("Error: No se encontró un cliente con ese correo")

    @staticmethod
    def mostrar_cliente(email):
        try:
            cliente = Cliente.objects.get(cliente_mail=email)
            print(f"Nombre: {cliente.cliente_nom}, Email: {cliente.cliente_mail}, Teléfono: {cliente.cliente_tel}, Dirección: {cliente.cliente_direc}")
        except Cliente.DoesNotExist:
            print("Error: No se encontró un cliente con ese correo")

    @staticmethod
    def eliminar_cliente(email):
        try:
            cliente = Cliente.objects.get(cliente_mail=email)
            cliente.delete()
            print(f"Usuario {email} ha sido eliminado correctamente")
        except Cliente.DoesNotExist:
            print("Error: No se encontró un cliente con ese correo")

class GestorCiudad:
    pass

class GestionCategoria:
    @staticmethod
    def crear_categoria(nombre):
        if Categoria.objects.filter(cate_nom=nombre).exists():
            print("Error: la categoria ya esta registrada")
        else:
            categoria = Categoria.objects.create(
                cate_nom=nombre,
            )
            categoria.save()
            print(f"la categoria {nombre} fue registrada exitosamente ")
     
     
    def editar_categoria(nombre,nuevo_nombre=None):
        try:
            categoria = Categoria.objects.get(cate_nom=nombre)
            if nuevo_nombre:
                Categoria.cate_nom = nuevo_nombre
            categoria.save()
            print(f"La categoria {nombre} ha sido modificado correctamente")
        except Categoria.DoesNotExist:
            print("Error: No se encontró una categoria")

  
    def mostrar_cliente(nombre):
        try:
            categoria = Categoria.objects.get(cate_nom=nombre)
            print(f"Nombre: {categoria.cate_nom}")
        except Cliente.DoesNotExist:
            print("Error: No se encontró una categoria")

   
    def eliminar_categoria(nombre):
        try:
            categoria = Categoria.objects.get(cate_nom=nombre)
            categoria.delete()
            print(f"la categoria: {nombre} ha sido eliminada correctamente")
        except Cliente.DoesNotExist:
            print("Error: No se encontró una categoria")

