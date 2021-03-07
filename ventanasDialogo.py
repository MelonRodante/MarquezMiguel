import os
import shutil
import sys
import zipfile

import cCliente
import cFactura
import cProducto
import var

from datetime import datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialogButtonBox

import ventanaPrincipal
from PYQT5_dialogAviso import Ui_dialogAviso
from PYQT5_dialogCalendario import Ui_dialogCalendario


class EventosVentanas:

    @staticmethod
    def abrirDialogCalendario(edit):
        """

        Modulo que abre una ventana de dialogo con un calendario para seleccionar una fecha.

        :param edit: Edit text en el que debe escribir la fecha seleccionada
        :type edit: QtWidgets.QLineEdit

        :return: None
        :rtype: None

        Abre una ventana de dialogo con un calendario para seleccionar una fecha y cargar esa fecha en un edit text que
        se le pasa como parametro.

        """
        try:
            dlgCalendar = DialogCalendario(edit=edit)
            dlgCalendar.exec_()
        except Exception as error:
            print('Error: %s ' % str(error))

    @staticmethod
    def abrirDialogSalir():
        """

        Módulo que abre una ventana de dialogo para cerrar el programa.

        :return: None
        :rtype: None

        Muestra una ventana de confirmacion para que el usuario elija si salir del programa o cancelar.

        """
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
        """

        Módulo que abre una ventana de dialogo con un mensaje.

        :param msg: Mensaje que debe mostrar la ventana
        :type msg: str

        :return: None
        :rtype: None

        Muestra una ventana de dialogo con un mensaje informativo que recibe como parametro.

        """
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
        """

        Módulo que abre una ventana de confirmacion con un mensaje.

        :param msg: Mensaje que debe mostrar la ventana
        :type msg: str

        :return: Devuelve True si se acepta o False si se cancela
        :rtype: bool

        Muestra una ventana de confirmacion con un mensaje que recibe como parametro.

        """
        try:
            dialog = DialogConfirmacion(msg)
            dialog.show()
            dialog.setFixedSize(dialog.size())
            return dialog.exec_()
        except Exception as error:
            print('El error es %s' % str(error))

    @staticmethod
    def hacerBackup():
        """

        Módulo que realizar el backup de la BBDD

        :return: None
        :rtype: None

        Utiliza la librería zipfile, añade la fecha y hora de la copia al nombre de esta y tras realizar la copia
        la mueve al directorio deseado por el cliente. Para ello abre una ventana de diálogo

        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            copia = (str(fecha) + '_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = QtWidgets.QFileDialog().getSaveFileName(None, 'Crear backup', copia, '.zip', options=option)
            if filename != '':
                fichzip = zipfile.ZipFile(copia, 'w')
                fichzip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                fichzip.close()
                var.ui.statusbar.showMessage('Backup creado con exito')
                shutil.move(str(copia), str(directorio))
        except Exception as error:
            print('El error es %s' % str(error))

    @staticmethod
    def restaurarBackup():
        """

        Módulo que restaura la BBDD

        :return: None
        :rtype: None

        Abre ventana de diálogo para buscar el directorio donde está copia de la BBDD y la restaura haciendo uso
        de la librería zipfile

        """
        try:
            option = QtWidgets.QFileDialog.Options()
            filename = QtWidgets.QFileDialog().getOpenFileName(None, 'Restaurar backup', '', '*.zip;;All Files', options=option)

            if filename != '':
                file = filename[0]
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
                var.ui.statusbar.showMessage('Backup de la BD restaurada')

                ventanaPrincipal.Conexion.conectardb(var.filedb)
                cCliente.EventosCliente.recargarCliente()
                cProducto.EventosProducto.recargarProducto()
                cFactura.EventosFactura.recargarFactura()


        except Exception as error:
            print('Error restaurar base de datos: %s ' % str(error))



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