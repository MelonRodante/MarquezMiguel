import var
import ventanasDialogo

from PyQt5 import QtWidgets, QtCore


class Factura:

    def __init__(self):
        self.nfactura = None
        self.fechafactura = ""
        self.dni = ""
        self.cliente = ""
        self.estado = ""


class EventosFactura:

    @staticmethod
    def conectarEventosFactura():
        # Cargar los valores del combobox de estado de la factura
        EventosFactura.cargarTipoFactura()

        # Formato tabla facturas
        header = var.ui.tablaFacturas.horizontalHeader()
        header.show()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        # Formato tabla ventas
        header = var.ui.tablaVentas.horizontalHeader()
        header.show()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)

        # Evento tabla facturas
        # var.ui.tablaClientes.clicked.connect(eventos.EventosCliente.cargarDatosCliente)
        var.ui.tablaFacturas.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        # Evento combobox
        # var.ui.cmbTipoFacturas.currentIndexChanged.connect(EventosFactura.buscarFacturas)

        # Botones producto
        var.ui.btnCalendarioFacturacion.clicked.connect(EventosFactura.calendarioFechaFactura)
        var.ui.btnFacturacionLimpiar.clicked.connect(EventosFactura.limpiarFactura)

        # var.ui.btnFaturacionBuscar.clicked.connect(EventosFactura.buscarFacturas)

        # Cargar facturas en la tabla
        # facturas.EventosFactura.recargarFacturas()

    @staticmethod
    def calendarioFechaFactura():
        try:
            ventanasDialogo.EventosVentanas.abrirDialogCalendario(var.ui.editFechaFactura)
        except Exception as error:
            print('Error calendarioFechaFactura: %s' % str(error))

    @staticmethod
    def cargarTipoFactura():
        try:
            for i in ['Pendiente', 'Pagada', 'Anulada', 'Todas']:
                var.ui.cmbTipoFacturas.addItem(i)
        except Exception as error:
            print('Error cargarTipoFactura: %s' % str(error))

    @staticmethod
    def cargarDatosCliente(cliente):
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

            EventosFactura.recargarFacturas()
        except Exception as error:
            print('Error limpiarFactura: %s' % str(error))

    @staticmethod
    def mostrarFacturasTabla(facturas):
        try:
            index = 0
            var.ui.tablaFacturas.setRowCount(0)

            for factura in facturas:
                var.ui.tablaFacturas.setRowCount(index + 1)
                var.ui.tablaFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(factura.nfactura)))
                var.ui.tablaFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(factura.fechafactura))
                var.ui.tablaFacturas.setItem(index, 2, QtWidgets.QTableWidgetItem(factura.dni))
                var.ui.tablaFacturas.setItem(index, 3, QtWidgets.QTableWidgetItem(factura.cliente))

                var.ui.tablaFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tablaFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tablaFacturas.item(index, 2).setTextAlignment(QtCore.Qt.AlignCenter)

                index += 1

        except Exception as error:
            print('Error mostrarFacturasTabla: %s' % str(error))

    '''@staticmethod
    def recargarFacturas():
        try:
            factura = Factura()
            factura.estado = var.ui.cmbTipoFacturas.currentText()
            facturas = ConexionFactura.buscarFacturas(factura)
            EventosFactura.mostrarFacturasTabla(facturas)
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def buscarFacturas():
        try:
            factura = Factura()
            factura.dni = var.ui.editDNIFacturacion.text()
            factura.fechafactura = var.ui.editFechaFactura.text()
            factura.estado = var.ui.cmbTipoFacturas.currentText()

            facturas = ConexionFactura.buscarFacturas(factura)
            EventosFactura.mostrarFacturasTabla(facturas)

        except Exception as error:
            print('Error: %s' % str(error))'''