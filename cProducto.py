import var
import ventanasDialogo

from PyQt5 import QtWidgets, QtCore, QtSql


class Producto:

    def __init__(self):
        self.codigoProducto = 0
        self.producto = ""

        self.stock = 0
        self.precio = 0

    def rellenarDatosProducto(self):
        try:
            self.codigoProducto = var.ui.editCodigoProducto.text()
            self.producto = var.ui.editProducto.text()

            self.stock = var.ui.spinStock.value()
            self.precio = var.ui.spinPrecio.value()
        except Exception as error:
            print('Error rellenarDatosProducto: %s' % str(error))

    def rellenarFormularioProducto(self):
        try:
            var.ui.editCodigoProducto.setText(str(self.codigoProducto))
            var.ui.editProducto.setText(self.producto)

            var.ui.spinStock.setValue(self.stock)
            var.ui.spinPrecio.setValue(self.precio)
        except Exception as error:
            print('Error rellenarFormularioProducto: %s' % str(error))

    def datosValidos(self):
        return self.producto != ""


class EventosProducto:

    @staticmethod
    def conectarEventosProducto():
        # Formato tabla productos
        header = var.ui.tablaProductos.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)

        # Evento tabla productos
        var.ui.tablaProductos.clicked.connect(EventosProducto.cargarDatosProducto)

        # Botones producto
        var.ui.btnProductoBuscar.clicked.connect(EventosProducto.buscarProducto)
        var.ui.btnProductoRecargar.clicked.connect(EventosProducto.recargarProducto)
        var.ui.btnProductoLimpiar.clicked.connect(EventosProducto.limpiarProducto)

        var.ui.btnProductoAlta.clicked.connect(EventosProducto.altaProducto)
        var.ui.btnProductoModificar.clicked.connect(EventosProducto.modificarProducto)
        var.ui.btnProductoBaja.clicked.connect(EventosProducto.bajaProducto)

        # Cargar productos en la tabla
        EventosProducto.recargarProducto()

    @staticmethod
    def cargarTablaProductos(productos):
        try:
            index = 0
            var.ui.tablaProductos.setRowCount(len(productos))

            for producto in productos:
                var.ui.tablaProductos.setItem(index, 0, QtWidgets.QTableWidgetItem(str(producto.codigoProducto)))
                var.ui.tablaProductos.setItem(index, 1, QtWidgets.QTableWidgetItem(producto.producto))
                var.ui.tablaProductos.setItem(index, 2, QtWidgets.QTableWidgetItem(str(producto.stock)))
                var.ui.tablaProductos.setItem(index, 3, QtWidgets.QTableWidgetItem("{:,.2f}".format(producto.precio) + " € "))

                var.ui.tablaProductos.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tablaProductos.item(index, 2).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tablaProductos.item(index, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                index += 1

        except Exception as error:
            print('Error cargarTablaProductos: %s' % str(error))

    @staticmethod
    def cargarDatosProducto():
        try:
            fila = var.ui.tablaProductos.selectedItems()
            producto = ConexionProducto.buscarProductoDB(fila[1].text()).pop()
            producto.rellenarFormularioProducto()
        except Exception as error:
            print('Error cargarDatosProducto: %s' % str(error))

    @staticmethod
    def limpiarProducto():
        try:
            var.ui.editCodigoProducto.setText('')
            var.ui.editProducto.setText('')

            var.ui.spinStock.setValue(0)
            var.ui.spinPrecio.setValue(0)
        except Exception as error:
            print('Error limpiarProducto: %s' % str(error))

    @staticmethod
    def recargarProducto():
        try:
            productos = ConexionProducto.buscarProductoDB("")
            EventosProducto.cargarTablaProductos(productos)
        except Exception as error:
            print('Error recargarProducto: %s' % str(error))

    @staticmethod
    def buscarProducto():
        try:
            producto = var.ui.editProducto.text()
            productos = ConexionProducto.buscarProductoDB(producto)
            EventosProducto.cargarTablaProductos(productos)
        except Exception as error:
            print('Error buscarProducto: %s' % str(error))

    @staticmethod
    def altaProducto():
        try:
            producto = Producto()
            producto.rellenarDatosProducto()

            if producto.datosValidos():
                if ConexionProducto.altaProductoDB(producto):
                    var.ui.statusbar.showMessage("Producto \'" + producto.producto + "\' dado de alta.")
                    EventosProducto.limpiarProducto()
                    EventosProducto.recargarProducto()
                else:
                    ventanasDialogo.EventosVentanas.abrirDialogAviso("ERROR: Ya existe el producto \'" + producto.producto + "\'.")
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso("ERROR: Faltan datos")

        except Exception as error:
            print('Error altaProducto: %s' % str(error))

    @staticmethod
    def bajaProducto():
        try:
            producto = var.ui.editProducto.text()

            if producto:
                if len(ConexionProducto.buscarProductoDB(producto)) != 0:
                    if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro que desea dar de baja el producto \'' + producto + '\'?'):
                        if ConexionProducto.bajaProductoDB(producto):
                            var.ui.statusbar.showMessage('Producto \'' + producto + '\' dado de baja.')
                            EventosProducto.limpiarProducto()
                            EventosProducto.recargarProducto()
                        else:
                            ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: No se ha podido dar de baja el producto \'' + producto + '\'.')
                else:
                    ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: No existe ningun producto llamado \'' + producto + '\'.')
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: Introduzca un producto a eliminar.')
        except Exception as error:
            print('Error bajaProducto: %s' % str(error))

    @staticmethod
    def modificarProducto():
        try:
            producto = Producto()
            producto.rellenarDatosProducto()

            if producto.producto:
                if len(ConexionProducto.buscarProductoDB(producto.producto)) != 0:
                    if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro que desea modificar el producto \'' + producto.producto + '\'?'):
                        if ConexionProducto.modificarProductoDB(producto):
                            var.ui.statusbar.showMessage('Producto \'' + producto.producto + '\' actualizado con exito.')
                            EventosProducto.recargarProducto()
                        else:
                            ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: No se han podido modificar el producto \'' + producto.producto + '\'.')
                else:
                    ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: No existe ningun producto llamado \'' + producto.producto + '\'.')
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso('ERROR: Introduzca un producto a modificar.')

        except Exception as error:
            print('Error modificarProducto: %s' % str(error))


