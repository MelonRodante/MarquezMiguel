import var
import ventanasDialogo

from PyQt5 import QtWidgets, QtCore, QtSql


class Cliente:

    def __init__(self):
        self.dni = ""
        self.nombre = ""
        self.apellidos = ""

        self.edad = 18
        self.fechaAlta = ""

        self.direccion = ""
        self.provincia = ""

        self.sexo = ""
        self.formaspago = ""

    def rellenarDatosCliente(self):
        try:
            self.dni = var.ui.editDNI.text()
            self.nombre = var.ui.editNombre.text()
            self.apellidos = var.ui.editApellidos.text()

            self.edad = var.ui.spinEdad.value()
            self.fechaAlta = var.ui.editFechaAlta.text()

            self.direccion = var.ui.editDireccion.text()
            self.provincia = var.ui.cmbProvincia.currentText()

            self.sexo = self.__selSexo()
            self.formaspago = self.__selPago()
        except Exception as error:
            print('Error rellenarDatosCliente: %s' % str(error))

    def rellenarFormularioCliente(self):
        try:
            var.ui.editDNI.setText(self.dni)
            var.ui.editNombre.setText(self.nombre)
            var.ui.editApellidos.setText(self.apellidos)

            var.ui.spinEdad.setValue(self.edad)
            var.ui.editFechaAlta.setText(self.fechaAlta)

            var.ui.editDireccion.setText(self.direccion)
            var.ui.cmbProvincia.setCurrentIndex(var.prov.index(self.provincia))

            if self.sexo == 'Hombre':
                var.ui.rbtMasculino.setChecked(True)
            else:
                var.ui.rbtFemenino.setChecked(True)

            var.ui.chkTransferencia.setChecked(self.formaspago.__contains__("Transferencia"))
            var.ui.chkTarjeta.setChecked(self.formaspago.__contains__("Tarjeta"))
            var.ui.chkEfectivo.setChecked(self.formaspago.__contains__("Efectivo"))

        except Exception as error:
            print('Error rellenarFormularioCliente: %s' % str(error))

    def datosValidos(self):

        if self.nombre == '':
            return False
        if self.apellidos == '':
            return False

        if self.fechaAlta == '':
            return False

        if self.direccion == '':
            return False
        if self.provincia == '':
            return False

        if self.sexo == '':
            return False
        if self.formaspago == '':
            return False

        return True

    @staticmethod
    def comprobarDNI():
        try:
            dni = var.ui.editDNI.text()

            if dni:
                tabla = "TRWAGMYFDPXBNJZSQVHLCKE"
                dig_ext = "XYZ"
                reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
                numeros = "1234567890"

                dni = dni.upper()

                if len(dni) == 9:
                    dig_control = dni[8]
                    dni = dni[:8]

                    if dni[0] in dig_ext:
                        dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])

                    return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control
                return False

        except Exception as error:
            print('Error comprobarDNI: %s' % str(error))
            return None

    @staticmethod
    def __selSexo():
        try:
            if var.ui.rbtFemenino.isChecked():
                return 'Mujer'
            elif var.ui.rbtMasculino.isChecked():
                return 'Hombre'
            else:
                return ''
        except Exception as error:
            print('Error __selSexo: %s' % str(error))

    @staticmethod
    def __selPago():
        try:
            pay = ""
            if var.ui.chkTransferencia.isChecked():
                pay = pay + '|Transferencia|'
            if var.ui.chkTarjeta.isChecked():
                pay = pay + '|Tarjeta|'
            if var.ui.chkEfectivo.isChecked():
                pay = pay + '|Efectivo|'
            return pay
        except Exception as error:
            print('Error __selPago: %s' % str(error))


