import cCliente
import var
import ventanasDialogo

from PyQt5 import QtWidgets, QtCore, QtSql


class Factura:

    def __init__(self):
        self.nfactura = None
        self.fechafactura = ""
        self.dni = ""
        self.cliente = ""
        self.estado = var.ui.cmbTipoFacturas.currentText()

    def rellenarDatosFactura(self):
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
        try:
            var.ui.editFechaFactura.setText(self.fechafactura)
            var.ui.editDNIFacturacion.setText(self.dni)
            var.ui.editApellidosNombreFacturacion.setText(self.cliente)
            var.ui.editNFactura.setText(str(self.nfactura))
        except Exception as error:
            print('Error rellenarFormularioCliente: %s' % str(error))

    def datosValidos(self):

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
        # Cambiar el estado de los botones de pagar, borrar, anular, restaurar cuando editNFactura cambia
        var.ui.editNFactura.textChanged.connect(EventosFactura.editFacturaChange)

        # Borrar el numero de factura cuando un dato cambia
        var.ui.editDNIFacturacion.textChanged.connect(EventosFactura.editDNIFacturaChange)
        var.ui.editFechaFactura.textChanged.connect(EventosFactura.limpiarEditNFactura)

        # Cargar los valores del combobox de estado de la factura
        EventosFactura.comboboxFactura()

        # Evento al cambiar el valor del combobox de estado de la factura
        var.ui.cmbTipoFacturas.currentIndexChanged.connect(EventosFactura.buscarFactura)

        # Formato tabla facturas
        header = var.ui.tablaFacturas.horizontalHeader()
        header.show()

        var.ui.tablaFacturas.setColumnWidth(0, 52)
        var.ui.tablaFacturas.setColumnWidth(1, 72)
        var.ui.tablaFacturas.setColumnWidth(2, 72)
        var.ui.tablaFacturas.setColumnWidth(3, 218)

        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Custom)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Custom)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Custom)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        # Evento tabla facturas
        var.ui.tablaFacturas.clicked.connect(EventosFactura.cargarDatosFactura)

        # Botones producto
        var.ui.btnFacturacionNueva.clicked.connect(EventosFactura.altaFactura)
        var.ui.btnFacturacionPagar.clicked.connect(EventosFactura.pagarFactura)
        var.ui.btnFacturacionPagar.clicked.connect(EventosFactura.editFacturaChange)

        var.ui.btnFacturacionCalendario.clicked.connect(EventosFactura.calendarioFactura)

        var.ui.btnFaturacionBuscar.clicked.connect(EventosFactura.buscarFactura)
        var.ui.btnFacturacionLimpiar.clicked.connect(EventosFactura.limpiarFactura)
        var.ui.btnFacturacionRecargar.clicked.connect(EventosFactura.recargarFactura)

        # Cargar facturas en la tabla
        EventosFactura.recargarFactura()

    @staticmethod
    def limpiarEditNFactura():
        try:
            var.ui.editNFactura.setText("")
        except Exception as error:
            print('Error limpiarEditNFactura: %s' % str(error))

    @staticmethod
    def editDNIFacturaChange():
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
    def editFacturaChange():
        try:
            nfactura = var.ui.editNFactura.text()
            var.ui.btnFacturacionPagar.setEnabled(False)
            var.ui.btnFacturacionEliAnuRes.setEnabled(False)
            var.ui.btnFacturacionNueva.setEnabled(False)

            try: var.ui.btnFacturacionEliAnuRes.clicked.disconnect()
            except Exception: pass

            if nfactura != "":
                factura = Factura()
                factura.nfactura = nfactura
                factura = ConexionFactura.buscarFacturaDB(factura).pop()

                if factura.estado == "Pendiente":
                    var.ui.btnFacturacionPagar.setEnabled(True)
                    var.ui.btnFacturacionEliAnuRes.setEnabled(True)
                    var.ui.btnFacturacionEliAnuRes.setText('Eliminar')
                    var.ui.btnFacturacionEliAnuRes.clicked.connect(EventosFactura.eliminarFactura)
                elif factura.estado == "Pagada":
                    var.ui.btnFacturacionEliAnuRes.setEnabled(True)
                    var.ui.btnFacturacionEliAnuRes.setText('Anular')
                    var.ui.btnFacturacionEliAnuRes.clicked.connect(EventosFactura.anularFactura)
                elif factura.estado == "Anulada":
                    var.ui.btnFacturacionEliAnuRes.setEnabled(True)
                    var.ui.btnFacturacionEliAnuRes.setText('Restaurar')
                    var.ui.btnFacturacionEliAnuRes.clicked.connect(EventosFactura.restaurarFactura)

                var.ui.btnFacturacionEliAnuRes.clicked.connect(EventosFactura.editFacturaChange)
            else:
                var.ui.btnFacturacionNueva.setEnabled(True)
                var.ui.btnFacturacionEliAnuRes.setText('Eliminar')


        except Exception as error:
            print('Error editFacturaChange: %s' % str(error))

    @staticmethod
    def calendarioFactura():
        try:
            ventanasDialogo.EventosVentanas.abrirDialogCalendario(var.ui.editFechaFactura)
        except Exception as error:
            print('Error calendarioFactura: %s' % str(error))

    @staticmethod
    def comboboxFactura():
        try:
            for i in ['Pendiente', 'Pagada', 'Anulada', 'Todas']:
                var.ui.cmbTipoFacturas.addItem(i)
        except Exception as error:
            print('Error comboboxFactura: %s' % str(error))

    @staticmethod
    def cargarTablaFactura(facturas):
        try:
            index = 0
            var.ui.tablaFacturas.setRowCount(len(facturas))

            for factura in facturas:
                var.ui.tablaFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(factura.nfactura)))
                var.ui.tablaFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(factura.fechafactura))
                var.ui.tablaFacturas.setItem(index, 2, QtWidgets.QTableWidgetItem(factura.dni))
                var.ui.tablaFacturas.setItem(index, 3, QtWidgets.QTableWidgetItem(factura.cliente))

                var.ui.tablaFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tablaFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tablaFacturas.item(index, 2).setTextAlignment(QtCore.Qt.AlignCenter)

                index += 1

        except Exception as error:
            print('Error cargarTablaFacturas: %s' % str(error))

    @staticmethod
    def cargarDatosFactura():
        try:
            fila = var.ui.tablaFacturas.selectedItems()
            factura = Factura()
            factura.nfactura = fila[0].text()

            factura = ConexionFactura.buscarFacturaDB(factura)
            factura[0].rellenarFormularioFactura()
        except Exception as error:
            print('Error cargarDatosFactura: %s' % str(error))

    @staticmethod
    def cargarDatosClienteFactura(cliente):
        try:
            var.ui.editDNIFacturacion.setText(cliente.dni)
            var.ui.editApellidosNombreFacturacion.setText(cliente.apellidos + ", " + cliente.nombre)
        except Exception as error:
            print('Error cargarDatosCliente: %s' % str(error))

    @staticmethod
    def limpiarFactura():
        try:
            var.ui.editNFactura.setText("")
            var.ui.editFechaFactura.setText("")
            var.ui.editDNIFacturacion.setText("")
            var.ui.editApellidosNombreFacturacion.setText("")

            var.ui.editSubtotal.setText("")
            var.ui.editIVA.setText("")
            var.ui.editTotal.setText("")

        except Exception as error:
            print('Error limpiarFactura: %s' % str(error))

    @staticmethod
    def recargarFactura():
        try:
            facturas = ConexionFactura.buscarFacturaDB(Factura())
            var.ui.tablaFacturas.clearSelection()
            EventosFactura.cargarTablaFactura(facturas)
        except Exception as error:
            print('Error recargarFactura: %s' % str(error))

    @staticmethod
    def buscarFactura():
        try:
            factura = Factura()
            factura.rellenarDatosFactura()
            factura.nfactura = None
            facturas = ConexionFactura.buscarFacturaDB(factura)
            var.ui.tablaFacturas.clearSelection()
            EventosFactura.cargarTablaFactura(facturas)
        except Exception as error:
            print('Error buscarCliente: %s' % str(error))

    @staticmethod
    def altaFactura():
        try:
            factura = Factura()
            factura.rellenarDatosFactura()

            if factura.datosValidos():
                if ConexionFactura.altaFacturaDB(factura):
                    var.ui.statusbar.showMessage('Factura creada con exito.')
                    EventosFactura.limpiarFactura()
                    EventosFactura.recargarFactura()
                else:
                    ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: No se ha podido crear la factura.')
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: Faltan datos')

        except Exception as error:
            print('Error altaFactura: %s' % str(error))

    @staticmethod
    def pagarFactura():
        try:
            nfactura = var.ui.editNFactura.text()
            factura = Factura()

            factura.nfactura = nfactura
            factura.estado = 'Pagada'

            if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro de que desea marcar la factura como pagada?'):
                ConexionFactura.cambiarEstadoFacturaDB(factura)
                EventosFactura.recargarFactura()

        except Exception as error:
            print('Error altaFactura: %s' % str(error))

    @staticmethod
    def anularFactura():
        try:
            nfactura = var.ui.editNFactura.text()
            factura = Factura()

            factura.nfactura = nfactura
            factura.estado = 'Anulada'

            if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro de que desea anular la factura pagada?'):
                ConexionFactura.cambiarEstadoFacturaDB(factura)
                EventosFactura.recargarFactura()

        except Exception as error:
            print('Error altaFactura: %s' % str(error))

    @staticmethod
    def restaurarFactura():
        try:
            nfactura = var.ui.editNFactura.text()
            factura = Factura()

            factura.nfactura = nfactura
            factura.estado = 'Pagada'

            if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro de que desea restaurar la factura anulada?'):
                ConexionFactura.cambiarEstadoFacturaDB(factura)
                EventosFactura.recargarFactura()

        except Exception as error:
            print('Error altaFactura: %s' % str(error))

    @staticmethod
    def eliminarFactura():
        try:
            nfactura = var.ui.editNFactura.text()

            if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro de que desea eliminar la factura pendiente?'):
                ConexionFactura.eliminarFacturaDB(nfactura)
                EventosFactura.limpiarFactura()
                EventosFactura.recargarFactura()

        except Exception as error:
            print('Error altaFactura: %s' % str(error))


