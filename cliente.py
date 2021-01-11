import eventos
import var


class Cliente:

    def __init__(self):
        self.dni = var.ui.editDNI.text()
        self.nombre = var.ui.editNombre.text()
        self.apellidos = var.ui.editApellidos.text()

        self.edad = var.ui.spinEdad.value()
        self.fechaAlta = var.ui.editFechaAlta.text()

        self.direccion = var.ui.editDireccion.text()
        self.provincia = var.ui.cmbProvincia.currentText()

        self.sexo = self.selSexo()
        self.pago = self.selPago()

    def datosValidos(self):

        if self.nombre == '':
            return False
        if self.apellidos == '':
            return False

        if self.fechaAlta == '':
            return False

        if self.direccion == '':
            return False
        if self.provincia == '':
            return False

        if self.sexo == '':
            return False
        if self.pago == '':
            return False

        return True

    @staticmethod
    def comprobarDNI():
        try:
            dni = var.ui.editDNI.text()

            if dni:
                tabla = "TRWAGMYFDPXBNJZSQVHLCKE"
                dig_ext = "XYZ"
                reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
                numeros = "1234567890"

                dni = dni.upper()
                if len(dni) == 9:
                    dig_control = dni[8]
                    dni = dni[:8]
                    if dni[0] in dig_ext:
                        dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                    return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control
                return False
        except:
            print('error en la aplicacion')
            return None

    @staticmethod
    def selSexo():
        try:
            if var.ui.rbtFemenino.isChecked():
                return 'Mujer'
            elif var.ui.rbtMasculino.isChecked():
                return 'Hombre'
            else:
                return ''
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def selPago():
        try:
            pay = ""
            if var.ui.chkTransferencia.isChecked():
                pay = pay + ',Transferencia,'
            if var.ui.chkTarjeta.isChecked():
                pay = pay + ',Tarjeta,'
            if var.ui.chkEfectivo.isChecked():
                pay = pay + ',Efectivo,'
            return pay
        except Exception as error:
            print('Error: %s' % str(error))