import var


class Producto:

    def __init__(self):
        self.codigoProducto = ""
        self.producto = ""

        self.stock = 0
        self.precio = 0

    def rellenarDatosProducto(self):
        self.codigoProducto = var.ui.editCodigoProducto.text()
        self.producto = var.ui.editProducto.text()

        self.stock = var.ui.spinStock.value()
        self.precio = var.ui.spinPrecio.value()

    def rellenarFormularioProducto(self):
        var.ui.editCodigoProducto.setText(str(self.codigoProducto))
        var.ui.editProducto.setText(self.producto)

        var.ui.spinStock.setValue(self.stock)
        var.ui.spinPrecio.setValue(self.precio)

    def datosValidos(self):
        return self.producto != ""


