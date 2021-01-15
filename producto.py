import var
import ventanasDialogo

from PyQt5 import QtWidgets, QtCore, QtSql


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
        var.ui.tablaProductos.itemSelectionChanged.connect(EventosProducto.cargarDatosProducto)
        var.ui.tablaProductos.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        # Botones producto
        var.ui.btnProductoBuscar.clicked.connect(EventosProducto.buscarProducto)
        var.ui.btnProductoRecargar.clicked.connect(ConexionProducto.mostrarProductosTabla)
        var.ui.btnProductoLimpiar.clicked.connect(EventosProducto.limpiarProducto)

        var.ui.btnProductoAlta.clicked.connect(EventosProducto.altaProducto)
        var.ui.btnProductoModificar.clicked.connect(EventosProducto.modificarProducto)
        var.ui.btnProductoBaja.clicked.connect(EventosProducto.bajaProducto)

        # Cargar productos en la tabla
        ConexionProducto.mostrarProductosTabla()

    @staticmethod
    def cargarDatosProducto():
        try:
            fila = var.ui.tablaProductos.selectedItems()
            producto = ConexionProducto.buscarProducto(fila[1].text())

            if producto:
                producto.rellenarFormularioProducto()
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso("ERROR: No se han podido cargar los datos")
        except Exception as error:
            print('Error cargarDatosProducto: %s' % str(error))

    @staticmethod
    def buscarProducto():
        try:
            producto = ConexionProducto.buscarProducto(var.ui.editProducto.text())

            if producto is not None:
                index = 0
                var.ui.tablaProductos.setRowCount(0)
                var.ui.tablaProductos.setRowCount(index + 1)
                var.ui.tablaProductos.setItem(index, 0, QtWidgets.QTableWidgetItem(str(producto.codigoProducto)))
                var.ui.tablaProductos.setItem(index, 1, QtWidgets.QTableWidgetItem(producto.producto))
                var.ui.tablaProductos.setItem(index, 2, QtWidgets.QTableWidgetItem(str(producto.stock)))
                var.ui.tablaProductos.setItem(index, 3, QtWidgets.QTableWidgetItem("{:.2f}".format(producto.precio) + " €"))
                var.ui.tablaProductos.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tablaProductos.item(index, 2).setTextAlignment(QtCore.Qt.AlignCenter)
                var.ui.tablaProductos.item(index, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                index += 1


        except Exception as error:
            print('Error buscarProducto: %s' % str(error))

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
    def altaProducto():
        try:
            producto = Producto()
            producto.rellenarDatosProducto()

            if producto.datosValidos():
                if ConexionProducto.altaProducto(producto):
                    var.ui.statusbar.showMessage("Producto \'" + producto.producto +"\' dado de alta.")
                    EventosProducto.limpiarProducto()
                    ConexionProducto.mostrarProductosTabla()
                else:
                    ventanasDialogo.EventosVentanas.abrirDialogAviso("ERROR: Ya existe ese producto \'" + producto.producto + "\'.")
            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso("ERROR: Faltan datos")

        except Exception as error:
            print('Error altaProducto: %s' % str(error))

    @staticmethod
    def bajaProducto():
        try:
            producto = var.ui.editProducto.text()
            p = ConexionProducto.buscarProducto(producto)

            if var.ui.editProducto.text():
                if p is not None:
                    if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro que desea dar de baja el producto \'' + producto + '\'?'):
                        if ConexionProducto.bajaProducto(producto):
                            var.ui.statusbar.showMessage('Producto \'' + p.producto + '\' dado de baja.')
                            EventosProducto.limpiarProducto()
                            ConexionProducto.mostrarProductosTabla()
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
                if ConexionProducto.buscarProducto(producto.producto) is not None:
                    if ventanasDialogo.EventosVentanas.abrirDialogConfimacion('¿Esta seguro que desea modificar el producto \'' + producto.producto + '\'?'):
                        if ConexionProducto.modificarProducto(producto):
                            var.ui.statusbar.showMessage('Producto \'' + producto.producto + '\' actualizado con exito.')
                            ConexionProducto.mostrarProductosTabla()
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
    def mostrarProductosTabla():
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codigoproducto, producto, stock, precio from productos')

            if query.exec_():
                var.ui.tablaProductos.setRowCount(0)
                while query.next():
                    var.ui.tablaProductos.setRowCount(index + 1)
                    var.ui.tablaProductos.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(0))))
                    var.ui.tablaProductos.setItem(index, 1, QtWidgets.QTableWidgetItem(query.value(1)))
                    var.ui.tablaProductos.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(2))))
                    var.ui.tablaProductos.setItem(index, 3, QtWidgets.QTableWidgetItem("{:.2f}".format(query.value(3)) + " € "))

                    var.ui.tablaProductos.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tablaProductos.item(index, 2).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tablaProductos.item(index, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

                    index += 1
            else:
                print("Error mostrar productos: ", query.lastError().text())

        except Exception as error:
            print('Error mostrarProductosTabla: %s' % str(error))

    @staticmethod
    def buscarProducto(producto):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select codigoproducto, producto, stock, precio from productos where producto = :producto')
            query.bindValue(':producto', producto)

            if query.exec_():
                if query.next():
                    p = Producto()
                    p.codigoProducto = query.value(0)
                    p.producto = query.value(1)
                    p.stock = query.value(2)
                    p.precio = query.value(3)
                    return p
                else:
                    return None
            else:
                return None

        except Exception as error:
            print('Error buscarProducto: %s' % str(error))

    @staticmethod
    def altaProducto(producto):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into productos (producto, stock, precio)'
                          'VALUES (:producto, :stock, :precio)')

            query.bindValue(':producto', producto.producto)
            query.bindValue(':stock', producto.stock)
            query.bindValue(':precio', producto.precio)

            if query.exec_():
                return True
            else:
                return False

        except Exception as error:
            print('Error altaProducto: %s' % str(error))

    @staticmethod
    def bajaProducto(producto):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from productos where producto = :producto')
            query.bindValue(':producto', producto)

            if query.exec_():
                return True
            else:
                return False

        except Exception as error:
            print('Error bajaProducto: %s' % str(error))

    @staticmethod
    def modificarProducto(producto):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update productos set stock=:stock, precio=:precio where producto = :producto')

            query.bindValue(':producto', producto.producto)
            query.bindValue(':stock', producto.stock)
            query.bindValue(':precio', producto.precio)

            if query.exec_():
                return True
            else:
                return False

        except Exception as error:
            print('Error modificarProducto: %s' % str(error))

    @staticmethod
    def listarProductos():
        try:
            productos = []
            query = QtSql.QSqlQuery()
            query.prepare('select codigoproducto, producto, stock, precio from productos order by stock')

            if query.exec_():
                while query.next():
                    producto = Producto()
                    producto.codigoProducto = query.value(0)
                    producto.producto = query.value(1)
                    producto.stock = query.value(2)
                    producto.precio = query.value(3)
                    productos.append(producto)
                return productos
            else:
                print('No se ha podido listar los productos')

        except Exception as error:
            print('Error listarProductos: %s' % str(error))


