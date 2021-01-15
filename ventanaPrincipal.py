import var

import cliente
import producto
import factura
import informes
import ventanasDialogo

from datetime import datetime
from PyQt5 import QtWidgets, QtSql
from venPrincipal import Ui_venPrincipal


class VentanaPrincipal(QtWidgets.QMainWindow):

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)

        ''' Eventos menubar y toolbar '''
        var.ui.actionAbrir.triggered.connect(QtWidgets.QFileDialog.getSaveFileName)
        #var.ui.actionImprimir.triggered.connect(ventanasDialogo.EventosVentanas.abrirDialogConfimacion)

        var.ui.actionCrear_Backup.triggered.connect(ventanasDialogo.EventosVentanas.backup)

        var.ui.actionInforme_Clientes.triggered.connect(informes.Informes.informeClientes)
        var.ui.actionInforme_Productos.triggered.connect(informes.Informes.informeProductos)

        var.ui.actionSalir.triggered.connect(ventanasDialogo.EventosVentanas.abrirDialogSalir)

        ''' Label de fecha en el statusbar '''
        lblStatusFecha = QtWidgets.QLabel(datetime.now().strftime("%d %B %Y"))
        var.ui.statusbar.addPermanentWidget(lblStatusFecha)

        ''' Conexion con la base de datos '''
        Conexion.conectardb(var.filedb)

        ''' Conexion Eventos Cliente'''
        cliente.EventosCliente.conectarEventosCliente()

        ''' Conexion Eventos Producto '''
        producto.EventosProducto.conectarEventosProducto()

        ''' Conexion Eventos Facturas '''
        factura.EventosFactura.conectarEventosFactura()

        ''' Evento de cerrado de la aplicacion '''
        QtWidgets.QAction(self).triggered.connect(self.close)

    def closeEvent(self, event):
        ventanasDialogo.EventosVentanas.abrirDialogSalir()
        event.ignore()

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