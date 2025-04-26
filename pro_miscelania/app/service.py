from .models import Categoria
from .models import Ciudad
from .models import Cliente
from .models import Compra
from .models import Producto
from .models import Proveedor
from .models import FacturaVenta
from .models import FacturaProducto
from .models import FacturaCompraProducto
from .models import Envios

# -----------------------------------------
class GestorCliente:
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

# -----------------------------------------
class GestorCiudad:
    @staticmethod
    def crear_ciudad(nombre_ciudad):
        if Ciudad.objects.filter(ciud_nom=nombre_ciudad).exists():
            print("Error: La ciudad ya está registrada")
        else:
            ciudad = Ciudad.objects.create(
                ciud_nom=nombre_ciudad,
            )
            ciudad.save()
            print(f"La ciudad {nombre_ciudad} fue registrada exitosamente")

    @staticmethod
    def editar_ciudad(nombre_ciudad, nuevo_nombre=None):
        try:
            ciudad = Ciudad.objects.get(ciud_nom=nombre_ciudad)
            if nuevo_nombre:
                ciudad.ciud_nom = nuevo_nombre
            ciudad.save()
            print(f"La ciudad {nombre_ciudad} ha sido modificada correctamente")
        except Ciudad.DoesNotExist:
            print("Error: No se encontró una ciudad con ese nombre")

    @staticmethod
    def mostrar_ciudad(nombre_ciudad):
        try:
            ciudad = Ciudad.objects.get(ciud_nom=nombre_ciudad)
            print(f"Nombre: {ciudad.ciud_nom}")
        except Ciudad.DoesNotExist:
            print("Error: No se encontró una ciudad")

    @staticmethod
    def eliminar_ciudad(nombre_ciudad):
        try:
            ciudad = Ciudad.objects.get(ciud_nom=nombre_ciudad)
            ciudad.delete()
            print(f"La ciudad {nombre_ciudad} ha sido eliminada correctamente")
        except Ciudad.DoesNotExist:
            print("Error: No se encontró una ciudad")

# -----------------------------------------
class GestionCategoria:
    @staticmethod
    def crear_categoria(nombre):
        if Categoria.objects.filter(cate_nom=nombre).exists():
            print("Error: La categoría ya está registrada")
        else:
            categoria = Categoria.objects.create(
                cate_nom=nombre,
            )
            categoria.save()
            print(f"La categoría {nombre} fue registrada exitosamente")

    @staticmethod
    def editar_categoria(nombre, nuevo_nombre=None):
        try:
            categoria = Categoria.objects.get(cate_nom=nombre)
            if nuevo_nombre:
                categoria.cate_nom = nuevo_nombre
            categoria.save()
            print(f"La categoría {nombre} ha sido modificada correctamente")
        except Categoria.DoesNotExist:
            print("Error: No se encontró una categoría")

    @staticmethod
    def mostrar_categoria(nombre):
        try:
            categoria = Categoria.objects.get(cate_nom=nombre)
            print(f"Nombre: {categoria.cate_nom}")
        except Categoria.DoesNotExist:
            print("Error: No se encontró una categoría")

    @staticmethod
    def eliminar_categoria(nombre):
        try:
            categoria = Categoria.objects.get(cate_nom=nombre)
            categoria.delete()
            print(f"La categoría {nombre} ha sido eliminada correctamente")
        except Categoria.DoesNotExist:
            print("Error: No se encontró una categoría")

