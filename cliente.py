import var


class Cliente:

    def __init__(self):
        self.dni = ""
        self.nombre = ""
        self.apellidos = ""

        self.edad = 18
        self.fechaAlta = ""

        self.direccion = ""
        self.provincia = ""

        self.sexo = ""
        self.formaspago = ""

    def rellenarDatosCliente(self):
        self.dni = var.ui.editDNI.text()
        self.nombre = var.ui.editNombre.text()
        self.apellidos = var.ui.editApellidos.text()

        self.edad = var.ui.spinEdad.value()
        self.fechaAlta = var.ui.editFechaAlta.text()

        self.direccion = var.ui.editDireccion.text()
        self.provincia = var.ui.cmbProvincia.currentText()

        self.sexo = self.__selSexo()
        self.formaspago = self.__selPago()

    def rellenarDatosFormulario(self):
        var.ui.editDNI.setText(self.dni)
        var.ui.editNombre.setText(self.nombre)
        var.ui.editApellidos.setText(self.apellidos)

        var.ui.spinEdad.setValue(self.edad)
        var.ui.editFechaAlta.setText(self.fechaAlta)

        var.ui.editDireccion.setText(self.direccion)
        var.ui.cmbProvincia.setCurrentIndex(var.prov.index(self.provincia))

        if self.sexo == 'Hombre':
            var.ui.rbtMasculino.setChecked(True)
        else:
            var.ui.rbtFemenino.setChecked(True)

        var.ui.chkTransferencia.setChecked(self.formaspago.__contains__("Transferencia"))
        var.ui.chkTarjeta.setChecked(self.formaspago.__contains__("Tarjeta"))
        var.ui.chkEfectivo.setChecked(self.formaspago.__contains__("Efectivo"))

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
        if self.formaspago == '':
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
    def __selSexo():
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
    def __selPago():
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