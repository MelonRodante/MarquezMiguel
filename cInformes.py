import os

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.platypus import Table, TableStyle

import cCliente
import cFactura
import cProducto

from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

import var


class Informes:

    @staticmethod
    def conectarEventosFactura():
        """

        Módulo que conecta los eventos de los informes.

        :return: None
        :rtype: None

        Llama a la conexion con todos los eventos relacionados con los informes.

        """
        var.ui.actionInforme_Clientes.triggered.connect(Informes.informeClientes)

        var.ui.actionInforme_Productos.triggered.connect(Informes.informeProductos)

        var.ui.actionImprimir_factura.triggered.connect(Informes.informeFactura)

    @staticmethod
    def cabecera(c, textlistado):
        logo = '.\\img\logo.png'

        c.setTitle('INFORMES')
        c.setAuthor('Administracion')

        textcif = 'CIF: A00000000H'
        textnom = 'FERRETERIA MARQUEZ, S.L.'
        textdir = 'Avenida Galicia, 101 - Vigo'
        texttlfo = '986 33 22 11'

        c.setFont('Helvetica', size=10)

        Informes.drawLine(c, 820)

        c.drawImage(logo, 450, 752)
        c.drawString(50, 800, textcif)
        c.drawString(50, 785, textnom)
        c.drawString(50, 770, textdir)
        c.drawString(50, 755, texttlfo)

        Informes.drawLine(c, 745)
        c.drawCentredString(A4[0] / 2, 734, textlistado)
        Informes.drawLine(c, 730)

    @staticmethod
    def drawLine(c, y):
        c.line(45, y, A4[0] - 45, y)

    @staticmethod
    def pie(c, textlistado):
        fecha = datetime.today()
        fecha = fecha.strftime('%d/%m/%Y - %H:%M:%S')

        c.setFont('Helvetica-Oblique', size=7)

        Informes.drawLine(c, 50)
        c.drawString(65, 30, str(textlistado))
        c.drawCentredString(A4[0] / 2, 30, str('Pagina %s' % c.getPageNumber()))
        c.drawRightString(A4[0] - 65, 30, str(fecha))

    @staticmethod
    def encabezadoPaginaCliente(c):
        textlistado = "LISTADO CLIENTES"
        Informes.cabecera(c, textlistado)
        c.setFont('Helvetica-Bold', size=9)
        c.drawCentredString(90, 710, 'DNI')
        c.drawCentredString(180, 710, 'APELLIDOS')
        c.drawCentredString(295, 710, 'NOMBRE')
        c.drawCentredString(400, 710, 'PROVINCIA')
        c.drawCentredString(500, 710, 'FECHA ALTA')
        Informes.drawLine(c, 697)
        Informes.pie(c, textlistado)

    @staticmethod
    def informeClientes():
        try:
            c = canvas.Canvas('informes/listado-clientes.pdf')

            Informes.encabezadoPaginaCliente(c)
            clientes = cCliente.ConexionCliente.buscarClienteDB()

            index = 0
            i = 80
            j = 680

            for cliente in clientes:
                if index == 35:
                    c.showPage()
                    Informes.encabezadoPaginaCliente(c)
                    j = 680
                    index = 0

                c.setFont('Helvetica', size=9)
                c.drawCentredString(i + 10, j, cliente.dni)
                c.drawString(i + 65, j, cliente.apellidos)
                c.drawString(i + 190, j, cliente.nombre)
                c.drawCentredString(i + 320, j, cliente.provincia)
                c.drawCentredString(i + 420, j, cliente.fechaAlta)

                j -= 18
                index += 1


            c.save()
            rootPath = ".\\informes"
            for file in os.listdir(rootPath):
                if file.endswith('informes/listado-clientes.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))

        except Exception as error:
            print('Error: %s ' % str(error))

    @staticmethod
    def encabezadoPaginaProductos(c):
        textlistado = "LISTADO PRODUCTOS"
        Informes.cabecera(c, textlistado)
        c.setFont('Helvetica-Bold', size=9)
        c.drawCentredString(80, 710, 'CODIGO')
        c.drawCentredString(240, 710, 'PRODUCTO')
        c.drawCentredString(400, 710, 'STOCK')
        c.drawCentredString(500, 710, 'PRECIO')
        Informes.drawLine(c, 697)
        Informes.pie(c, textlistado)

    @staticmethod
    def informeProductos():
        try:
            c = canvas.Canvas('informes/listado-productos.pdf')

            Informes.encabezadoPaginaProductos(c)
            productos = cProducto.ConexionProducto.buscarProductoDB()

            index = 0
            i = 80
            j = 680

            for producto in productos:
                if index == 35:
                    c.showPage()
                    Informes.encabezadoPaginaProductos(c)
                    j = 680
                    index = 0

                c.setFont('Helvetica', size=9)
                c.drawCentredString(i, j, str(producto.codigoProducto))
                c.drawString(i + 50, j, producto.producto)
                c.drawCentredString(i + 320, j, str(producto.stock))
                c.drawRightString(i + 445, j, "{:,.2f} €".format(producto.precio))

                j -= 18
                index += 1

            c.save()
            rootPath = ".\\informes"

            for file in os.listdir(rootPath):
                if file.endswith('listado-productos.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))

        except Exception as error:
            print('Error: %s ' % str(error))

    @staticmethod
    def paginaBaseFactura(c, factura):
        Informes.cabecera(c, "FACTURA")

        c.setFont('Helvetica-Bold', size=9)
        c.drawString(50, 710, "DNI:")
        c.drawString(150, 710, "Cliente:")
        c.drawString(435, 710, "Fecha factura:")

        c.setFont('Helvetica', size=9)
        c.drawString(72, 710, factura.dni)
        c.drawString(187, 710, factura.cliente)
        c.drawString(500, 710, factura.fechafactura)

        Informes.drawLine(c, 697)

        Informes.drawLine(c, 105)

        Informes.pie(c, "FACTURA")

    @staticmethod
    def informeFactura():
        try:

            c = canvas.Canvas('informes/listado-productos.pdf')

            fac = cFactura.Factura()
            fac.nfactura = var.ui.editNFactura.text()
            factura = cFactura.ConexionFactura.buscarFacturaDB(fac)[0]
            ventas = cFactura.ConexionVenta.buscarVentaDB(fac.nfactura)

            Informes.paginaBaseFactura(c, factura)

            index = 0
            subtotal = 0
            datos = [['UNIDADES', 'PRODUCTO', 'PRECIO', 'SUBTOTAL']]

            ts = TableStyle([
                ('FONTNAME', (0, 0), (3, 0), 'Helvetica-Bold'),
                ('BACKGROUND', (0, 0), (3, 0), HexColor(0xC6CDFF)),
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('ALIGN', (0, 1), (0, -1), 'RIGHT'),
                ('ALIGN', (2, 1), (-1, -1), 'RIGHT'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ])

            for venta in ventas:
                index += 1
                if index == 32:
                    index = 0
                    tabla = Table(datos, colWidths=[70, 285, 70, 70])
                    tabla.setStyle(ts)
                    tabla.wrapOn(c, 700, 50)
                    tabla.drawOn(c, 50, 690 - (len(datos) * 18))
                    datos = [['UNIDADES', 'PRODUCTO', 'PRECIO', 'SUBTOTAL']]
                    c.showPage()
                    Informes.paginaBaseFactura(c, factura)
                datos.append([str(venta.unidades), venta.producto, "{:,.2f} €".format(venta.precio), "{:,.2f} €".format(venta.precio * venta.unidades)])
                subtotal += (venta.precio * venta.unidades)

            tabla = Table(datos, colWidths=[70, 285, 70, 70])
            tabla.setStyle(ts)
            tabla.wrapOn(c, 700, 50)
            tabla.drawOn(c, 50, 690 - (len(datos) * 18))

            datos = [['SUBTOTAL', 'IMPUESTOS(21%)', 'TOTAL'], ["{:,.2f} €".format(subtotal), "{:,.2f} €".format(subtotal * 0.21), "{:,.2f} €".format(subtotal * 1.21)]]
            ts = TableStyle([
                ('FONTNAME', (0, 0), (3, 0), 'Helvetica-Bold'),
                ('BACKGROUND', (0, 0), (3, 0), HexColor(0xC6CDFF)),
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('ALIGN', (0, 1), (-1, -1), 'RIGHT'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ])
            tabla = Table(datos, colWidths=[165, 165, 165])
            tabla.setStyle(ts)
            tabla.wrapOn(c, 700, 50)
            tabla.drawOn(c, 50, 60)

            c.save()
            rootPath = ".\\informes"

            for file in os.listdir(rootPath):
                if file.endswith('listado-productos.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))

        except Exception as error:
            print('Error: %s ' % str(error))
