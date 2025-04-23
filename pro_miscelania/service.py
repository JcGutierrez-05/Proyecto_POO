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

class ClienteFuncionalidad:
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
    def modificar_cliente(email, nuevo_nombre=None, nuevo_telefono=None, nueva_direccion=None):
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