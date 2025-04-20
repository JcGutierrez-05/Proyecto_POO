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
