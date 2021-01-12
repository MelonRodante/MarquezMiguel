import var
import ventanas
import conexion
from cliente import Cliente


class EventosVarios:

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
    def cargarProvincias():
        try:
            for i in var.prov:
                var.ui.cmbProvincia.addItem(i)
        except Exception as error:
            print('Error: %s' % str(error))




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
    def cargarDatosCliente():
        try:
            fila = var.ui.tablaClientes.selectedItems()
            cliente = conexion.ConexionCliente.cargarDatosCliente(fila[0].text())

            if cliente:
                cliente.rellenarDatosFormulario()
            else:
                EventosVentanas.abrirDialogAviso("ERROR: No se han podido cargar los datos")

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
                        var.ui.statusbar.showMessage("Cliente con DNI " + cliente.dni + " dado de alta.")
                        EventosCliente.limpiarCliente()
                        conexion.ConexionCliente.mostrarClientesTabla()
                    else:
                        EventosVentanas.abrirDialogAviso("ERROR: Ya existe un cliente con ese DNI")
                else:
                    EventosVentanas.abrirDialogAviso("ERROR: Faltan datos")
            else:
                EventosVentanas.abrirDialogAviso("ERROR: Formato DNI no valido o vacio")
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def bajaCliente():
        try:
            dni = var.ui.editDNI.text()

            if dni:
                if conexion.ConexionCliente.clienteExiste(dni):
                    if conexion.ConexionCliente.bajaCliente(dni):
                        var.ui.statusbar.showMessage("Cliente con DNI " + dni + " dado de baja.")
                        EventosCliente.limpiarCliente()
                        conexion.ConexionCliente.mostrarClientesTabla()
                    else:
                        EventosVentanas.abrirDialogAviso('ERROR: No se ha podido dar de baja al cliente')
                else:
                    EventosVentanas.abrirDialogAviso('ERROR: No existe ningun cliente con ese DNI')
            else:
                EventosVentanas.abrirDialogAviso("ERROR: Necesita un DNI para dar de baja")
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def modificarCliente():
        try:
            cliente = Cliente()
            cliente.rellenarDatosCliente()

            if cliente.comprobarDNI():
                if cliente.datosValidos():
                    if conexion.ConexionCliente.clienteExiste(cliente.dni):
                        if conexion.ConexionCliente.modificarCliente(cliente):
                            var.ui.statusbar.showMessage("Datos del cliente " + cliente.dni + " actualizados con exito.")
                            conexion.ConexionCliente.mostrarClientesTabla()
                        else:
                            EventosVentanas.abrirDialogAviso("ERROR: No se han podido modificar los datos del cliente")
                    else:
                        EventosVentanas.abrirDialogAviso('ERROR: No existe ningun cliente con ese DNI')
                else:
                    EventosVentanas.abrirDialogAviso("ERROR: Faltan datos")
            else:
                EventosVentanas.abrirDialogAviso("ERROR: Formato DNI no valido o vacio")
        except Exception as error:
            print('Error: %s' % str(error))