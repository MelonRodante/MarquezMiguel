import var

from cliente import Cliente
from producto import Producto
from PyQt5 import QtSql, QtWidgets, QtCore

from eventos import EventosCliente


class Conexion:

    @staticmethod
    def conectardb(filename):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)

        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer conexion.\n' 'Haz click para cancelar.',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexion establecida')
            return True


class ConexionCliente:

    @staticmethod
    def mostrarClientesTabla():
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre from clientes')
        if query.exec_():
            var.ui.tablaClientes.setRowCount(0)
            while query.next():
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                var.ui.tablaClientes.setRowCount(index + 1)
                var.ui.tablaClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                var.ui.tablaClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                index += 1
        else:
            print("Error mostrar clientes: ", query.lastError().text())

    @staticmethod
    def buscarCliente(dni):

        query = QtSql.QSqlQuery()
        query.prepare(
            'select dni, nombre, apellidos, edad, fechaalta, direccion, provincia, sexo, formaspago from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            if query.next():
                cliente = Cliente()

                cliente.dni = query.value(0)
                cliente.nombre = query.value(1)
                cliente.apellidos = query.value(2)
                cliente.edad = query.value(3)
                cliente.fechaAlta = query.value(4)
                cliente.direccion = query.value(5)
                cliente.provincia = query.value(6)
                cliente.sexo = query.value(7)
                cliente.formaspago = query.value(8)

                return cliente
            else:
                return None
        else:
            return None

    @staticmethod
    def altaCliente(cliente):

        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into clientes (dni, nombre, apellidos, edad, fechaalta, direccion, provincia, sexo, formaspago)'
            'VALUES (:dni, :nombre, :apellidos, :edad, :fechaalta, :direccion, :provincia, :sexo, :formaspago)')
        query.bindValue(':dni', cliente.dni)
        query.bindValue(':nombre', cliente.nombre)
        query.bindValue(':apellidos', cliente.apellidos)
        query.bindValue(':edad', cliente.edad)
        query.bindValue(':fechaalta', cliente.fechaAlta)
        query.bindValue(':direccion', cliente.direccion)
        query.bindValue(':provincia', cliente.provincia)
        query.bindValue(':sexo', cliente.sexo)
        query.bindValue(':formaspago', cliente.formaspago)

        if query.exec_():
            return True
        else:
            return False

    @staticmethod
    def bajaCliente(dni):

        query = QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni = :dni')
        query.bindValue(':dni', dni)

        if query.exec_():
            return True
        else:
            return False

    @staticmethod
    def modificarCliente(cliente):

        query = QtSql.QSqlQuery()
        query.prepare(
            'update clientes set nombre=:nombre, apellidos=:apellidos, edad=:edad, fechaalta=:fechaalta, direccion=:direccion, provincia=:provincia, sexo=:sexo, formaspago=:formaspago where dni = :dni')
        query.bindValue(':dni', cliente.dni)
        query.bindValue(':nombre', cliente.nombre)
        query.bindValue(':apellidos', cliente.apellidos)
        query.bindValue(':edad', cliente.edad)
        query.bindValue(':fechaalta', cliente.fechaAlta)
        query.bindValue(':direccion', cliente.direccion)
        query.bindValue(':provincia', cliente.provincia)
        query.bindValue(':sexo', cliente.sexo)
        query.bindValue(':formaspago', cliente.formaspago)

        if query.exec_():
            return True
        else:
            return False

    @staticmethod
    def altaPrueba():

        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into clientes (dni, nombre, apellidos, edad, fechaalta, direccion, provincia, sexo, formaspago)'
            'VALUES (:dni, :nombre, :apellidos, :edad, :fechaalta, :direccion, :provincia, :sexo, :formaspago)')
        query.bindValue(':dni', '00000000T')
        query.bindValue(':nombre', 'Miguel')
        query.bindValue(':apellidos', 'Marquez')
        query.bindValue(':edad', 23)
        query.bindValue(':fechaalta', '22/5/2020')
        query.bindValue(':direccion', 'Camino Lamela nº 13')
        query.bindValue(':provincia', 'Pontevedra')
        query.bindValue(':sexo', 'Hombre')
        query.bindValue(':formaspago', ',Tarjeta,')

        if query.exec_():
            print('Altaaa')
            EventosCliente.limpiarCliente()
            ConexionCliente.mostrarClientesTabla()
        else:
            print('No altaaa')


class ConexionProducto:

    @staticmethod
    def mostrarProductosTabla():
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select codigoproducto, producto, stock, precio from productos')
        if query.exec_():
            var.ui.tablaProductos.setRowCount(0)
            while query.next():
                codigoproducto = str(query.value(0))
                producto = query.value(1)
                stock = str(query.value(2))
                precio = "{:.2f}".format(query.value(3)) + " €"
                var.ui.tablaProductos.setRowCount(index + 1)
                var.ui.tablaProductos.setItem(index, 0, QtWidgets.QTableWidgetItem(codigoproducto))
                var.ui.tablaProductos.setItem(index, 1, QtWidgets.QTableWidgetItem(producto))
                var.ui.tablaProductos.setItem(index, 2, QtWidgets.QTableWidgetItem(stock))
                var.ui.tablaProductos.setItem(index, 3, QtWidgets.QTableWidgetItem(precio))
                var.ui.tablaProductos.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tablaProductos.item(index, 2).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tablaProductos.item(index, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                index += 1
        else:
            print("Error mostrar productos: ", query.lastError().text())

    @staticmethod
    def buscarProducto(producto):

        query = QtSql.QSqlQuery()
        query.prepare('select codigoproducto, producto, stock, precio from productos where producto = :producto')
        query.bindValue(':producto', producto)
        if query.exec_():
            if query.next():
                p = Producto()

                p.codigoProducto = query.value(0)
                p.producto = query.value(1)
                p.stock = query.value(2)
                p.precio = query.value(3)

                return p
            else:
                return None
        else:
            return None

    @staticmethod
    def altaProducto(producto):

        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into productos (producto, stock, precio)'
            'VALUES (:producto, :stock, :precio)')
        query.bindValue(':producto', producto.producto)
        query.bindValue(':stock', producto.stock)
        query.bindValue(':precio', producto.precio)

        if query.exec_():
            return True
        else:
            return False

    @staticmethod
    def bajaProducto(producto):

        query = QtSql.QSqlQuery()
        query.prepare('delete from productos where producto = :producto')
        query.bindValue(':producto', producto)

        if query.exec_():
            return True
        else:
            return False

    @staticmethod
    def modificarProducto(producto):

        query = QtSql.QSqlQuery()
        query.prepare('update productos set stock=:stock, precio=:precio where producto = :producto')
        query.bindValue(':producto', producto.producto)
        query.bindValue(':stock', producto.stock)
        query.bindValue(':precio', producto.precio)

        if query.exec_():
            return True
        else:
            return False