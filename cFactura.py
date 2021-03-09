import cCliente
import cProducto
import var
import ventanasDialogo

from PyQt5 import QtWidgets, QtCore, QtSql


class Factura:

    facturas = None

    def __init__(self):
        """

        Constructor del objeto factura.

        :return: None
        :rtype: None

        Constructor del objeto factura que almacena los datos de una factura.

        """
        self.nfactura = None
        self.fechafactura = ""
        self.dni = ""
        self.cliente = ""
        self.estado = var.ui.cmbTipoFacturas.currentText()

    def rellenarDatosFactura(self):
        """

        Metodo que rellena los campos del objeto factura.

        :return: None
        :rtype: None

        Metodo que rellena los campos del objeto factura con los datos almacenados en el formulario de factura.

        """
        try:
            nfactura = var.ui.editNFactura.text()

            if nfactura != "":
                self.nfactura = int(nfactura)

            self.fechafactura = var.ui.editFechaFactura.text()
            self.dni = var.ui.editDNIFacturacion.text()
            self.cliente = var.ui.editApellidosNombreFacturacion.text()
            self.estado = var.ui.cmbTipoFacturas.currentText()
        except Exception as error:
            print('Error rellenarDatosCliente: %s' % str(error))

    def rellenarFormularioFactura(self):
        """

        Metodo que rellena los campos del formulario de factura.

        :return: None
        :rtype: None

        Metodo que rellena los campos del formulario de factura con los datos almacenados en el objeto factura.

        """
        try:
            var.ui.editFechaFactura.setText(self.fechafactura)
            var.ui.editDNIFacturacion.setText(self.dni)
            var.ui.editApellidosNombreFacturacion.setText(self.cliente)
            var.ui.editNFactura.setText(str(self.nfactura))
        except Exception as error:
            print('Error rellenarFormularioCliente: %s' % str(error))

    def datosValidos(self):
        """

        Metodo que comprueba la validez de los datos almacenados en el objeto factura.

        :return: Retorna si los datos son validos para dar de alta una factura.
        :rtype: bool

        Metodo que comprueba que ningun dato este vacio en el objeto factura.

        """
        if self.fechafactura == '':
            return False
        if self.dni == '':
            return False
        if self.cliente == '':
            return False

        return True


