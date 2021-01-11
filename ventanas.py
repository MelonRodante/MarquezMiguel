import eventos
import var

from datetime import datetime
from PyQt5 import QtWidgets
from venPrincipal import Ui_venPrincipal


class VentanaPrincipal(QtWidgets.QMainWindow):

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)

        ''' Label de fecha en el statusbar'''
        lblStatusFecha = QtWidgets.QLabel(datetime.now().strftime("%d %B %Y"))
        var.ui.statusbar.addPermanentWidget(lblStatusFecha)

        ''' Formateo tablas '''
        #Tabla clientes
        header = var.ui.tablaClientes.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        ''' Conexion Eventos '''

        # Comprobar que el DNI sea valido y informar de ello
        var.ui.editDNI.editingFinished.connect(eventos.Eventos.DNIValido)

        # Botones
        var.ui.btnClienteAlta.clicked.connect(eventos.Eventos.prueba)