class ConexionProducto:

    @staticmethod
    def buscarProductoDB(producto):
        try:
            productos = []
            query = QtSql.QSqlQuery()

            b_producto = 'producto'
            if producto:
                b_producto = ':producto'

            query.prepare('select codigoproducto, producto, stock, precio from productos where producto = ' + b_producto)
            query.bindValue(':producto', producto)

            if query.exec_():
                while query.next():
                    p = Producto()

                    p.codigoProducto = query.value(0)
                    p.producto = query.value(1)
                    p.stock = query.value(2)
                    p.precio = query.value(3)

                    productos.append(p)

                return productos
            else:
                return []

        except Exception as error:
            print('Error buscarProducto: %s' % str(error))

    @staticmethod
    def altaProductoDB(producto):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into productos (producto, stock, precio)'
                          'VALUES (:producto, :stock, :precio)')

            query.bindValue(':producto', producto.producto)
            query.bindValue(':stock', producto.stock)
            query.bindValue(':precio', producto.precio)

            return query.exec_()

        except Exception as error:
            print('Error altaProducto: %s' % str(error))

    @staticmethod
    def bajaProductoDB(producto):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from productos where producto = :producto')
            query.bindValue(':producto', producto)

            return query.exec_()

        except Exception as error:
            print('Error bajaProducto: %s' % str(error))

    @staticmethod
    def modificarProductoDB(producto):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update productos set stock=:stock, precio=:precio where producto = :producto')

            query.bindValue(':producto', producto.producto)
            query.bindValue(':stock', producto.stock)
            query.bindValue(':precio', producto.precio)

            return query.exec_()

        except Exception as error:
            print('Error modificarProducto: %s' % str(error))