class EventosCliente:

    @staticmethod
    def conectarEventosCliente():
        # Comprobar que el DNI sea valido y informar de ello
        var.ui.editDNI.editingFinished.connect(EventosCliente.DNIValido)

        # Cargar los valores de las provincias
        EventosCliente.comboboxCliente()

        # Formato tabla clientes
        header = var.ui.tablaClientes.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        # Evento tabla clientes
        var.ui.tablaClientes.itemSelectionChanged.connect(EventosCliente.cargarDatosCliente)
        var.ui.tablaClientes.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        # Botones cliente
        var.ui.btnCalendario.clicked.connect(EventosCliente.calendarioCliente)

        var.ui.btnClienteBuscar.clicked.connect(EventosCliente.buscarCliente)
        var.ui.btnClienteLimpiar.clicked.connect(EventosCliente.limpiarCliente)
        var.ui.btnClienteRecargar.clicked.connect(EventosCliente.recargarCliente)

        var.ui.btnClienteAlta.clicked.connect(EventosCliente.altaCliente)
        var.ui.btnClienteBaja.clicked.connect(EventosCliente.bajaCliente)
        var.ui.btnClienteModificar.clicked.connect(EventosCliente.modificarCliente)

        # Cargar clientes en la tabla
        EventosCliente.recargarCliente()

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
            print('Error DNIValido: %s ' % str(error))

    @staticmethod
    def calendarioCliente():
        try:
            ventanasDialogo.EventosVentanas.abrirDialogCalendario(var.ui.editFechaAlta)
        except Exception as error:
            print('Error calendarioCliente: %s' % str(error))

    @staticmethod
    def comboboxCliente():
        try:
            for i in var.prov:
                var.ui.cmbProvincia.addItem(i)
        except Exception as error:
            print('Error comboboxCliente: %s' % str(error))

    @staticmethod
    def cargarTablaClientes(clientes):
        try:
            index = 0
            var.ui.tablaClientes.setRowCount(0)

            for cliente in clientes:
                var.ui.tablaClientes.setRowCount(index + 1)
                var.ui.tablaClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(cliente.dni))
                var.ui.tablaClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(cliente.apellidos))
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(cliente.nombre))

                var.ui.tablaClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)

                index += 1

        except Exception as error:
            print('Error cargarTablaClientes: %s' % str(error))

    @staticmethod
    def cargarDatosCliente():
        try:
            fila = var.ui.tablaClientes.selectedItems()
            cliente = ConexionCliente.buscarClienteDB(fila[0].text()).pop()
            cliente.rellenarFormularioCliente()

        except Exception as error:
            print('Error cargarDatosCliente: %s' % str(error))

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
            print('Error limpiarCliente: %s' % str(error))

    @staticmethod
    def recargarCliente():
        try:
            clientes = ConexionCliente.buscarClienteDB("")
            EventosCliente.cargarTablaClientes(clientes)
        except Exception as error:
            print('Error recargarCliente: %s' % str(error))

    @staticmethod
    def buscarCliente():
        try:
            dni = var.ui.editDNI.text()
            clientes = ConexionCliente.buscarClienteDB(dni)
            EventosCliente.cargarTablaClientes(clientes)
        except Exception as error:
            print('Error buscarCliente: %s' % str(error))

    @staticmethod
    def altaCliente():
        try:
            cliente = Cliente()
            cliente.rellenarDatosCliente()

            if cliente.comprobarDNI():
                if cliente.datosValidos():
                    if ConexionCliente.altaClienteDB(cliente):
                        var.ui.statusbar.showMessage('Cliente con DNI \'' + cliente.dni + "\' dado de alta.")
                        EventosCliente.limpiarCliente()
                        EventosCliente.recargarCliente()
                    else:
                        ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: Ya existe un cliente con el DNI \'' + cliente.dni + '\'.')
                else:
                    ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: Faltan datos')
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: Formato DNI no valido o vacio')
        except Exception as error:
            print('Error altaCliente: %s' % str(error))

    @staticmethod
    def bajaCliente():
        try:
            dni = var.ui.editDNI.text()

            if dni:
                if len(ConexionCliente.buscarClienteDB(dni)) != 0:
                    if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro que desea dar de baja al cliente con DNI \'' + dni + '\'?'):
                        if ConexionCliente.bajaClienteDB(dni):
                            var.ui.statusbar.showMessage('Cliente con DNI \'' + dni + '\' dado de baja.')
                            EventosCliente.limpiarCliente()
                            EventosCliente.recargarCliente()
                        else:
                            ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: No se ha podido dar de baja al cliente con DNI \'' + dni +'\'.')
                else:
                    ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: No existe ningun cliente con el DNI \'' + dni + '\'.')
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: Introduzca un DNI para dar de baja')
        except Exception as error:
            print('Error bajaCliente: %s' % str(error))

    @staticmethod
    def modificarCliente():
        try:
            cliente = Cliente()
            cliente.rellenarDatosCliente()

            if cliente.dni:
                if len(ConexionCliente.buscarClienteDB(cliente.dni)) != 0:
                    if cliente.datosValidos():
                        if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro que desea dar de modificar los datos del cliente con DNI \'' + cliente.dni + '\'?'):
                            if ConexionCliente.modificarClienteDB(cliente):
                                var.ui.statusbar.showMessage('Datos del cliente con DNI \'' + cliente.dni + '\' actualizados con exito.')
                                EventosCliente.recargarCliente()
                            else:
                                ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: No se han podido modificar los datos del cliente con DNI \'' + cliente.dni + '\'.')
                    else:
                        ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: Faltan datos.')
                else:
                    ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: No existe ningun cliente con el DNI \'' + cliente.dni + '\'.')
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: Introduzca un DNI para modificar.')

        except Exception as error:
            print('Error modificarCliente: %s' % str(error))


class ConexionCliente:

    @staticmethod
    def buscarClienteDB(dni):
        try:
            clientes = []
            query = QtSql.QSqlQuery()

            bdni = 'dni'
            if dni:
                bdni = ':dni'

            query.prepare('select dni, nombre, apellidos, edad, fechaalta, direccion, provincia, sexo, formaspago from clientes where dni = ' + bdni)
            query.bindValue(':dni', dni)

            if query.exec_():
                while query.next():
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

                    clientes.append(cliente)

                return clientes
            else:
                return []

        except Exception as error:
            print('Error buscarClienteDB: %s' % str(error))

    @staticmethod
    def altaClienteDB(cliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into clientes (dni, nombre, apellidos, edad, fechaalta, direccion, provincia, sexo, formaspago)'
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

        except Exception as error:
            print('Error altaClienteDB: %s' % str(error))

    @staticmethod
    def bajaClienteDB(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from clientes where dni = :dni')
            query.bindValue(':dni', dni)

            if query.exec_():
                return True
            else:
                return False

        except Exception as error:
            print('Error bajaClienteDB: %s' % str(error))

    @staticmethod
    def modificarClienteDB(cliente):
        try:
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

        except Exception as error:
            print('Error modificarClienteDB: %s' % str(error))

