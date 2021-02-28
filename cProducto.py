import var
import ventanasDialogo

from PyQt5 import QtWidgets, QtCore, QtSql


class Producto:

    def __init__(self):
        """

        Constructor del objeto cliente.

        :return: None
        :rtype: None

        Constructor del objeto producto que almacena todos los datos de un producto

        """
        self.codigoProducto = 0
        self.producto = ""

        self.stock = 0
        self.precio = 0

    def rellenarDatosProducto(self):
        """

        Metodo que rellena los campos del objeto producto.

        :return: None
        :rtype: None

        Metodo que rellena los campos del objeto producto con los datos almacenados en el formulario de producto.

        """
        try:
            self.codigoProducto = var.ui.editCodigoProducto.text()
            self.producto = var.ui.editProducto.text()

            self.stock = var.ui.spinStock.value()
            self.precio = var.ui.spinPrecio.value()
        except Exception as error:
            print('Error rellenarDatosProducto: %s' % str(error))

    def rellenarFormularioProducto(self):
        """

        Metodo que rellena los campos del formulario de producto.

        :return: None
        :rtype: None

        Metodo que rellena los campos del formulario de producto con los datos almacenados en el objeto producto.

        """
        try:
            var.ui.editCodigoProducto.setText(str(self.codigoProducto))
            var.ui.editProducto.setText(self.producto)

            var.ui.spinStock.setValue(self.stock)
            var.ui.spinPrecio.setValue(self.precio)
        except Exception as error:
            print('Error rellenarFormularioProducto: %s' % str(error))

    def datosValidos(self):
        """

        Metodo que comprueba la validez de los datos almacenados en el objeto producto.

        :return: Retorna si los datos son validos para dar de alta un producto.
        :rtype: bool

        Metodo que comprueba que el nombre del producto no sea una cadena vacia.

        """
        return self.producto != ""


