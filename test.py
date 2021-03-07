import unittest

import cCliente
import var
import ventanaPrincipal
from cProducto import Producto, ConexionProducto


class MyTestCase(unittest.TestCase):

    def test_conexion(self):
        value = ventanaPrincipal.Conexion.conectardb(var.filedb)
        msg = 'Conexión no válida'
        self.assertTrue(value, msg)

    def test_dni(self):
        dni = '00000000T'
        value = cCliente.Cliente.comprobarDNIValido(dni)
        msg = 'Proba DNI Errónea'
        self.assertTrue(value, msg)

    def test_actualizar_producto(self):
        resultado = False
        ventanaPrincipal.Conexion.conectardb(var.filedb)

        producto = Producto()
        producto.producto = "Martillo"
        producto.precio = 21
        producto.stock = 60

        resultado = ConexionProducto.modificarProductoDB(producto)
        msg = 'Prueba alta producto erronea'
        self.assertTrue(resultado, msg)