# -----------------------------------------
class GestionCompra:
    @staticmethod
    def crear_fecha_compra(fecha_compra):
        if Compra.objects.filter(compra_fecha=fecha_compra).exists():
            print("Error: La fecha ya está registrada")
        else:
            compra = Compra.objects.create(
                compra_fecha=fecha_compra,
            )
            compra.save()
            print(f"La fecha {fecha_compra} fue registrada exitosamente")

    @staticmethod
    def editar_fecha_compra(fecha_compra, nueva_fecha=None):
        try:
            compra = Compra.objects.get(compra_fecha=fecha_compra)
            if nueva_fecha:
                compra.compra_fecha = nueva_fecha
            compra.save()
            print(f"La fecha {fecha_compra} ha sido modificada correctamente")
        except Compra.DoesNotExist:
            print("Error: No se encontró una fecha")

    @staticmethod
    def mostrar_fecha_compra(fecha_compra):
        try:
            compra = Compra.objects.get(compra_fecha=fecha_compra)
            print(f"Fecha: {compra.compra_fecha}")
        except Compra.DoesNotExist:
            print("Error: No se encontró una fecha")

    @staticmethod
    def eliminar_fecha_compra(fecha_compra):
        try:
            compra = Compra.objects.get(compra_fecha=fecha_compra)
            compra.delete()
            print(f"La fecha {fecha_compra} ha sido eliminada correctamente")
        except Compra.DoesNotExist:
            print("Error: No se encontró una fecha")

# -----------------------------------------
class GestorProducto:
    @staticmethod
    def crear_producto(nombre_producto, precio_producto):
        if Producto.objects.filter(producto_nom=nombre_producto).exists():
            print("Error: El producto ya está registrado")
        else:
            producto = Producto.objects.create(
                producto_nom=nombre_producto,
                producto_precio=precio_producto,
            )
            producto.save()
            print(f"Producto {nombre_producto} fue creado exitosamente")

    @staticmethod
    def editar_producto(nombre_producto, nuevo_nombre_producto=None, nuevo_precio_producto=None):
        try:
            producto = Producto.objects.get(producto_nom=nombre_producto)
            if nuevo_nombre_producto:
                producto.producto_nom = nuevo_nombre_producto
            if nuevo_precio_producto:
                producto.producto_precio = nuevo_precio_producto
            producto.save()
            print(f"Producto {nombre_producto} ha sido modificado correctamente")
        except Producto.DoesNotExist:
            print("Error: No se encontró un producto")

    @staticmethod
    def mostrar_producto(nombre_producto):
        try:
            producto = Producto.objects.get(producto_nom=nombre_producto)
            print(f"Nombre: {producto.producto_nom}, Precio: {producto.producto_precio}")
        except Producto.DoesNotExist:
            print("Error: No se encontró un producto")

    @staticmethod
    def eliminar_producto(nombre_producto):
        try:
            producto = Producto.objects.get(producto_nom=nombre_producto)
            producto.delete()
            print(f"Producto {nombre_producto} ha sido eliminado correctamente")
        except Producto.DoesNotExist:
            print("Error: No se encontró un producto")

# -----------------------------------------
class GestorProveedor:
    @staticmethod
    def crear_proveedor(nombre_proveedor, email_proveedor, telefono_proveedor, direccion_proveedor):
        if Proveedor.objects.filter(prove_mail=email_proveedor).exists():
            print("Error: El correo ya está registrado")
        else:
            proveedor = Proveedor.objects.create(
                prove_nom=nombre_proveedor,
                prove_mail=email_proveedor,
                prove_tel=telefono_proveedor,
                prove_direc=direccion_proveedor
            )
            proveedor.save()
            print(f"Proveedor {nombre_proveedor} fue creado exitosamente")

    @staticmethod
    def editar_proveedor(email_proveedor, nuevo_nombre_proveedor=None, nuevo_telefono_proveedor=None, nueva_direccion_proveedor=None):
        try:
            proveedor = Proveedor.objects.get(prove_mail=email_proveedor)
            if nuevo_nombre_proveedor:
                proveedor.prove_nom = nuevo_nombre_proveedor
            if nuevo_telefono_proveedor:
                proveedor.prove_tel = nuevo_telefono_proveedor
            if nueva_direccion_proveedor:
                proveedor.prove_direc = nueva_direccion_proveedor
            proveedor.save()
            print(f"Proveedor {email_proveedor} ha sido modificado correctamente")
        except Proveedor.DoesNotExist:
            print("Error: No se encontró un proveedor")

    @staticmethod
    def mostrar_proveedor(email_proveedor):
        try:
            proveedor = Proveedor.objects.get(prove_mail=email_proveedor)
            print(f"Nombre: {proveedor.prove_nom}, Email: {proveedor.prove_mail}, Teléfono: {proveedor.prove_tel}, Dirección: {proveedor.prove_direc}")
        except Proveedor.DoesNotExist:
            print("Error: No se encontró un proveedor")

    @staticmethod
    def eliminar_proveedor(email_proveedor):
        try:
            proveedor = Proveedor.objects.get(prove_mail=email_proveedor)
            proveedor.delete()
            print(f"Proveedor {email_proveedor} ha sido eliminado correctamente")
        except Proveedor.DoesNotExist:
            print("Error: No se encontró un proveedor")

