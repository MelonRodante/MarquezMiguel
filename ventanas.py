import eventos
import var

from datetime import datetime
from PyQt5 import QtWidgets, QtCore
from venPrincipal import Ui_venPrincipal
from dialogCalendario import Ui_dialogCalendario


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
        var.ui.btnCalendario.clicked.connect(eventos.Eventos.abrirCalendario)

        var.ui.btnClienteAlta.clicked.connect(eventos.Eventos.prueba)


class DialogCalendario(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendario, self).__init__()
        self.dialogCalendario = Ui_dialogCalendario()
        self.dialogCalendario.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        self.dialogCalendario.widgetCalendario.setSelectedDate(QtCore.QDate(anoactual,mesactual,diaactual))
        self.dialogCalendario.widgetCalendario.clicked.connect(self.cargarFecha)

    def cargarFecha(self):
        try:
            date = self.dialogCalendario.widgetCalendario.selectedDate()
            data = ('{0}/{1}/{2}'.format(date.day(),date.month(),date.year()))
            var.ui.editFechaAlta.setText(str(data))
            self.close()
        except Exception as error:
            print('Error: %s' % str(error))