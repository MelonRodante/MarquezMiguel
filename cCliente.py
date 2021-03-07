import cFactura
import var
import ventanasDialogo

from PyQt5 import QtWidgets, QtCore, QtSql


class Cliente:

    def __init__(self):
        """

        Constructor del objeto cliente.

        :return: None
        :rtype: None

        Constructor del objeto cliente que almacena todos los datos de un cliente

        """
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
        """

        Metodo que rellena los campos del objeto cliente.

        :return: None
        :rtype: None

        Metodo que rellena los campos del objeto cliente con los datos almacenados en el formulario de cliente.

        """
        try:
            self.dni = var.ui.editDNI.text()
            self.nombre = var.ui.editNombre.text()
            self.apellidos = var.ui.editApellidos.text()

            self.edad = var.ui.spinEdad.value()
            self.fechaAlta = var.ui.editFechaAlta.text()

            self.direccion = var.ui.editDireccion.text()
            self.provincia = var.ui.cmbProvincia.currentText()

            self.__selSexo()
            self.__selPago()
        except Exception as error:
            print('Error rellenarDatosCliente: %s' % str(error))

    def rellenarFormularioCliente(self):
        """

        Metodo que rellena los campos del formulario de cliente.

        :return: None
        :rtype: None

        Metodo que rellena los campos del formulario de cliente con los datos almacenados en el objeto cliente.

        """
        try:

            var.ui.editNombre.setText(self.nombre)
            var.ui.editApellidos.setText(self.apellidos)

            var.ui.spinEdad.setValue(self.edad)
            var.ui.editFechaAlta.setText(self.fechaAlta)

            var.ui.editDireccion.setText(self.direccion)
            var.ui.cmbProvincia.setCurrentIndex(Cliente.provincias.index(self.provincia))

            var.ui.editDNI.setText(self.dni)

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
        """

        Metodo que comprueba la validez de los datos almacenados en el objeto cliente.

        :return: Retorna si los datos son validos para dar de alta o modificar un cliente.
        :rtype: bool

        Metodo que comprueba que ningun dato este vacio en el objeto cliente.

        """
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

    provincias = ['',
                  'Álava',
                  'Albacete ',
                  'Alicante ',
                  'Almería',
                  'Asturias',
                  'Ávila',
                  'Badajoz',
                  'Barcelona',
                  'Burgos',
                  'Cáceres',
                  'Cádiz',
                  'Cantabria',
                  'Castellón',
                  'Ciudad Real',
                  'Córdoba',
                  'Cuenca',
                  'Gerona',
                  'Granada',
                  'Guadalajara',
                  'Guipúzcoa',
                  'Huelva',
                  'Huesca',
                  'Islas Baleares ',
                  'Jaén',
                  'A Coruña',
                  'La Rioja',
                  'Las Palmas',
                  'León',
                  'Lérida',
                  'Lugo',
                  'Madrid',
                  'Málaga',
                  'Murcia',
                  'Navarra',
                  'Ourense',
                  'Palencia',
                  'Pontevedra',
                  'Salamanca',
                  'Santa Cruz de Tenerife',
                  'Segovia',
                  'Sevilla',
                  'Soria',
                  'Tarragona',
                  'Teruel',
                  'Toledo',
                  'Valencia',
                  'Valladolid',
                  'Vizcaya',
                  'Zamora',
                  'Zaragoza'
                  ]

    @staticmethod
    def comprobarDNI():
        dni = var.ui.editDNI.text()
        return Cliente.comprobarDNIValido(dni)

    @staticmethod
    def comprobarDNIValido(dni):
        """

        Módulo que comprueba la validez de un DNI.

        :return: Devuelve verdadero si el DNI es valido y falso si no lo es
        :rtype: bool

        Comprueba si el DNI en el edit text dni es un DNI valido.

        """
        try:
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

    def __selSexo(self):
        """

        Metodo que estable el sexo en el objeto cliente.

        :return: None
        :rtype: None

        Almacena el valor del sexo del cliente en el objeto Cliente en base a los radio button del formulario de cliente.

        """
        try:
            if var.ui.rbtFemenino.isChecked():
                self.sexo = 'Mujer'
            elif var.ui.rbtMasculino.isChecked():
                self.sexo = 'Hombre'
            else:
                self.sexo = ''
        except Exception as error:
            print('Error __selSexo: %s' % str(error))

    def __selPago(self):
        """

        Metodo que estable los metodos de pago en el objeto cliente.

        :return: None
        :rtype: None

        Construye una cadena que almacena los valores de los checkbox del formulario cliente y lo almacena en el
        campo metodospago del objeto cliente

        """
        try:
            pay = ""
            if var.ui.chkTransferencia.isChecked():
                pay = pay + '|Transferencia|'
            if var.ui.chkTarjeta.isChecked():
                pay = pay + '|Tarjeta|'
            if var.ui.chkEfectivo.isChecked():
                pay = pay + '|Efectivo|'
            self.formaspago = pay
        except Exception as error:
            print('Error __selPago: %s' % str(error))


