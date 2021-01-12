from PyQt5 import QtWidgets, QtCore

import var
import ventanas
import conexion
from cliente import Cliente
from producto import Producto


class EventosVentanas:

    @staticmethod
    def abrirDialogCalendario():
        try:
            dlgCalendar = ventanas.DialogCalendario()
            dlgCalendar.exec_()
        except Exception as error:
            print('Error: %s ' % str(error))

    @staticmethod
    def abrirDialogSalir():
        try:
            dialog = ventanas.DialogSalir()
            dialog.show()
            dialog.exec_()
        except Exception as error:
            print('El error es %s' % str(error))

    @staticmethod
    def abrirDialogAviso(msg):
        try:
            var.ui.statusbar.showMessage(msg)

            dialog = ventanas.DialogAviso(msg)
            dialog.show()
            dialog.setFixedSize(dialog.size())
            dialog.exec_()
        except Exception as error:
            print('El error es %s' % str(error))


class EventosCliente:

    @staticmethod
    def cargarProvincias():
        try:
            for i in var.prov:
                var.ui.cmbProvincia.addItem(i)
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def DNIValido():
        try:
            dni = var.ui.editDNI.text()
            if dni != '':
                if Cliente.comprobarDNI():
                    var.ui.lblValido.setStyleSheet('QLabel {color: green}')
                    var.ui.lblValido.setText('V')
                    var.ui.editDNI.setText(dni.upper())
                else:
                    var.ui.lblValido.setStyleSheet('QLabel {color: red}')
                    var.ui.lblValido.setText('X')
                    var.ui.editDNI.setText(dni.upper())
            else:
                var.ui.lblValido.setText('')
        except Exception as error:
            print('Error: %s ' % str(error))

    @staticmethod
    def cargarDatosCliente():
        try:
            fila = var.ui.tablaClientes.selectedItems()
            cliente = conexion.ConexionCliente.buscarCliente(fila[0].text())

            if cliente:
                cliente.rellenarFormularioCliente()
            else:
                EventosVentanas.abrirDialogAviso("ERROR: No se han podido cargar los datos")

        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def buscarCliente():
        try:
            cliente = conexion.ConexionCliente.buscarCliente(var.ui.editDNI.text())

            if cliente is not None:
                index = 0
                var.ui.tablaClientes.setRowCount(0)
                var.ui.tablaClientes.setRowCount(index + 1)
                var.ui.tablaClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(cliente.dni))
                var.ui.tablaClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(cliente.apellidos))
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(cliente.nombre))
                index += 1


        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def limpiarCliente():
        try:
            var.ui.lblValido.setText('')

            var.ui.editDNI.setText('')
            var.ui.editNombre.setText('')
            var.ui.editApellidos.setText('')

            var.ui.spinEdad.setValue(18)
            var.ui.editFechaAlta.setText('')

            var.ui.editDireccion.setText('')
            var.ui.cmbProvincia.setCurrentIndex(0)

            var.ui.grpSexo.setExclusive(False)
            var.ui.rbtMasculino.setChecked(False)
            var.ui.rbtFemenino.setChecked(False)
            var.ui.grpSexo.setExclusive(True)

            var.ui.chkTransferencia.setChecked(False)
            var.ui.chkTarjeta.setChecked(False)
            var.ui.chkEfectivo.setChecked(False)


        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def altaCliente():
        try:
            cliente = Cliente()
            cliente.rellenarDatosCliente()

            if cliente.comprobarDNI():
                if cliente.datosValidos():
                    if conexion.ConexionCliente.altaCliente(cliente):
                        var.ui.statusbar.showMessage('Cliente con DNI \'' + cliente.dni + "\' dado de alta.")
                        EventosCliente.limpiarCliente()
                        conexion.ConexionCliente.mostrarClientesTabla()
                    else:
                        EventosVentanas.abrirDialogAviso('ERROR: Ya existe un cliente con el DNI \'' + cliente.dni + '\'.')
                else:
                    EventosVentanas.abrirDialogAviso('ERROR: Faltan datos')
            else:
                EventosVentanas.abrirDialogAviso('ERROR: Formato DNI no valido o vacio')
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def bajaCliente():
        try:
            dni = var.ui.editDNI.text()

            if dni:
                if conexion.ConexionCliente.buscarCliente(dni) is not None:
                    if conexion.ConexionCliente.bajaCliente(dni):
                        var.ui.statusbar.showMessage('Cliente con DNI \'' + dni + '\' dado de baja.')
                        EventosCliente.limpiarCliente()
                        conexion.ConexionCliente.mostrarClientesTabla()
                    else:
                        EventosVentanas.abrirDialogAviso('ERROR: No se ha podido dar de baja al cliente con DNI \'' + dni +'\'.')
                else:
                    EventosVentanas.abrirDialogAviso('ERROR: No existe ningun cliente con el DNI \'' + dni + '\'.')
            else:
                EventosVentanas.abrirDialogAviso('ERROR: Introduzca un DNI para dar de baja')
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def modificarCliente():
        try:
            cliente = Cliente()
            cliente.rellenarDatosCliente()

            if cliente.comprobarDNI():
                if cliente.datosValidos():
                    if conexion.ConexionCliente.buscarCliente(cliente.dni) is not None:
                        if conexion.ConexionCliente.modificarCliente(cliente):
                            var.ui.statusbar.showMessage('Datos del cliente con DNI \'' + cliente.dni + '\' actualizados con exito.')
                            conexion.ConexionCliente.mostrarClientesTabla()
                        else:
                            EventosVentanas.abrirDialogAviso('ERROR: No se han podido modificar los datos del cliente con DNI \'' + cliente.dni + '\'.')
                    else:
                        EventosVentanas.abrirDialogAviso('ERROR: No existe ningun cliente con el DNI \'' + cliente.dni + '\'.')
                else:
                    EventosVentanas.abrirDialogAviso('ERROR: Faltan datos')
            else:
                EventosVentanas.abrirDialogAviso('ERROR: Formato DNI no valido o vacio')
        except Exception as error:
            print('Error: %s' % str(error))


