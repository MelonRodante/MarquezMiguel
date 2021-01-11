import var
from cliente import Cliente


class Eventos:

    @staticmethod
    def DNIValido():
        try:
            dni = var.ui.editDNI.text()
            if dni != '':
                if Cliente.comprobarDNI():
                    var.ui.lblValido.setStyleSheet('QLabel {color: green}')
                    var.ui.lblValido.setText('V')
                    var.ui.editDNI.setText(dni.upper())
                else:
                    var.ui.lblValido.setStyleSheet('QLabel {color: red}')
                    var.ui.lblValido.setText('X')
                    var.ui.editDNI.setText(dni.upper())
            else:
                var.ui.lblValido.setText('')
        except Exception as error:
            print('Error: %s ' % str(error))



    @staticmethod
    def prueba():
        c = Cliente()

        print('DNI:', c.dni)
        print('Nombre:', c.nombre)
        print('Apellidos:', c.apellidos)
        print('Edad:', c.edad)
        print('Fecha Alta:', c.fechaAlta)
        print('Direccion:', c.direccion)
        print('Provincia:', c.provincia)
        print('Sexo:', c.sexo)
        print('Pago:', c.pago)