class ConexionFactura:

    @staticmethod
    def buscarFacturaDB(factura):
        try:
            facturas = []
            query = QtSql.QSqlQuery()

            b_nfactura = 'nfactura'
            b_fechafactura = 'fechafactura'
            b_dni = 'dni'
            b_estado = 'estado'

            if factura.nfactura is not None:
                b_nfactura = ':nfactura'
            else:
                if factura.fechafactura:
                    b_fechafactura = ':fechafactura'
                if factura.dni:
                    b_dni = ':dni'
                if factura.estado != 'Todas':
                    b_estado = ':estado'

            busqueda = 'nfactura = ' + b_nfactura + ' and fechafactura = ' + b_fechafactura + ' and dni = ' + b_dni + ' and estado = ' + b_estado

            query.prepare('select nfactura, fechafactura, dni, cliente, estado from facturas where ' + busqueda + ' order by nfactura')
            query.bindValue(':nfactura', factura.nfactura)
            query.bindValue(':fechafactura', factura.fechafactura)
            query.bindValue(':dni', factura.dni)
            query.bindValue(':estado', factura.estado)

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
    def altaFacturaDB(factura):
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
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from facturas where nfactura = :nfactura')
            query.bindValue(':nfactura', nfactura)
            return query.exec_()
        except Exception as error:
            print('Error eliminarFacturaDB: %s' % str(error))

    @staticmethod
    def cambiarEstadoFacturaDB(factura):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update facturas set estado=:estado where nfactura = :nfactura')
            query.bindValue(':nfactura', factura.nfactura)
            query.bindValue(':estado', factura.estado)

            return query.exec_()

        except Exception as error:
            print('Error cambiarEstadoFacturaDB: %s' % str(error))


class EventosVenta:

    @staticmethod
    def conectarEventosVenta():
        # Formato tabla ventas
        header = var.ui.tablaVentas.horizontalHeader()
        header.show()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)