# -----------------------------------------
class GestorFacturaVenta:
    @staticmethod
    def crear_factura_venta(fecha_venta, cliente):
        factura = FacturaVenta.objects.create(
            factura_fecha=fecha_venta,
            cliente=cliente
        )
        factura.save()
        print(f"Factura de venta registrada para el cliente {cliente}")

    @staticmethod
    def mostrar_factura_venta(id_factura):
        try:
            factura = FacturaVenta.objects.get(id=id_factura)
            print(f"Factura ID: {factura.id}, Fecha: {factura.factura_fecha}, Cliente: {factura.cliente}")
        except FacturaVenta.DoesNotExist:
            print("Error: No se encontró la factura de venta")

# -----------------------------------------
class GestorFacturaProducto:
    @staticmethod
    def crear_factura_producto(producto, cantidad):
        factura_producto = FacturaProducto.objects.create(
            producto=producto,
            cantidad=cantidad
        )
        factura_producto.save()
        print(f"Factura producto registrada para el producto {producto}")

    @staticmethod
    def mostrar_factura_producto(id_factura_producto):
        try:
            factura_producto = FacturaProducto.objects.get(id=id_factura_producto)
            print(f"FacturaProducto ID: {factura_producto.id}, Producto: {factura_producto.producto}, Cantidad: {factura_producto.cantidad}")
        except FacturaProducto.DoesNotExist:
            print("Error: No se encontró la factura producto")

# -----------------------------------------
class EnvioService:
    @staticmethod
    def crear_envio(fecha_envio, factura, cliente, ciudad):
        if Envios.objects.filter(envi_fecha=fecha_envio, factura=factura, cliente=cliente, ciud=ciudad).exists():
            print("Error: El envío ya está registrado con estos parámetros")
        else:
            envio = Envios.objects.create(
                envi_fecha=fecha_envio,
                factura=factura,
                cliente=cliente,
                ciud=ciudad
            )
            envio.save()
            print(f'Envío creado: {envio.envi_id}')

    @staticmethod
    def mostrar_envio(id_envio):
        try:
            envio = Envios.objects.get(envi_id=id_envio)
            print(f'Envio ID: {envio.envi_id}, Fecha Envío: {envio.envi_fecha}, Factura ID: {envio.factura}, Cliente: {envio.cliente}, Ciudad: {envio.ciud}')
        except Envios.DoesNotExist:
            print('Error: No se encontró el envío')

    @staticmethod
    def actualizar_estado_envio(id_envio, nuevo_estado):
        try:
            envio = Envios.objects.get(envi_id=id_envio)
            envio.estado = nuevo_estado
            envio.save()
            print(f'Estado actualizado para envío: {id_envio}')
        except Envios.DoesNotExist:
            print('Error: No se encontró el envío')

    @staticmethod
    def eliminar_envio(id_envio):
        try:
            envio = Envios.objects.get(envi_id=id_envio)
            envio.delete()
            print(f'Envío eliminado: {id_envio}')
        except Envios.DoesNotExist:
            print('Error: No se encontró el envío')