class EventosCliente:

    @staticmethod
    def conectarEventosCliente():
        """

        Módulo que conecta los eventos de la pestaña clientes y da formato a la tabla.

        :return: None
        :rtype: None

        Llama a la conexion con todos los eventos relacionados con los botones y widgets de la pestaña de clientes
        asi como ajustar el tamaño de las columnas de la tabla.

        """
        var.ui.editDNI.textChanged.connect(EventosCliente.editDNIChange)

        EventosCliente.comboboxCliente()

        header = var.ui.tablaClientes.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

        var.ui.tablaClientes.clicked.connect(EventosCliente.cargarDatosCliente)


        var.ui.btnCalendario.clicked.connect(EventosCliente.calendarioCliente)

        var.ui.btnClienteBuscar.clicked.connect(EventosCliente.buscarCliente)
        var.ui.btnClienteLimpiar.clicked.connect(EventosCliente.limpiarCliente)
        var.ui.btnClienteRecargar.clicked.connect(EventosCliente.recargarCliente)

        var.ui.btnClienteAlta.clicked.connect(EventosCliente.altaCliente)
        var.ui.btnClienteBaja.clicked.connect(EventosCliente.bajaCliente)
        var.ui.btnClienteModificar.clicked.connect(EventosCliente.modificarCliente)

        EventosCliente.recargarCliente()

    @staticmethod
    def editDNIChange():
        """

        Módulo que comprueba la validez del DNI y carga los datos del cliente cuando el edit text de DNI cambia.

        :return: None
        :rtype: None

        Cuando el edit text de DNI cambia:

        Recoge el valor del DNI y comprueba que este sea valido, en caso de ser valido dibuja un check verde o una cruz
        roja en caso de no ser valido.

        Carga todos los datos del cliente en el formulario si hay un cliente con ese DNI.

        """
        try:
            dni = var.ui.editDNI.text()
            dni = dni.upper()
            var.ui.editDNI.setText(dni)

            if len(dni) == 9:
                cliente = ConexionCliente.buscarClienteDB(dni)
                if len(cliente) != 0:
                    cliente[0].rellenarFormularioCliente()
                if Cliente.comprobarDNI():
                    var.ui.lblValido.setStyleSheet('QLabel {color: green}')
                    var.ui.lblValido.setText('V')
                else:
                    var.ui.lblValido.setStyleSheet('QLabel {color: red}')
                    var.ui.lblValido.setText('X')
            else:
                var.ui.lblValido.setText('')

        except Exception as error:
            print('Error editDNIChange: %s' % str(error))

    @staticmethod
    def calendarioCliente():
        """

        Módulo que abre una ventana de dialogo en la que seleccionar la fecha de alta del cliente.

        :return: None
        :rtype: None

        Llama al modulo para abrir la ventana de dialogo del calendario para seleccionar una fecha y le pasa como
        argumento el edit text donde debe almacenar el valor.

        """
        try:
            ventanasDialogo.EventosVentanas.abrirDialogCalendario(var.ui.editFechaAlta)
        except Exception as error:
            print('Error calendarioCliente: %s' % str(error))

    @staticmethod
    def comboboxCliente():
        """

        Módulo carga los valores de las provincias en el combo box.

        :return: None
        :rtype: None

        Carga las provincias en el combo box de la pestaña clientes.

        """
        try:
            for i in Cliente.provincias:
                var.ui.cmbProvincia.addItem(i)
        except Exception as error:
            print('Error comboboxCliente: %s' % str(error))

    @staticmethod
    def cargarTablaClientes(clientes):
        """

        Módulo actualiza los valores de la tabla de clientes.

        :param clientes: Lista de clientes para cargar en la tabla
        :type clientes: tuple

        :return: None
        :rtype: None

        Rellena la tabla de cliente con la lista de objetos cliente que recibe como parametro.

        """
        try:
            index = 0
            var.ui.tablaClientes.setRowCount(len(clientes))

            for cliente in clientes:
                var.ui.tablaClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(cliente.dni))
                var.ui.tablaClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(cliente.apellidos))
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(cliente.nombre))
                var.ui.tablaClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(cliente.direccion))
                var.ui.tablaClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(cliente.provincia))

                var.ui.tablaClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)

                index += 1

        except Exception as error:
            print('Error cargarTablaClientes: %s' % str(error))

    @staticmethod
    def cargarDatosCliente():
        """

        Módulo que carga un cliente de la tabla en el formulario de cliente.

        :return: None
        :rtype: None

        Al hacer click en un cliente de la tabla recoge su dni y carga todos sus datos en el formulario de cliente y
        los datos de cliente en el formulario de facturacion.

        """
        try:
            fila = var.ui.tablaClientes.selectedItems()
            cliente = ConexionCliente.buscarClienteDB(fila[0].text())[0]

            var.ui.editDNI.setText("")
            var.ui.editDNI.setText(cliente.dni)

            var.ui.editDNIFacturacion.setText("")
            var.ui.editDNIFacturacion.setText(cliente.dni)
        except Exception as error:
            print('Error cargarDatosCliente: %s' % str(error))

    @staticmethod
    def limpiarCliente():
        """

        Módulo limpia el formulario de cliente.

        :return: None
        :rtype: None

        Vacia todos los datos del formulario cliente, desmarca los checkbox y los radio button.

        """
        try:
            var.ui.lblValido.setText('')

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

            var.ui.editDNI.setText('')

        except Exception as error:
            print('Error limpiarCliente: %s' % str(error))

    @staticmethod
    def recargarCliente():
        """

        Módulo que recarga la tabla de clientes.

        :return: None
        :rtype: None

        Recarga la tabla de clientes.

        """
        try:
            clientes = ConexionCliente.buscarClienteDB()
            EventosCliente.cargarTablaClientes(clientes)
        except Exception as error:
            print('Error recargarCliente: %s' % str(error))

    @staticmethod
    def buscarCliente():
        """

        Módulo para buscar un cliente concreto en la tabla de clientes.

        :return: None
        :rtype: None

        Recoge el dni del formulario de cliente y lo busca en la base de datos para luego pasarselo al modulo que carga
        la tabla de clientes.

        """
        try:
            dni = var.ui.editDNI.text()
            clientes = ConexionCliente.buscarClienteDB(dni)
            EventosCliente.cargarTablaClientes(clientes)
        except Exception as error:
            print('Error buscarCliente: %s' % str(error))

    @staticmethod
    def altaCliente():
        """

        Módulo que da de alta un cliente.

        :return: None
        :rtype: None

        Recoge los datos del formulario de cliente y los vuelca en un objeto cliente y lo envia al metodo de alta en
        la base de datos.

        Tambien da un mensaje de error en una ventana de dialogo en caso de que ya exista en la base de datos, falten
        datos, el formato del DNI no sea valido o da un mensaje de confirmacion en la status bar.

        """
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
        """

        Módulo que da de baja un cliente.

        :return: None
        :rtype: None

        Recoge el dni del formulario de cliente y lo envia al metodo de baja en la base de datos pidiendo antes
        confirmacion.

        Tambien da un mensaje de error en una ventana de dialogo en caso de que no haya ningun DNI en el edit text de
        dni, no existe ningun cliente con ese DNI o no fue posible darlo de baja.

        """
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
                            ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: No se ha podido dar de baja al cliente con DNI \'' + dni + '\'.')
                else:
                    ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: No existe ningun cliente con el DNI \'' + dni + '\'.')
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: Introduzca un DNI para dar de baja')
        except Exception as error:
            print('Error bajaCliente: %s' % str(error))

    @staticmethod
    def modificarCliente():
        """

        Módulo que modifica los datos de un cliente.

        :return: None
        :rtype: None

        Recoge el dni del formulario de cliente y lo envia al metodo de baja en la base de datos pidiendo antes
        confirmacion.

        Tambien da un mensaje de error en una ventana de dialogo en caso de que no haya ningun DNI en el edit text de
        dni, no existe ningun cliente con ese DNI o no fue posible modificar sus datos.

        """
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
    def buscarClienteDB(dni=""):
        """

        Módulo busca en la base de datos un cliente concreto o todos los clientes.

        :param dni: DNI del cliente a buscar, si no se recibe ningun DNI o el DNI esta vacio devuelve la lista de todos los clientes
        :type dni: str

        :return: Devuelve una lista con todos los clientes o el cliente cuyo dni recibe como paramtro
        :rtype: tuple

        En caso de que el parametro contenga una cadena que no este vacia busca en la BD un cliente cuyo dni
        recibe en parametros, si no se le pasa ninguno o la cadena esta vacia devolvera una lista con todos
        los clientes.

        """
        try:
            clientes = []
            query = QtSql.QSqlQuery()

            b_dni = 'dni'
            if dni:
                b_dni = ':dni'

            query.prepare('select dni, nombre, apellidos, edad, fechaalta, direccion, provincia, sexo, formaspago from clientes where dni = ' + b_dni + ' order by apellidos, nombre')
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
        """

        Módulo que da de alta el cliente en la BD.

        :param cliente: Objeto de tipo Cliente para darlo de alta
        :type cliente: Cliente

        :return: Devuelve el resultado de la ejecucion de la sentensia sql
        :rtype: bool

        Da de alta un cliente en la base de datos.

        """
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

            return query.exec_()

        except Exception as error:
            print('Error altaClienteDB: %s' % str(error))

    @staticmethod
    def bajaClienteDB(dni):
        """

        Módulo da de baja un cliente en la BD.

        :param dni: DNI del cliente a dar de baja
        :type dni: str

        :return: Devuelve el resultado de la ejecucion de la sentensia sql
        :rtype: bool

        Elimina de la base de datos al cliente con el dni que recibe como parametro.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from clientes where dni = :dni')
            query.bindValue(':dni', dni)

            return query.exec_()

        except Exception as error:
            print('Error bajaClienteDB: %s' % str(error))

    @staticmethod
    def modificarClienteDB(cliente):
        """

        Módulo modifica los datos de un cliente en la BD.

        :param cliente: Objeto de tipo cliente con los nuevos datos
        :type cliente: Cliente

        :return: Devuelve el resultado de la ejecucion de la sentensia sql
        :rtype: bool

        Actualiza la informacion del cliente en la base de datos.

        """
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

            return query.exec_()

        except Exception as error:
            print('Error modificarClienteDB: %s' % str(error))