class EventosFactura:

    @staticmethod
    def conectarEventosFactura():
        """

        Módulo que conecta los eventos de la pestaña facturas y da formato a la tabla de facturas.

        :return: None
        :rtype: None

        Llama a la conexion con todos los eventos relacionados con los botones y widgets de la pestaña de clientes
        asi como ajustar el tamaño de las columnas de la tabla.

        """
        var.ui.editNFactura.textChanged.connect(EventosFactura.editNFacturaChange)

        var.ui.editDNIFacturacion.textChanged.connect(EventosFactura.editDNIFacturaChange)
        var.ui.editFechaFactura.textChanged.connect(EventosFactura.limpiarEditNFactura)

        EventosFactura.comboboxFactura()
        EventosFactura.comboboxDescuento()

        var.ui.cmbTipoFacturas.currentIndexChanged.connect(EventosFactura.cargarTablaFactura)

        header = var.ui.tablaFacturas.horizontalHeader()
        header.show()

        var.ui.tablaFacturas.setColumnWidth(0, 81)
        var.ui.tablaFacturas.setColumnWidth(1, 82)
        var.ui.tablaFacturas.setColumnWidth(2, 82)
        var.ui.tablaFacturas.setColumnWidth(3, 218)

        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Custom)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Custom)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Custom)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        var.ui.tablaFacturas.clicked.connect(EventosFactura.cargarDatosFactura)

        var.ui.btnFacturacionNueva.clicked.connect(EventosFactura.altaFactura)
        var.ui.btnFacturacionPagar.clicked.connect(EventosFactura.pagarFactura)
        var.ui.btnFacturacionPagar.clicked.connect(EventosFactura.editNFacturaChange)

        var.ui.btnFacturacionCalendario.clicked.connect(EventosFactura.calendarioFactura)

        var.ui.btnFaturacionBuscar.clicked.connect(EventosFactura.buscarFactura)
        var.ui.btnFacturacionLimpiar.clicked.connect(EventosFactura.limpiarFactura)
        var.ui.btnFacturacionRecargar.clicked.connect(EventosFactura.recargarFactura)

        EventosVenta.conectarEventosVenta()

        var.ui.btnDescuento.clicked.connect(EventosFactura.hacerDescuento)

        EventosFactura.recargarFactura()

    @staticmethod
    def limpiarEditNFactura():
        """

        Módulo que vacia el campo numero de factura del formulario de factura.

        :return: None
        :rtype: None

        Vacia el edit text numero de factura del formulario de factura.

        """
        try:
            var.ui.editNFactura.setText("")
        except Exception as error:
            print('Error limpiarEditNFactura: %s' % str(error))

    @staticmethod
    def editDNIFacturaChange():
        """

        Módulo rellena los datos del cliente en el formulario factura al escribir el DNI.

        :return: None
        :rtype: None

        Cuando el campo DNI de factura cambia si existe un cliente asociado a ese DNI escribe su nombre y apellidos en
        el formulario asi como borra el campo numero de factura.

        """
        try:
            dni = var.ui.editDNIFacturacion.text()
            var.ui.editDNIFacturacion.setText(dni.upper())
            if len(dni) == 9:
                cliente = cCliente.ConexionCliente.buscarClienteDB(dni)
                if len(cliente) != 0:
                    var.ui.editApellidosNombreFacturacion.setText(cliente[0].apellidos + ", " + cliente[0].nombre)
            else:
                var.ui.editApellidosNombreFacturacion.setText("")
            EventosFactura.limpiarEditNFactura()
        except Exception as error:
            print('Error editDNIFacturaChange: %s' % str(error))

    @staticmethod
    def editNFacturaChange():
        """

        Módulo cambia el estado de los botones de la pestaña de facturas cuando cambia el edit text de numero de factura.

        :return: None
        :rtype: None

        Cuando el contenido del edit text de numero de factura cambia se modifica el estado y los metodos que llaman los
        botones del formulario de factura, actualiza la tabla de ventas de la factura y actualiza el estado de los botones
        de venta de la factura.

        """
        try:
            nfactura = var.ui.editNFactura.text()

            var.ui.btnFacturacionPagar.setEnabled(False)
            var.ui.btnFacturacionEliAnuRes.setEnabled(False)
            var.ui.btnFacturacionNueva.setEnabled(False)
            try:
                var.ui.btnFacturacionEliAnuRes.clicked.disconnect()
            except Exception:
                pass

            estado = ''
            if nfactura != "":
                factura = Factura()
                factura.nfactura = nfactura
                estado = ConexionFactura.buscarFacturaDB(factura).pop().estado

                if estado == "Pendiente":
                    var.ui.btnFacturacionPagar.setEnabled(True)
                    var.ui.btnFacturacionEliAnuRes.setEnabled(True)
                    var.ui.btnFacturacionEliAnuRes.setText('Eliminar')
                    var.ui.btnFacturacionEliAnuRes.clicked.connect(EventosFactura.eliminarFactura)
                elif estado == "Pagada":
                    var.ui.btnFacturacionEliAnuRes.setEnabled(True)
                    var.ui.btnFacturacionEliAnuRes.setText('Anular')
                    var.ui.btnFacturacionEliAnuRes.clicked.connect(EventosFactura.anularFactura)
                elif estado == "Anulada":
                    var.ui.btnFacturacionEliAnuRes.setEnabled(True)
                    var.ui.btnFacturacionEliAnuRes.setText('Restaurar')
                    var.ui.btnFacturacionEliAnuRes.clicked.connect(EventosFactura.restaurarFactura)

                # Cuando se pulse el boton se vuelve a llamar al evento para actualizar el estado de los botones
                var.ui.btnFacturacionEliAnuRes.clicked.connect(EventosFactura.editNFacturaChange)

            else:
                var.ui.btnFacturacionNueva.setEnabled(True)
                var.ui.btnFacturacionEliAnuRes.setText('Eliminar')

            EventosVenta.cargarTablaVenta(nfactura, estado)
            EventosVenta.updateVentaButtons(estado)

        except Exception as error:
            print('Error editFacturaChange: %s' % str(error))

    @staticmethod
    def calendarioFactura():
        """

        Módulo que abre una ventana de dialogo en la que seleccionar la fecha de la factura.

        :return: None
        :rtype: None

        Llama al modulo para abrir la ventana de dialogo del calendario para seleccionar una fecha y le pasa como
        argumento el edit text donde debe almacenar el valor.

        """
        try:
            ventanasDialogo.EventosVentanas.abrirDialogCalendario(var.ui.editFechaFactura)
        except Exception as error:
            print('Error calendarioFactura: %s' % str(error))

    @staticmethod
    def comboboxFactura():
        """

        Módulo carga los valores de los estados de una factura en el combo box.

        :return: None
        :rtype: None

        Carga los estados posibles de una factyra en el combo box de la pestaña facturas.

        """
        try:
            for i in ['Pendiente', 'Pagada', 'Anulada', 'Todas']:
                var.ui.cmbTipoFacturas.addItem(i)
        except Exception as error:
            print('Error comboboxFactura: %s' % str(error))

    @staticmethod
    def cargarTablaFactura():
        """

        Módulo actualiza los valores de la tabla de facturas.

        :return: None
        :rtype: None

        Rellena la tabla de facturas con la lista de facturas que esta almacenada en una variable global en la clase
        Factura.

        Solo rellena la tabla con las facturas cuyo estado sea igual al del estado actual del combobox de facturas.

        """
        try:
            var.ui.tablaFacturas.setRowCount(0)
            for factura in Factura.facturas:
                if var.ui.cmbTipoFacturas.currentText() == 'Todas':
                    EventosFactura.cargarLineaTablaFactura(factura)
                elif var.ui.cmbTipoFacturas.currentText() == factura.estado:
                    EventosFactura.cargarLineaTablaFactura(factura)
        except Exception as error:
            print('Error cargarTablaFacturas: %s' % str(error))

    @staticmethod
    def cargarLineaTablaFactura(factura):
        """

        Módulo que añade una factura como una nueva fila en la tabla de facturas.

        :param factura: Lista de clientes para cargar en la tabla
        :type factura: Factura

        :return: None
        :rtype: None

        Rellena una fila de la tabla de facturas con una factura que recibe en los parametros.

        """
        try:
            index = var.ui.tablaFacturas.rowCount()

            var.ui.tablaFacturas.setRowCount(index + 1)

            var.ui.tablaFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(factura.nfactura)))
            var.ui.tablaFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(factura.fechafactura))
            var.ui.tablaFacturas.setItem(index, 2, QtWidgets.QTableWidgetItem(factura.dni))
            var.ui.tablaFacturas.setItem(index, 3, QtWidgets.QTableWidgetItem(factura.cliente))
            var.ui.tablaFacturas.setItem(index, 4, QtWidgets.QTableWidgetItem(factura.estado))

            var.ui.tablaFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
            var.ui.tablaFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignCenter)
            var.ui.tablaFacturas.item(index, 2).setTextAlignment(QtCore.Qt.AlignCenter)
            var.ui.tablaFacturas.item(index, 4).setTextAlignment(QtCore.Qt.AlignCenter)

        except Exception as error:
            print('Error cargarLineaTablaFactura: %s' % str(error))

    @staticmethod
    def cargarDatosFactura():
        """

        Módulo que carga una factura de la tabla en el formulario de factura.

        :return: None
        :rtype: None

        Al hacer click en una factura de la tabla recoge su numero de factura y carga todos sus datos en el formulario
        de factura.

        """
        try:
            fila = var.ui.tablaFacturas.selectedItems()
            factura = Factura()
            factura.nfactura = fila[0].text()

            factura = ConexionFactura.buscarFacturaDB(factura).pop()
            factura.rellenarFormularioFactura()
        except Exception as error:
            print('Error cargarDatosFactura: %s' % str(error))

    @staticmethod
    def cargarDatosClienteFactura(cliente):
        """

        Módulo rellena los campos del cliente en la pestaña facturacion.

        :param cliente: Objeto de cliente que contiene los datos a cargar en los edit text
        :type cliente: Cliente

        :return: None
        :rtype: None

        Recibe un objeto Cliente y escribe su DNI, nombre y apellidos en los edit text correspondientes de la pestaña
        de facturacion.

        """
        try:
            var.ui.editDNIFacturacion.setText(cliente.dni)
            var.ui.editApellidosNombreFacturacion.setText(cliente.apellidos + ", " + cliente.nombre)
        except Exception as error:
            print('Error cargarDatosCliente: %s' % str(error))

    @staticmethod
    def limpiarFactura():
        """

        Módulo limpia el formulario de factura.

        :return: None
        :rtype: None

        Vacia todos los datos del formulario de factura.

        """
        try:
            var.ui.editNFactura.setText("")
            var.ui.editFechaFactura.setText("")
            var.ui.editDNIFacturacion.setText("")
            var.ui.editApellidosNombreFacturacion.setText("")

            var.ui.editSubtotal.setText("")
            var.ui.editIVA.setText("")
            var.ui.editTotal.setText("")

            var.ui.cmbDescuento.setCurrentIndex(0)

        except Exception as error:
            print('Error limpiarFactura: %s' % str(error))

    @staticmethod
    def recargarFactura():
        """

        Módulo que recarga la tabla de facturas.

        :return: None
        :rtype: None

        Recarga la tabla de facturas.

        """
        try:
            Factura.facturas = ConexionFactura.buscarFacturaDB(Factura())
            var.ui.tablaFacturas.clearSelection()
            EventosFactura.cargarTablaFactura()
        except Exception as error:
            print('Error recargarFactura: %s' % str(error))

    @staticmethod
    def buscarFactura():
        """

        Módulo para buscar facturas y mostrarlas en la tabla.

        :return: None
        :rtype: None

        Crea un objeto tipo factura con los datos del formulario y realiza una busqueda de las facturas que tengan la
        misma fecha, el mismo DNI o ambos y carga todas las facturas encontradas en la tabla.

        """
        try:
            factura = Factura()
            factura.rellenarDatosFactura()
            factura.nfactura = None

            Factura.facturas = ConexionFactura.buscarFacturaDB(factura)
            var.ui.tablaFacturas.clearSelection()
            EventosFactura.cargarTablaFactura()
        except Exception as error:
            print('Error buscarCliente: %s' % str(error))

    @staticmethod
    def altaFactura():
        """

        Módulo que da de alta una factura.

        :return: None
        :rtype: None

        Recoge los datos del formulario de factura y los vuelca en un objeto factura y lo envia al metodo de alta en
        la base de datos.

        Tambien da un mensaje de error en una ventana de dialogo en caso de que falten datos, no sea posible dar de alta
        la factura o da un mensaje de confirmacion en la status bar.

        """
        try:
            factura = Factura()
            factura.rellenarDatosFactura()

            if factura.datosValidos():
                if ConexionFactura.altaFacturaDB(factura):
                    var.ui.statusbar.showMessage('Factura creada con exito.')
                    var.ui.editNFactura.setText(ConexionFactura.buscarUltimaFacturaDB(factura.dni, factura.fechafactura))
                    var.ui.cmbTipoFacturas.setCurrentIndex(0)
                    EventosFactura.buscarFactura()
                else:
                    ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: No se ha podido crear la factura.')
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: Faltan datos')

        except Exception as error:
            print('Error altaFactura: %s' % str(error))

    @staticmethod
    def pagarFactura():
        """

        Módulo que cambia el estado de una factura a pagada.

        :return: None
        :rtype: None

        Cambia el estado de la factura actual, aquella cuyo numero de factura este en el edit text de numero de factura,
        de pendiente a pagada tras pedirnos confirmacion.

        Solo permite cambiar el estado en caso de que tenga al menos una venta asociada a ese numero de factura.

        """
        try:
            if var.ui.tablaVentas.rowCount() > 1:
                nfactura = var.ui.editNFactura.text()
                factura = Factura()

                factura.nfactura = nfactura
                factura.estado = 'Pagada'

                if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro de que desea marcar la factura como pagada?'):
                    ConexionFactura.cambiarEstadoFacturaDB(factura)
                    var.ui.cmbTipoFacturas.setCurrentIndex(1)
                    EventosFactura.buscarFactura()
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso("Error: No puede pagarse una factura sin productos")

        except Exception as error:
            print('Error altaFactura: %s' % str(error))

    @staticmethod
    def anularFactura():
        """

        Módulo que cambia el estado de una factura a anulada.

        :return: None
        :rtype: None

        Cambia el estado de la factura actual, aquella cuyo numero de factura este en el edit text de numero de factura,
        de pagada a anulada tras pedirnos confirmacion.

        """
        try:
            nfactura = var.ui.editNFactura.text()
            factura = Factura()

            factura.nfactura = nfactura
            factura.estado = 'Anulada'

            if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro de que desea anular la factura pagada?'):
                ConexionFactura.cambiarEstadoFacturaDB(factura)
                var.ui.cmbTipoFacturas.setCurrentIndex(2)
                EventosFactura.buscarFactura()

        except Exception as error:
            print('Error altaFactura: %s' % str(error))

    @staticmethod
    def restaurarFactura():
        """

        Módulo que cambia el estado de una factura a pagada.

        :return: None
        :rtype: None

        Cambia el estado de la factura actual, aquella cuyo numero de factura este en el edit text de numero de factura,
        de anulada a pagada tras pedirnos confirmacion.

        """
        try:
            nfactura = var.ui.editNFactura.text()
            factura = Factura()

            factura.nfactura = nfactura
            factura.estado = 'Pagada'

            if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro de que desea restaurar la factura anulada?'):
                ConexionFactura.cambiarEstadoFacturaDB(factura)
                var.ui.cmbTipoFacturas.setCurrentIndex(1)
                EventosFactura.buscarFactura()

        except Exception as error:
            print('Error altaFactura: %s' % str(error))

    @staticmethod
    def eliminarFactura():
        """

        Módulo que cambia el estado de una factura a pagada cuando esta esta anulada.

        :return: None
        :rtype: None

        Borra de la base de datos la factura actual, aquella cuyo numero de factura este en el edit text de numero de
        factura, tras pedirnos confirmacion.

        """
        try:
            nfactura = var.ui.editNFactura.text()

            if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro de que desea eliminar la factura pendiente?'):
                ConexionFactura.eliminarFacturaDB(nfactura)
                var.ui.editNFactura.setText("")
                EventosFactura.buscarFactura()

        except Exception as error:
            print('Error altaFactura: %s' % str(error))

    @staticmethod
    def comboboxDescuento():
        try:
            for i in ['0 %', '5 %', '10 %', '15 %']:
                var.ui.cmbDescuento.addItem(i)
        except Exception as error:
            print('Error comboboxDescuento: %s' % str(error))

    @staticmethod
    def hacerDescuento():
        try:
            if var.ui.editNFactura.text():
                cmbIndex = var.ui.cmbDescuento.currentIndex()

                if cmbIndex == 0:
                    descuento = 0
                elif cmbIndex == 1:
                    descuento = 5
                elif cmbIndex == 2:
                    descuento = 10
                elif cmbIndex == 3:
                    descuento = 15
                else:
                    descuento = 0

                EventosVenta.updateTotalesFactura(descuento=descuento)
                if descuento > 0:
                    var.ui.statusbar.showMessage('Aplicado un ' + str(descuento) + '% de descuento')
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso("Seleccione una factura para hacer descuento")
        except Exception as error:
            print('Error hacerDescuento: %s' % str(error))