class EventosProducto:

    @staticmethod
    def cargarDatosProducto():
        try:
            fila = var.ui.tablaProductos.selectedItems()
            producto = conexion.ConexionProducto.buscarProducto(fila[1].text())

            if producto:
                producto.rellenarFormularioProducto()
            else:
                EventosVentanas.abrirDialogAviso("ERROR: No se han podido cargar los datos")
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def buscarProducto():
        try:
            producto = conexion.ConexionProducto.buscarProducto(var.ui.editProducto.text())

            if producto is not None:
                index = 0
                var.ui.tablaProductos.setRowCount(0)
                var.ui.tablaProductos.setRowCount(index + 1)
                var.ui.tablaProductos.setItem(index, 0, QtWidgets.QTableWidgetItem(str(producto.codigoProducto)))
                var.ui.tablaProductos.setItem(index, 1, QtWidgets.QTableWidgetItem(producto.producto))
                var.ui.tablaProductos.setItem(index, 2, QtWidgets.QTableWidgetItem(str(producto.stock)))
                var.ui.tablaProductos.setItem(index, 3, QtWidgets.QTableWidgetItem("{:.2f}".format(producto.precio) + " €"))
                var.ui.tablaProductos.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tablaProductos.item(index, 2).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tablaProductos.item(index, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                index += 1


        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def limpiarProducto():
        try:
            var.ui.editCodigoProducto.setText('')
            var.ui.editProducto.setText('')

            var.ui.spinStock.setValue(0)
            var.ui.spinPrecio.setValue(0)
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def altaProducto():
        try:
            producto = Producto()
            producto.rellenarDatosProducto()

            if producto.datosValidos():
                if conexion.ConexionProducto.altaProducto(producto):
                    var.ui.statusbar.showMessage("Producto \'" + producto.producto +"\' dado de alta.")
                    EventosProducto.limpiarProducto()
                    conexion.ConexionProducto.mostrarProductosTabla()
                else:
                    EventosVentanas.abrirDialogAviso("ERROR: Ya existe ese producto \'" + producto.producto + "\'.")
            else:
                EventosVentanas.abrirDialogAviso("ERROR: Faltan datos")

        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def bajaProducto():
        try:
            producto = var.ui.editProducto.text()
            p = conexion.ConexionProducto.buscarProducto(producto)

            if var.ui.editProducto.text():
                if p is not None:
                    if conexion.ConexionProducto.bajaProducto(producto):
                        var.ui.statusbar.showMessage('Producto \'' + p.producto + '\' dado de baja.')
                        EventosProducto.limpiarProducto()
                        conexion.ConexionProducto.mostrarProductosTabla()
                    else:
                        EventosVentanas.abrirDialogAviso('ERROR: No se ha podido dar de baja el producto \'' + producto + '\'.')
                else:
                    EventosVentanas.abrirDialogAviso('ERROR: No existe ningun producto llamado \'' + producto + '\'.')
            else:
                EventosVentanas.abrirDialogAviso('ERROR: Introduzca un producto a eliminar.')
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def modificarProducto():
        try:
            producto = Producto()
            producto.rellenarDatosProducto()

            if producto.producto:
                if conexion.ConexionProducto.buscarProducto(producto.producto) is not None:
                    if conexion.ConexionProducto.modificarProducto(producto):
                        var.ui.statusbar.showMessage('Producto \'' + producto.producto + '\' actualizado con exito.')
                        conexion.ConexionProducto.mostrarProductosTabla()
                    else:
                        EventosVentanas.abrirDialogAviso('ERROR: No se han podido modificar el producto \'' + producto.producto + '\'.')
                else:
                    EventosVentanas.abrirDialogAviso('ERROR: No existe ningun producto llamado \'' + producto.producto + '\'.')
            else:
                EventosVentanas.abrirDialogAviso('ERROR: Introduzca un producto a modificar.')
        except Exception as error:
            print('Error: %s' % str(error))