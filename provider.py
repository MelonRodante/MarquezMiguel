from PyQt5 import QtWidgets, QtCore, QtSql

import var
import ventanasDialogo


class Proveedor:

    def __init__(self):

        self.codigo = None
        self.nombre = ""
        self.telefono = ""


    def rellenarDatosProveedor(self):
        try:
            self.codigo = var.ui.editProvCodigo.text()
            self.nombre = var.ui.editProvNombre.text()
            self.telefono = var.ui.editProvTelefono.text()

        except Exception as error:
            print('Error rellenarDatosProveedor: %s' % str(error))

    def rellenarFormularioProveedor(self):
        try:
            var.ui.editProvCodigo.setText(str(self.codigo))
            var.ui.editProvNombre.setText(self.nombre)
            var.ui.editProvTelefono.setText(self.telefono)
        except Exception as error:
            print('Error rellenarFormularioProveedor: %s' % str(error))

    def datosValidos(self):
        if self.nombre == "":
            return False
        elif self.telefono == "":
            return False
        else:
            return True


class EventosProveedor:

    @staticmethod
    def conectarEventosProveedor():

        header = var.ui.tablaProveedores.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)

        var.ui.tablaProveedores.clicked.connect(EventosProveedor.cargarDatosProveedor)

        var.ui.btnProvBuscar.clicked.connect(EventosProveedor.buscarProveedor)
        var.ui.btnProvRecargar.clicked.connect(EventosProveedor.recargarProveedor)
        var.ui.btnProvLimpiar.clicked.connect(EventosProveedor.limpiarProveedor)

        var.ui.btnProvAlta.clicked.connect(EventosProveedor.altaProveedor)
        var.ui.btnProvModificar.clicked.connect(EventosProveedor.modificarProveedor)
        var.ui.btnProvBaja.clicked.connect(EventosProveedor.bajaProveedor)

        var.ui.editProvTelefono.textChanged.connect(EventosProveedor.editTelefonoChange)

        EventosProveedor.recargarProveedor()

    @staticmethod
    def editTelefonoChange():
        try:
            telefono = var.ui.editProvTelefono.text()

            numeros = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

            telefono_corregido = ''
            for l in telefono:
                if l in numeros:
                    telefono_corregido = telefono_corregido + l

            telefono1= telefono_corregido[:3]
            telefono2 = telefono_corregido[3:5]
            telefono3 = telefono_corregido[5:7]
            telefono4 = telefono_corregido[7:9]

            if telefono1:
                telefono_corregido = telefono1
                if telefono2:
                    telefono_corregido = telefono_corregido + ' ' + telefono2
                    if telefono3:
                        telefono_corregido = telefono_corregido + ' ' + telefono3
                        if telefono4:
                            telefono_corregido = telefono_corregido + ' ' + telefono4

            var.ui.editProvTelefono.setText(telefono_corregido)

        except Exception as error:
            print('Error editTelefonoChange: %s' % str(error))
            var.ui.editProvTelefono.setText('')

    @staticmethod
    def cargarTablaProveedores(proveedores):

        try:
            index = 0
            var.ui.tablaProveedores.setRowCount(len(proveedores))

            for proveedor in proveedores:
                var.ui.tablaProveedores.setItem(index, 0, QtWidgets.QTableWidgetItem(str(proveedor.codigo)))
                var.ui.tablaProveedores.setItem(index, 1, QtWidgets.QTableWidgetItem(proveedor.nombre))
                var.ui.tablaProveedores.setItem(index, 2, QtWidgets.QTableWidgetItem(proveedor.telefono))

                var.ui.tablaProveedores.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tablaProveedores.item(index, 2).setTextAlignment(QtCore.Qt.AlignCenter)

                index += 1

        except Exception as error:
            print('Error cargarTablaProveedores: %s' % str(error))

    @staticmethod
    def cargarDatosProveedor():
        try:
            fila = var.ui.tablaProveedores.selectedItems()
            proveedor = ConexionProveedor.buscarProveedorDB(nombre=fila[1].text()).pop()
            proveedor.rellenarFormularioProveedor()
        except Exception as error:
            print('Error cargarDatosProveedor: %s' % str(error))

    @staticmethod
    def limpiarProveedor():
        try:
            var.ui.editProvCodigo.setText('')
            var.ui.editProvNombre.setText('')
            var.ui.editProvTelefono.setText('')
        except Exception as error:
            print('Error limpiarProveedor: %s' % str(error))

    @staticmethod
    def recargarProveedor():
        try:
            proveedores = ConexionProveedor.buscarProveedorDB()
            EventosProveedor.cargarTablaProveedores(proveedores)
        except Exception as error:
            print('Error recargarProveedor: %s' % str(error))

    @staticmethod
    def buscarProveedor():

        try:
            nombre_proveedor = var.ui.editProvNombre.text()
            proveedores = ConexionProveedor.buscarProveedorDB(nombre=nombre_proveedor)
            EventosProveedor.cargarTablaProveedores(proveedores)
        except Exception as error:
            print('Error buscarProducto: %s' % str(error))

    @staticmethod
    def altaProveedor():
        try:
            proveedor = Proveedor()
            proveedor.rellenarDatosProveedor()

            if proveedor.datosValidos():
                if ConexionProveedor.altaProveedorDB(proveedor):
                    var.ui.statusbar.showMessage("Proveedor \'" + proveedor.nombre + "\' dado de alta.")
                    EventosProveedor.limpiarProveedor()
                    EventosProveedor.recargarProveedor()
                else:
                    ventanasDialogo.EventosVentanas.abrirDialogAviso(
                        "ERROR: Ya existe un proveedor con el nombre \'" + proveedor.nombre + "\'.")
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso("ERROR: Faltan datos")

        except Exception as error:
            print('Error altaProveedor: %s' % str(error))

    @staticmethod
    def bajaProveedor():
        try:
            codigo = var.ui.editProvCodigo.text()

            if codigo:
                if len(ConexionProveedor.buscarProveedorDB(codigo=codigo)) != 0:
                    if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro que desea dar de baja el proveedor con codigo \'' + codigo + '\'?'):
                        if ConexionProveedor.bajaProveedorDB(codigo):
                            var.ui.statusbar.showMessage('Proveedor con codigo \'' + codigo + '\' dado de baja.')
                            EventosProveedor.limpiarProveedor()
                            EventosProveedor.recargarProveedor()
                        else:
                            ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: No se ha podido dar de baja el proveedor con codigo \'' + codigo + '\'.')
                else:
                    ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: No existe ningun proveedor con el codigo \'' + codigo + '\'.')
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: Seleccione un proveedor a eliminar.')
        except Exception as error:
            print('Error bajaProveedor: %s' % str(error))

    @staticmethod
    def modificarProveedor():
        try:
            proveedor = Proveedor()
            proveedor.rellenarDatosProveedor()

            if proveedor.codigo:
                if proveedor.datosValidos():
                    if len(ConexionProveedor.buscarProveedorDB(codigo=proveedor.codigo)) != 0:
                        if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro que desea modificar los datos del proveedor con codigo \'' + proveedor.codigo + '\'?'):
                            if ConexionProveedor.modificarProveedorDB(proveedor):
                                var.ui.statusbar.showMessage('Proveedor con codigo \'' + proveedor.codigo + '\' actualizado con exito.')
                                EventosProveedor.recargarProveedor()
                            else:
                                ventanasDialogo.EventosVentanas.abrirDialogAviso(
                                    'ERROR: No se han podido modificar los datos del proveedor con codigo \'' + proveedor.codigo + '\'.')
                    else:
                        ventanasDialogo.EventosVentanas.abrirDialogAviso(
                            'ERROR: No existe ningun producto llamado \'' + proveedor.codigo + '\'.')
                else:
                    ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: Faltan datos.')
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: Seleccione un proveedor.')

        except Exception as error:
            print('Error modificarProveedor: %s' % str(error))

