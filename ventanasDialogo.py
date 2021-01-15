import os
import shutil
import sys
import zipfile
import var

from datetime import datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialogButtonBox
from PYQT5_dialogAviso import Ui_dialogAviso
from PYQT5_dialogCalendario import Ui_dialogCalendario


class EventosVentanas:

    @staticmethod
    def abrirDialogCalendario(edit):
        try:
            dlgCalendar = DialogCalendario(edit=edit)
            dlgCalendar.exec_()
        except Exception as error:
            print('Error: %s ' % str(error))

    @staticmethod
    def abrirDialogSalir():
        try:
            dialog = DialogConfirmacion('¿Esta seguro que desea salir de la aplicacion?')
            dialog.show()
            dialog.setFixedSize(dialog.size())
            if dialog.exec_():
                sys.exit(0)
        except Exception as error:
            print('El error es %s' % str(error))

    @staticmethod
    def abrirDialogAviso(msg):
        try:
            var.ui.statusbar.showMessage(msg)

            dialog = DialogAviso(msg)
            dialog.show()
            dialog.setFixedSize(dialog.size())
            dialog.exec_()
        except Exception as error:
            print('El error es %s' % str(error))

    @staticmethod
    def abrirDialogConfimacion(msg):
        try:
            dialog = DialogConfirmacion(msg)
            dialog.show()
            dialog.setFixedSize(dialog.size())
            return dialog.exec_()
        except Exception as error:
            print('El error es %s' % str(error))

    @staticmethod
    def backup():
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            copia = (str(fecha) + '_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = QtWidgets.QFileDialog().getSaveFileName(None, 'Backup', copia, '.zip', options=option)
            if filename != '':
                fichzip = zipfile.ZipFile(copia, 'w')
                fichzip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                fichzip.close()
                var.ui.statusbar.showMessage('Backup creado con exito')
                shutil.move(str(copia), str(directorio))
        except Exception as error:
            print('El error es %s' % str(error))


class DialogCalendario(QtWidgets.QDialog):
    def __init__(self, edit):
        super(DialogCalendario, self).__init__()
        self.dialogCalendario = Ui_dialogCalendario()
        self.dialogCalendario.setupUi(self)
        self.edit = edit
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        self.dialogCalendario.widgetCalendario.setSelectedDate(QtCore.QDate(anoactual,mesactual,diaactual))
        self.dialogCalendario.widgetCalendario.clicked.connect(self.cargarFecha)

    def cargarFecha(self):
        try:
            date = self.dialogCalendario.widgetCalendario.selectedDate()
            data = ('{0}/{1}/{2}'.format(date.day(),date.month(),date.year()))
            self.edit.setText(str(data))
            self.close()
        except Exception as error:
            print('Error: %s' % str(error))


class DialogAviso(QtWidgets.QDialog):
    def __init__(self, msg):
        super(DialogAviso, self).__init__()
        self.ventana = Ui_dialogAviso()
        self.ventana.setupUi(self)
        self.ventana.botones.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.ventana.botones.button(QDialogButtonBox.Ok).setText("Aceptar")
        self.ventana.lblAviso.setText(msg)


class DialogConfirmacion(QtWidgets.QDialog):
    def __init__(self, msg):
        super(DialogConfirmacion, self).__init__()
        self.ventana = Ui_dialogAviso()
        self.ventana.setupUi(self)
        self.ventana.botones.setStandardButtons(QtWidgets.QDialogButtonBox.Yes | QtWidgets.QDialogButtonBox.No)
        self.ventana.botones.button(QDialogButtonBox.Yes).setText("Si")
        self.ventana.lblAviso.setText(msg)