import var

from cliente import Cliente
from PyQt5 import QtSql, QtWidgets

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

    '''
    @staticmethod
    def crearCli(cliente):
        query = QtSql.QSqlQuery()
        query.prepare('insert into clientes (dni, apellidos, nombre, fechaalta, direccion, provincia, sexo, formaspago, edad)'
                      'VALUES (:dni, :apellidos, :nombre, :fechaalta, :direccion, :provincia, :sexo, :formaspago, :edad)')
        query.bindValue(':dni',         str(cliente[0]))
        query.bindValue(':apellidos',   str(cliente[1]))
        query.bindValue(':nombre',      str(cliente[2]))
        query.bindValue(':fechaalta',   str(cliente[3]))
        query.bindValue(':direccion',   str(cliente[4]))
        query.bindValue(':provincia',   str(cliente[5]))
        query.bindValue(':sexo',        str(cliente[6]))
        query.bindValue(':formaspago',  str(cliente[7]))
        query.bindValue(':edad', cliente[8])

        if query.exec_():
            Conexion.mostrarClientesTabla()
            Clients.limpiarCliente()
            var.ui.statusbar.showMessage('Cliente con DNI ' + var.ui.editDNI.text() + ' dado de alta')

        else:
            dialog = main.DialogAviso('Error: Ya existe un cliente con el ese DNI')
            dialog.show()
            dialog.exec_()

    @staticmethod
    def bajaCli():

        dni = var.ui.editDNI.text()

        query = QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni = :dni')
        query.bindValue(':dni', dni)


        if query.exec_():
            var.ui.statusbar.showMessage('Cliente con DNI ' + dni + ' dado de baja')
            Conexion.mostrarClientesTabla()
            Clients.limpiarCliente()
        else:
            events.Eventos.DialoAviso('Error: No existe ningun empleado con ese DNI')

    @staticmethod
    def modificarCli(newdata):

        query = QtSql.QSqlQuery()
        query.prepare('update clientes set apellidos=:apellidos, nombre=:nombre, fechaalta=:fechaalta, direccion=:direccion, provincia=:provincia, sexo=:sexo, formaspago=:formaspago, edad=:edad where dni = :dni')
        query.bindValue(':dni',         str(newdata[0]))
        query.bindValue(':apellidos',   str(newdata[1]))
        query.bindValue(':nombre',      str(newdata[2]))
        query.bindValue(':fechaalta',    str(newdata[3]))
        query.bindValue(':direccion',   str(newdata[4]))
        query.bindValue(':provincia',   str(newdata[5]))
        query.bindValue(':sexo',        str(newdata[6]))
        query.bindValue(':formaspago',  str(newdata[7]))
        query.bindValue(':edad', newdata[8])

        if query.exec_() and Conexion.cargarDatosCliente(str(newdata[0])):
            Conexion.mostrarClientesTabla()
            Clients.limpiarCliente()
            var.ui.statusbar.showMessage('Datos del cliente con DNI ' + newdata[0] + ' modificados')
        else:
            events.Eventos.DialoAviso('Error: No existe ningun empleado con ese DNI')

    @staticmethod
    def buscarCli(dni):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre from clientes where dni = :dni')
        query.bindValue(':dni', dni)
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
    '''

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
    def cargarDatosCliente(dni):

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
    def clienteExiste(dni):
        query = QtSql.QSqlQuery()
        query.prepare('select dni from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            if query.next():
                return True
            else:
                return False
        else:
            return False

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
            return  False

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
        query.prepare('update clientes set nombre=:nombre, apellidos=:apellidos, edad=:edad, fechaalta=:fechaalta, direccion=:direccion, provincia=:provincia, sexo=:sexo, formaspago=:formaspago where dni = :dni')
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