class ConexionProveedor:

    @staticmethod
    def buscarProveedorDB(codigo='', nombre='', orden='codigo'):

        try:
            proveedores = []
            query = QtSql.QSqlQuery()

            b_codigo = 'codigo'
            if codigo:
                b_codigo = ':codigo'

            b_nombre = 'nombre'
            if nombre:
                b_nombre = ':nombre'

            query.prepare('select codigo, nombre, telefono from proveedores where codigo = ' + b_codigo + ' and ' + ' nombre = ' + b_nombre + ' order by ' + orden)
            query.bindValue(':codigo', codigo)
            query.bindValue(':nombre', nombre)

            if query.exec_():
                while query.next():
                    p = Proveedor()

                    p.codigo = query.value(0)
                    p.nombre = query.value(1)
                    p.telefono = query.value(2)

                    proveedores.append(p)

                return proveedores
            else:
                return []

        except Exception as error:
            print('Error buscarProveedorDB: %s' % str(error))

    @staticmethod
    def altaProveedorDB(proveedor):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into proveedores (nombre, telefono)'
                          'VALUES (:nombre, :telefono)')

            query.bindValue(':nombre', proveedor.nombre)
            query.bindValue(':telefono', proveedor.telefono)

            return query.exec_()

        except Exception as error:
            print('Error altaProveedorDB: %s' % str(error))

    @staticmethod
    def bajaProveedorDB(codigo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from proveedores where codigo = :codigo')
            query.bindValue(':codigo', codigo)

            return query.exec_()

        except Exception as error:
            print('Error bajaProveedorDB: %s' % str(error))

    @staticmethod
    def modificarProveedorDB(proveedor):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update proveedores set nombre=:nombre, telefono=:telefono where codigo = :codigo')

            query.bindValue(':codigo', proveedor.codigo)
            query.bindValue(':nombre', proveedor.nombre)
            query.bindValue(':telefono', proveedor.telefono)

            return query.exec_()

        except Exception as error:
            print('Error modificarProveedorDB: %s' % str(error))