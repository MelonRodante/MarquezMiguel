import locale
import sys

from PyQt5 import QtWidgets
from ventanaPrincipal import VentanaPrincipal

#locale.setlocale(locale.LC_ALL, 'es-ES')

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = VentanaPrincipal()
    # window.showMaximized()
    window.show()
    sys.exit(app.exec_())