class ConexionFactura:

    @staticmethod
    def buscarFacturaDB(factura):
        """

        Módulo busca en la base de datos una factura concreta o todas las facturas.

        :param factura: Objeto de tipo factura que contiene los datos por los que se debe buscar
        :type factura: Factura

        :return: Devuelve una lista con todas las facturas que coinciden con los criterios a buscar
        :rtype: tuple

        Devuelve una lista con todas las facturas que cuadran con los criterios de busqueda que se reciben como un objeto
        de tipo factura, se puede buscar por numero de factura, DNI o fecha de factura.

        """
        try:
            facturas = []
            query = QtSql.QSqlQuery()

            b_nfactura = 'nfactura'
            b_fechafactura = 'fechafactura'
            b_dni = 'dni'

            if factura.nfactura is not None:
                b_nfactura = ':nfactura'
            else:
                if factura.fechafactura:
                    b_fechafactura = ':fechafactura'
                if factura.dni:
                    b_dni = ':dni'

            busqueda = 'nfactura = ' + b_nfactura + ' and fechafactura = ' + b_fechafactura + ' and dni = ' + b_dni

            query.prepare('select nfactura, fechafactura, dni, cliente, estado from facturas where ' + busqueda + ' order by nfactura')
            query.bindValue(':nfactura', factura.nfactura)
            query.bindValue(':fechafactura', factura.fechafactura)
            query.bindValue(':dni', factura.dni)

            if query.exec_():
                while query.next():
                    factura = Factura()

                    factura.nfactura = query.value(0)
                    factura.fechafactura = query.value(1)
                    factura.dni = query.value(2)
                    factura.cliente = query.value(3)
                    factura.estado = query.value(4)

                    facturas.append(factura)

                return facturas
            else:
                return []

        except Exception as error:
            print('Error buscarFacturaDB: %s' % str(error))

    @staticmethod
    def buscarUltimaFacturaDB(dni, fechafactura):
        """

        Módulo busca la ultima factura creada de un cliente.

        :param dni: DNI del cliente a buscar
        :type dni: str

        :param fechafactura: Fecha de la factura a buscar
        :type fechafactura: str

        :return: Devuelve como string el numero de la ultima factura que figura con el dni y fecha de la busqueda
        :rtype: str

        Devuelve el numero de factura de la ultima factura que corresponde al cliente con el dni y fecha de factura
        recibidos como parametro.

        """
        try:
            query = QtSql.QSqlQuery()

            query.prepare('select nfactura from facturas where dni=:dni and fechafactura=:fechafactura order by nfactura desc')
            query.bindValue(':dni', dni)
            query.bindValue(':fechafactura', fechafactura)

            if query.exec_():
                if query.next():
                    return str(query.value(0))
                else:
                    return None
            else:
                return None

        except Exception as error:
            print('Error buscarFacturaDB: %s' % str(error))

    @staticmethod
    def altaFacturaDB(factura):
        """

        Módulo que da de alta una factura en la BD.

        :param factura: Objeto de tipo Factura para darla de alta
        :type factura: Factura

        :return: Devuelve el resultado de la ejecucion de la sentensia sql
        :rtype: bool

        Da de alta una factura en la base de datos.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into facturas (fechafactura, dni, cliente, estado)'
                          'VALUES (:fechafactura, :dni, :cliente, "Pendiente")')

            query.bindValue(':fechafactura', factura.fechafactura)
            query.bindValue(':dni', factura.dni)
            query.bindValue(':cliente', factura.cliente)

            return query.exec_()

        except Exception as error:
            print('Error altaFacturaDB: %s' % str(error))

    @staticmethod
    def eliminarFacturaDB(nfactura):
        """

        Módulo da de baja una factura en la BD.

        :param nfactura: Numero de factura a dar de baja
        :type nfactura: str

        :return: Devuelve el resultado de la ejecucion de la sentensia sql
        :rtype: bool

        Elimina de la base de datos la factura con el numero de factura que recibe como parametro.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from facturas where nfactura = :nfactura')
            query.bindValue(':nfactura', nfactura)
            return query.exec_()
        except Exception as error:
            print('Error eliminarFacturaDB: %s' % str(error))

    @staticmethod
    def cambiarEstadoFacturaDB(factura):
        """

        Módulo que cambia el estado de una factura en la BD.

        :param factura: Objeto de tipo factura que contiene el numero de factura y estado a cambiar
        :type factura: Factura

        :return: Devuelve el resultado de la ejecucion de la sentensia sql
        :rtype: bool

        Cambia el estado de una factura en la base de datos en base al numero de factura y estado del objeto que recibe.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update facturas set estado=:estado where nfactura = :nfactura')
            query.bindValue(':nfactura', factura.nfactura)
            query.bindValue(':estado', factura.estado)

            return query.exec_()

        except Exception as error:
            print('Error cambiarEstadoFacturaDB: %s' % str(error))


class Venta:

    def __init__(self):
        """

        Constructor del objeto venta.

        :return: None
        :rtype: None

        Constructor del objeto venta que almacena los datos de una venta asociada a una factura.

        """
        self.nfactura = None
        self.producto = ""
        self.precio = 0
        self.unidades = 0


class EventosVenta:

    @staticmethod
    def conectarEventosVenta():
        """

        Módulo que conecta los eventos asociados a las ventas de una factura.

        :return: None
        :rtype: None

        Llama a la conexion con todos los eventos relacionados con los botones y widgets de la pestaña de facturas
        referentes a las ventas de una factura.

        """
        header = var.ui.tablaVentas.horizontalHeader()
        header.show()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        var.ui.btnFacturacionNuevoElemento.clicked.connect(EventosVenta.altaVenta)
        var.ui.btnFacturacionBorrarElemento.clicked.connect(EventosVenta.bajaVenta)

    @staticmethod
    def crearSpinVenta():
        """

        Módulo crea un widget de tipo spinner.

        :return: Devuelve un objeto de tipo spinner que esta alineado al centro a la derecha y no tiene botones
        :rtype: QtWidgets.QSpinBox

        Crea y devuelve un spinner para la cantidad de producto, el cual esta alineado a la derecha al centro, no tiene
        borde ni botones, tiene un maximo de 9999, un minimo de 1 y tiene un color de fondo correspondiente a la primera
        fila de la tabla.

        Tambien conecta a este spinner el metodo correspondiente al cambio del valor de la cantidad.

        """
        try:
            spinCantidad = QtWidgets.QSpinBox()
            spinCantidad.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            spinCantidad.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            spinCantidad.setFrame(False)
            spinCantidad.setMinimum(1)
            spinCantidad.setMaximum(9999)

            spinCantidad.setStyleSheet('background-color: rgb(198, 205, 255);')

            spinCantidad.valueChanged.connect(EventosVenta.precio_cantidadChange)

            return spinCantidad
        except Exception as error:
            print('Error crearSpinVenta: %s' % str(error))

    @staticmethod
    def crearComboboxVenta(nfactura):
        """

        Módulo crea un widget de tipo combobox.

        :param nfactura: Numero de la factura para comprobar los productos ya asociados a esta factura
        :type nfactura: str

        :return: Devuelve un objeto de tipo combobox que contiene todos los posibles productos a agregar a las ventas
        :rtype: QtWidgets.QComboBox

        Crea y devuelve un combobox que contiene todos los nombres de todos los productos que no esten ya asociados a
        ese numero de factura, ademas de quitar el borde y poner un color de fondo acorde a la fila de la tabla.

        Tambien conecta a este combobox con el metodo correspondiente al cambio de producto.

        """
        try:
            cmbProducto = QtWidgets.QComboBox()
            cmbProducto.setFrame(False)
            productos = ConexionVenta.buscarProductosNotInVentaDB(nfactura)

            cmbProducto.addItem("")
            for i in productos:
                cmbProducto.addItem(i)

            cmbProducto.setStyleSheet("QComboBox {"
                                      "     background-color: rgb(198, 205, 255);"
                                      "}"
                                      "QComboBox:on{"
                                      "     background-color: rgb(198, 205, 255);"
                                      "}"
                                      )

            cmbProducto.currentIndexChanged.connect(EventosVenta.comboboxVentaChange)

            return cmbProducto

        except Exception as error:
            print('Error crearComboboxVenta: %s' % str(error))

    @staticmethod
    def comboboxVentaChange():
        """

        Módulo cambia los valores de precio de la fila al cambiar el producto del combobox de la tabla de venta.

        :return: None
        :rtype: None

        Cambia el precio por unidad de la fila de la tabla de ventas al cambiar el producto del combobox de la tabla de
        ventas.

        """
        try:
            producto = var.ui.tablaVentas.cellWidget(0, 1).currentText()
            if producto != "":
                precio = cProducto.ConexionProducto.buscarProductoDB(producto).pop().precio
            else:
                precio = 0

            var.ui.tablaVentas.item(0, 2).setText("{:,.2f}".format(precio) + " € ")
            EventosVenta.precio_cantidadChange()
        except Exception as error:
            print('Error comboboxVentaChange: %s' % str(error))

    @staticmethod
    def precio_cantidadChange():
        """

        Módulo cambia los valores de precio de la factura al cambiar el precio o la cantidad de producto.

        :return: None
        :rtype: None

        Cambia el precio de los subtotales y totales de la factura cuando el precio o la cantidad del producto cambian.

        """
        try:
            cantidad = var.ui.tablaVentas.cellWidget(0, 0).value()
            precio = float(var.ui.tablaVentas.item(0, 2).text()[:-3])

            subtotal_producto = precio * cantidad

            var.ui.tablaVentas.item(0, 3).setText("{:,.2f}".format(subtotal_producto) + " € ")

            EventosVenta.updateTotalesFactura()

        except Exception as error:
            print('Error precio_cantidadChange: %s' % str(error))

    @staticmethod
    def updateTotalesFactura(descuento=0):
        """

        Módulo actualiza los valores de subtotal, impuestos y total de la factura.

        :return: None
        :rtype: None

        Actualiza los valores de subtotal, impuestos y total de la factura.

        """
        try:
            subtotal = 0
            for row in range(var.ui.tablaVentas.rowCount()):
                subtotal += float(var.ui.tablaVentas.item(row, 3).text()[:-3].replace(",", ""))

            if descuento != 0:
                subtotal = subtotal - (subtotal * (descuento / 100))

            iva = subtotal * 0.21

            var.ui.editSubtotal.setText("{:,.2f}".format(subtotal))
            var.ui.editIVA.setText("{:,.2f}".format(iva))
            var.ui.editTotal.setText("{:,.2f}".format(subtotal + iva))

        except Exception as error:
            print('Error updateTotalesFactura: %s' % str(error))

    @staticmethod
    def updateVentaButtons(estado):
        """

        Módulo cambia el estado de los botones de la pestaña de facturas asociados a las ventas.

        :param estado: Estado de la factura actual
        :type estado: str

        :return: None
        :rtype: None

        Cambia el estado de los botones asociados a las ventas dependiendo del estado de la factura actual, teniendo en
        cuenta el estado que recibe como parametro.

        """
        try:
            if estado == 'Pendiente':
                var.ui.btnFacturacionNuevoElemento.setEnabled(True)
                var.ui.btnFacturacionBorrarElemento.setEnabled(True)
            else:
                var.ui.btnFacturacionNuevoElemento.setEnabled(False)
                var.ui.btnFacturacionBorrarElemento.setEnabled(False)
        except Exception as error:
            print('Error updateVentaButtons: %s' % str(error))

    @staticmethod
    def cargarTablaVenta(nfactura, estado):
        """

        Módulo actualiza los valores de la tabla de ventas de una factura.

        :param nfactura: Numero de la factura actualmente seleccionada
        :type nfactura: str

        :param estado: Estado de la factura actualmente seleccionada
        :type estado: str

        :return: None
        :rtype: None

        Rellena la tabla de ventas de una factura con la lista de objetos venta que busca en la base de datos, ademas si
        el estado de la factura fuese pendiente agrega como primera linea una en la que poder introducirse un nuevo
        producto y su cantidad para agregar como venta de una factura.

        """
        try:
            index = 0
            var.ui.tablaVentas.setRowCount(0)
            ventas = ConexionVenta.buscarVentaDB(nfactura)

            if estado == "Pendiente":

                var.ui.tablaVentas.setRowCount(len(ventas) + 1)

                var.ui.tablaVentas.setCellWidget(0, 0, EventosVenta.crearSpinVenta())
                var.ui.tablaVentas.setCellWidget(0, 1, EventosVenta.crearComboboxVenta(nfactura))
                var.ui.tablaVentas.setItem(0, 2, QtWidgets.QTableWidgetItem("{:,.2f}".format(0) + " € "))
                var.ui.tablaVentas.setItem(0, 3, QtWidgets.QTableWidgetItem("{:,.2f}".format(0) + " € "))

                var.ui.tablaVentas.item(0, 2).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                var.ui.tablaVentas.item(0, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                var.ui.tablaVentas.item(0, 2).setFlags(QtCore.Qt.ItemIsEnabled)
                var.ui.tablaVentas.item(0, 3).setFlags(QtCore.Qt.ItemIsEnabled)

                index += 1

            else:
                var.ui.tablaVentas.setRowCount(len(ventas))

            EventosVenta.updateVentaButtons(estado)

            for venta in ventas:
                var.ui.tablaVentas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(venta.unidades)))
                var.ui.tablaVentas.setItem(index, 1, QtWidgets.QTableWidgetItem(venta.producto))
                var.ui.tablaVentas.setItem(index, 2, QtWidgets.QTableWidgetItem("{:,.2f}".format(venta.precio) + " € "))
                var.ui.tablaVentas.setItem(index, 3, QtWidgets.QTableWidgetItem("{:,.2f}".format(venta.unidades * venta.precio) + " € "))

                var.ui.tablaVentas.item(index, 0).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                var.ui.tablaVentas.item(index, 2).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                var.ui.tablaVentas.item(index, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                index += 1

            EventosVenta.updateTotalesFactura()

        except Exception as error:
            print('Error cargarTablaVenta: %s' % str(error))

    @staticmethod
    def altaVenta():
        """

        Módulo que da de alta una venta asociada a una factura.

        :return: None
        :rtype: None

        Recoge los datos de la primera linea de la tabla de ventas, los vuelca en un objeto Venta y lo envia al metodo
        de alta en la base de datos.

        Tambien da un mensaje de error en una ventana de dialogo en caso de que no se seleccione ningun producto en el
        combobox o da un mensaje de confirmacion en la status bar.

        """
        try:
            venta = Venta()
            venta.nfactura = var.ui.editNFactura.text()
            venta.unidades = var.ui.tablaVentas.cellWidget(0, 0).value()
            venta.producto = var.ui.tablaVentas.cellWidget(0, 1).currentText()
            venta.precio = float(var.ui.tablaVentas.item(0, 2).text()[:-3])

            if venta.producto != "":
                ConexionVenta.altaVentaDB(venta)
                EventosFactura.editNFacturaChange()
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso("Error: Seleccione un producto")


        except Exception as error:
            print('Error altaVenta: %s' % str(error))

    @staticmethod
    def bajaVenta():
        """

        Módulo que da de baja un grupo de ventas asociadas a una factura.

        :return: None
        :rtype: None

        Recoge las ventas seleccionadas en la tabla ventas y las elimina de las ventas asociadas a dicha factura.

        """
        try:
            nfactura = var.ui.editNFactura.text()
            productos_eliminar = var.ui.tablaVentas.selectedItems()

            i = 1
            for a in range(int(len(productos_eliminar)/4)):
                ConexionVenta.bajaVentaDB(nfactura, productos_eliminar[i].text())
                i += 4

            EventosFactura.editNFacturaChange()

        except Exception as error:
            print('Error altaVenta: %s' % str(error))


class ConexionVenta:

    @staticmethod
    def buscarVentaDB(nfactura):
        """

        Módulo busca en la base de datos todas las ventas asociadas a un numero de factura.

        :param nfactura: Numero de factura de las ventas a listar
        :type nfactura: str

        :return: Devuelve una lista con todas las ventas asociadas a un numero de factura
        :rtype: tuple

        Devuelve una lista con todas las facturas de la base de datos que tengan asociado el numero de factura que se
        recibe como parametro.

        """
        try:
            ventas = []
            query = QtSql.QSqlQuery()

            query.prepare('select producto, precio, unidades from ventas where nfactura = :nfactura')
            query.bindValue(':nfactura', nfactura)

            if query.exec_():
                while query.next():
                    venta = Venta()

                    venta.nfactura = nfactura
                    venta.producto = query.value(0)
                    venta.precio = query.value(1)
                    venta.unidades = query.value(2)

                    ventas.append(venta)

                return ventas
            else:
                return []

        except Exception as error:
            print('Error buscarVentaDB: %s' % str(error))

    @staticmethod
    def buscarProductosNotInVentaDB(nfactura):
        """

        Módulo busca en la base de datos todos los productos que no estan ya en una factura concreta.

        :param nfactura: Numero de factura a consultar
        :type nfactura: str

        :return: Devuelve una lista con todos los productos que no estan ya vendidos en una factura
        :rtype: tuple

        Devuelve una lista con todos los productos posibles que no esten ya asociados a una venta en una factura concreta.

        """
        try:
            productos = []
            query = QtSql.QSqlQuery()

            query.prepare(
                'SELECT producto FROM productos WHERE producto not in (select producto from ventas where nfactura = :nfactura) ORDER BY producto')
            query.bindValue(':nfactura', nfactura)

            if query.exec_():
                while query.next():
                    productos.append(query.value(0))

                return productos
            else:
                return []

        except Exception as error:
            print('Error buscarProductosNotInVentaDB: %s' % str(error))

    @staticmethod
    def altaVentaDB(venta):
        """

        Módulo que da de alta una venta en la BD.

        :param venta: Objeto de tipo Venta para darlo de alta
        :type venta: Venta

        :return: Devuelve el resultado de la ejecucion de la sentensia sql
        :rtype: bool

        Da de alta una venta asociada a una factura en la base de datos.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into ventas (nfactura, producto, precio, unidades)'
                'VALUES (:nfactura, :producto, :precio, :unidades)')

            query.bindValue(':nfactura', venta.nfactura)
            query.bindValue(':producto', venta.producto)
            query.bindValue(':precio', venta.precio)
            query.bindValue(':unidades', venta.unidades)

            return query.exec_()

        except Exception as error:
            print('Error altaClienteDB: %s' % str(error))

    @staticmethod
    def bajaVentaDB(nfactura, producto):
        """

        Módulo que da de baja una venta en la BD.

        :param nfactura: Numero de la factura cuya venta se quiere borrar
        :type nfactura: str

        :param producto: Producto de la factura que se quiere borrar
        :type producto: str

        :return: Devuelve el resultado de la ejecucion de la sentensia sql
        :rtype: bool

        Da de baja una venta asociada a una factura en la base de datos.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from ventas where nfactura = :nfactura and producto=:producto')
            query.bindValue(':nfactura', nfactura)
            query.bindValue(':producto', producto)

            return query.exec_()

        except Exception as error:
            print('Error bajaVentaDB: %s' % str(error))