class EventosProducto:

    @staticmethod
    def conectarEventosProducto():
        """

        Módulo que conecta los eventos de la pestaña productos y da formato a la tabla.

        :return: None
        :rtype: None

        Llama a la conexion con todos los eventos relacionados con los botones y widgets de la pestaña de productos
        asi como ajustar el tamaño de las columnas de la tabla.

        """
        header = var.ui.tablaProductos.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)

        var.ui.tablaProductos.clicked.connect(EventosProducto.cargarDatosProducto)

        var.ui.btnProductoBuscar.clicked.connect(EventosProducto.buscarProducto)
        var.ui.btnProductoRecargar.clicked.connect(EventosProducto.recargarProducto)
        var.ui.btnProductoLimpiar.clicked.connect(EventosProducto.limpiarProducto)

        var.ui.btnProductoAlta.clicked.connect(EventosProducto.altaProducto)
        var.ui.btnProductoModificar.clicked.connect(EventosProducto.modificarProducto)
        var.ui.btnProductoBaja.clicked.connect(EventosProducto.bajaProducto)

        EventosProducto.recargarProducto()

    @staticmethod
    def cargarTablaProductos(productos):
        """

        Módulo actualiza los valores de la tabla de productos.

        :param productos: Lista de productos para cargar en la tabla
        :type productos: tuple

        :return: None
        :rtype: None

        Rellena la tabla de cliente con la lista de objetos cliente que recibe como parametro.

        """
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
        """

        Módulo carga un producto de la tabla en el formulario de producto.

        :return: None
        :rtype: None

        Al hacer click en un producto de la tabla recoge el nombre del producto y carga todos sus datos en el formulario
        de producto.

        """
        try:
            fila = var.ui.tablaProductos.selectedItems()
            producto = ConexionProducto.buscarProductoDB(fila[1].text()).pop()
            producto.rellenarFormularioProducto()
        except Exception as error:
            print('Error cargarDatosProducto: %s' % str(error))

    @staticmethod
    def limpiarProducto():
        """

        Módulo limpia el formulario de producto.

        :return: None
        :rtype: None

        Vacia todos los datos del formulario producto, y pone a 0 el spinner de precio.

        """
        try:
            var.ui.editCodigoProducto.setText('')
            var.ui.editProducto.setText('')

            var.ui.spinStock.setValue(0)
            var.ui.spinPrecio.setValue(0)
        except Exception as error:
            print('Error limpiarProducto: %s' % str(error))

    @staticmethod
    def recargarProducto():
        """

        Módulo que recarga la tabla de productos.

        :return: None
        :rtype: None

        Recarga la tabla de productos.

        """
        try:
            productos = ConexionProducto.buscarProductoDB("")
            EventosProducto.cargarTablaProductos(productos)
        except Exception as error:
            print('Error recargarProducto: %s' % str(error))

    @staticmethod
    def buscarProducto():
        """

        Módulo para buscar un producto concreto en la tabla de productos.

        :return: None
        :rtype: None

        Recoge el nombre del producto del formulario de producto y lo busca en la base de datos para luego pasarselo al
        modulo que carga la tabla de productos.

        """
        try:
            producto = var.ui.editProducto.text()
            productos = ConexionProducto.buscarProductoDB(producto)
            EventosProducto.cargarTablaProductos(productos)
        except Exception as error:
            print('Error buscarProducto: %s' % str(error))

    @staticmethod
    def altaProducto():
        """

        Módulo que da de alta un producto.

        :return: None
        :rtype: None

        Recoge los datos del formulario de producto y los vuelca en un objeto producto y lo envia al metodo de alta en
        la base de datos.

        Tambien da un mensaje de error en una ventana de dialogo en caso de que ya exista en la base de datos, falten
        datos, o da un mensaje de confirmacion en la status bar.

        """
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
        """

        Módulo que da de baja un producto.

        :return: None
        :rtype: None

        Recoge el nombre del producto del formulario de producto y lo envia al metodo de baja en la base de datos
        pidiendo antes confirmacion.

        Tambien da un mensaje de error en una ventana de dialogo en caso de que no haya nombre de producto en el edit
        text de nombre de producto, no existe ningun producto con ese nombre o no fue posible darlo de baja.

        """
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
        """

        Módulo que modifica los datos de un producto.

        :return: None
        :rtype: None

        Recoge el nombre del producto del formulario de producto y lo envia al metodo de modificar datos en la base de
        datos pidiendo antes confirmacion.

        Tambien da un mensaje de error en una ventana de dialogo en caso de que no haya nombre de producto en el edit
        text de nombre de producto, no existe ningun producto con ese nombre o no fue posible modificar sus datos.

        """
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
    def buscarProductoDB(producto=''):
        """

        Módulo busca en la base de datos un cliente o todos los clientes.

        :param producto: Nombre del producto a buscar, si no se recibe ningun nombre o esta vacio devuelve la lista de todos los productos
        :type producto: str

        :return: Devuelve una lista con todos los productos o el producto cuyo nombre recibe como parametro
        :rtype: tuple

        En caso de que el parametro contenga una cadena que no este vacia busca en la BD un producto cuyo nombre
        recibe en parametros, si no se le pasa ninguno o la cadena esta vacia devolvera una lista con todos
        los productos.

        """
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
        """

        Módulo que da de alta un producto en la BD.

        :param producto: Objeto de tipo Producto para darlo de alta
        :type producto: Producto

        :return: Devuelve el resultado de la ejecucion de la sentensia sql
        :rtype: bool

        Da de alta un producto en la base de datos.

        """
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
        """

        Módulo da de baja un producto en la BD.

        :param producto: Nombre del producto a dar de baja
        :type producto: str

        :return: Devuelve el resultado de la ejecucion de la sentensia sql
        :rtype: bool

        Elimina de la base de datos el producto con el nombre que recibe como parametro.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from productos where producto = :producto')
            query.bindValue(':producto', producto)

            return query.exec_()

        except Exception as error:
            print('Error bajaProducto: %s' % str(error))

    @staticmethod
    def modificarProductoDB(producto):
        """

        Módulo modifica los datos de un producto en la BD.

        :param producto: Objeto de tipo Producto con los nuevos datos
        :type producto: Producto

        :return: Devuelve el resultado de la ejecucion de la sentensia sql
        :rtype: bool

        Actualiza la informacion del producto en la base de datos.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update productos set stock=:stock, precio=:precio where producto = :producto')

            query.bindValue(':producto', producto.producto)
            query.bindValue(':stock', producto.stock)
            query.bindValue(':precio', producto.precio)

            return query.exec_()

        except Exception as error:
            print('Error modificarProducto: %s' % str(error))
