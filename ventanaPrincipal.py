from PyQt5.QtWidgets import QProgressBar

import cInformes
import var

import cCliente
import cProducto
import cFactura
import informes
import ventanasDialogo

from datetime import datetime
from PyQt5 import QtWidgets, QtSql
from PYQT5_venPrincipal import Ui_venPrincipal


class VentanaPrincipal(QtWidgets.QMainWindow):

    def __init__(self):
        """

        Constructor de la ventana principal del programa.

        :return: None
        :rtype: None

        Constructor de la ventana principal del programa, en el constructor se llama a los diferentes metodos de conexion
        de los eventos de los diferentes widgets de la aplicacion.

        """
        super(VentanaPrincipal, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)

        var.ui.actionAbrir.triggered.connect(QtWidgets.QFileDialog.getSaveFileName)
        #var.ui.actionImprimir.triggered.connect(ventanasDialogo.EventosVentanas.abrirDialogConfimacion)

        var.ui.actionCrear_Backup.triggered.connect(ventanasDialogo.EventosVentanas.hacerBackup)
        var.ui.actionRestaurar_Backup.triggered.connect(ventanasDialogo.EventosVentanas.restaurarBackup)

        var.ui.actionImportar_Datos.triggered.connect(cProducto.EventosProducto.importarDatos)

        var.ui.actionSalir.triggered.connect(ventanasDialogo.EventosVentanas.abrirDialogSalir)

        ''' Label de fecha en el statusbar y barra de carga'''
        var.ui.lblStatusFecha = QtWidgets.QLabel(datetime.now().strftime("%d %B %Y"))
        var.ui.pbar = QProgressBar()
        var.ui.pbar.setMaximumSize(150, 15)
        var.ui.statusbar.addPermanentWidget(var.ui.pbar)
        var.ui.statusbar.addPermanentWidget(var.ui.lblStatusFecha)
        var.ui.pbar.hide()


        ''' Conexion con la base de datos '''
        Conexion.conectardb(var.filedb)

        ''' Conexion Eventos Cliente'''
        cCliente.EventosCliente.conectarEventosCliente()

        ''' Conexion Eventos Producto '''
        cProducto.EventosProducto.conectarEventosProducto()

        ''' Conexion Eventos Facturas '''
        cFactura.EventosFactura.conectarEventosFactura()

        ''' Conexion Eventos Informes '''
        cInformes.Informes.conectarEventosFactura()

        ''' Evento de cerrado de la aplicacion '''
        QtWidgets.QAction(self).triggered.connect(self.close)

    def closeEvent(self, event):
        """

        Módulo que abre una ventana de dialogo para cerrar el programa cuando se pulsa la cruz de la ventana.

        :return: None
        :rtype: None

        Muestra una ventana de confirmacion para que el usuario elija si salir del programa o cancelar.

        """
        ventanasDialogo.EventosVentanas.abrirDialogSalir()
        event.ignore()


class Conexion:

    @staticmethod
    def conectardb(filename):
        """

        Módulo que realiza la conexión de la aplicación con la BBDD

        :param filename: nombre del archivo de la BBDD
        :type filename: str

        :return: True o False
        :rtype: bool

        Utiliza la librería de QtSql y el gestor de la BBDD es QSQlite. En caso de error muestra pantalla
        de aviso.

        """
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
