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
import ventanasDialogo


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

        var.ui.actionFacturas_cliente.triggered.connect(Informes.informeFacturasCliente)

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
        c.setFont('Helvetica-Bold', size=10)
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
        Informes.pie(c, textlistado)

    @staticmethod
    def informeClientes():
        try:
            filename = '.\\informes/listado-clientes.pdf'
            c = canvas.Canvas(filename)

            Informes.encabezadoPaginaCliente(c)
            clientes = cCliente.ConexionCliente.buscarClienteDB()

            index = 0
            datos = [['DNI', 'APELLIDOS', 'NOMBRE', 'PROVINCIA', 'FECHA ALTA']]

            ts = TableStyle([
                ('FONTNAME', (0, 0), (4, 0), 'Helvetica-Bold'),
                ('ALIGN', (0, 0), (4, 0), 'CENTER'),
                ('LINEBELOW', (0, 0), (4, 0), 1, colors.black),
                ('ALIGN', (0, 1), (0, -1), 'CENTER'),
                ('ALIGN', (3, 1), (4, -1), 'CENTER')
            ])

            for cliente in clientes:
                index += 1
                if index == 37:
                    index = 0
                    tabla = Table(datos, colWidths=[65, 145, 100, 105, 80])
                    tabla.setStyle(ts)
                    tabla.wrapOn(c, 700, 50)
                    tabla.drawOn(c, 50, 730 - (len(datos) * 18))
                    datos = [['DNI', 'APELLIDOS', 'NOMBRE', 'PROVINCIA', 'FECHA ALTA']]
                    c.showPage()
                    Informes.encabezadoPaginaCliente(c)

                datos.append([cliente.dni,
                              cliente.apellidos,
                              cliente.nombre,
                              cliente.provincia,
                              cliente.fechaAlta])

            tabla = Table(datos, colWidths=[65, 145, 100, 105, 80])
            tabla.setStyle(ts)
            tabla.wrapOn(c, 700, 50)
            tabla.drawOn(c, 50, 730 - (len(datos) * 18))

            c.save()
            os.startfile(filename)

        except Exception as error:
            print('Error informeClientes: %s ' % str(error))

    @staticmethod
    def encabezadoPaginaProductos(c):
        textlistado = "LISTADO PRODUCTOS"
        Informes.cabecera(c, textlistado)
        Informes.pie(c, textlistado)

    @staticmethod
    def informeProductos():
        try:
            filename = '.\\informes/listado-productos.pdf'
            c = canvas.Canvas(filename)

            Informes.encabezadoPaginaProductos(c)
            productos = cProducto.ConexionProducto.buscarProductoDB()

            index = 0
            datos = [['CODIGO', 'PRODUCTO', 'STOCK', 'PRECIO']]

            ts = TableStyle([
                ('FONTNAME', (0, 0), (3, 0), 'Helvetica-Bold'),
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('LINEBELOW', (0, 0), (3, 0), 1, colors.black),
                ('ALIGN', (0, 1), (0, -1), 'CENTER'),
                ('ALIGN', (2, 1), (2, -1), 'CENTER'),
                ('ALIGN', (3, 1), (3, -1), 'RIGHT')
            ])

            for producto in productos:
                index += 1
                if index == 37:
                    index = 0
                    tabla = Table(datos, colWidths=[80, 255, 80, 80])
                    tabla.setStyle(ts)
                    tabla.wrapOn(c, 700, 50)
                    tabla.drawOn(c, 50, 730 - (len(datos) * 18))
                    datos = [['CODIGO', 'PRODUCTO', 'STOCK', 'PRECIO']]
                    c.showPage()
                    Informes.encabezadoPaginaCliente(c)

                datos.append([str(producto.codigoProducto),
                              producto.producto,
                              str(producto.stock),
                              "{:,.2f} €   ".format(producto.precio)])

            tabla = Table(datos, colWidths=[80, 255, 80, 80])
            tabla.setStyle(ts)
            tabla.wrapOn(c, 700, 50)
            tabla.drawOn(c, 50, 730 - (len(datos) * 18))

            c.save()
            os.startfile(filename)

        except Exception as error:
            print('Error informeProductos: %s ' % str(error))

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

            if var.ui.editNFactura.text():

                fac = cFactura.Factura()
                fac.nfactura = var.ui.editNFactura.text()
                factura = cFactura.ConexionFactura.buscarFacturaDB(fac)[0]
                ventas = cFactura.ConexionVenta.buscarVentaDB(fac.nfactura)

                if len(ventas) > 0:
                    filename = '.\\informes/factura-' + str(factura.nfactura) + '.pdf'
                    c = canvas.Canvas(filename)

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
                        datos.append([str(venta.unidades),
                                      venta.producto,
                                      "{:,.2f} €".format(venta.precio),
                                      "{:,.2f} €".format(venta.precio * venta.unidades)])
                        subtotal += (venta.precio * venta.unidades)

                    tabla = Table(datos, colWidths=[70, 285, 70, 70])
                    tabla.setStyle(ts)
                    tabla.wrapOn(c, 700, 50)
                    tabla.drawOn(c, 50, 690 - (len(datos) * 18))

                    datos = [['SUBTOTAL', 'IMPUESTOS(21%)', 'TOTAL'],
                             ["{:,.2f} €".format(subtotal), "{:,.2f} €".format(subtotal * 0.21),
                              "{:,.2f} €".format(subtotal * 1.21)]]
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
                    os.startfile(filename)
                else:
                    ventanasDialogo.EventosVentanas.abrirDialogAviso("No es posible imprimir una factura vacia")

            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso("Seleccione una factura para imprimir")


        except Exception as error:
            print('Error informeFactura: %s ' % str(error))

    @staticmethod
    def paginaBaseFacturasCliente(c, factura):
        Informes.cabecera(c, "FACTURAS DE CLIENTE")

        c.setFont('Helvetica-Bold', size=9)
        c.drawString(50, 710, "DNI:")
        c.drawString(150, 710, "Cliente:")

        c.setFont('Helvetica', size=9)
        c.drawString(72, 710, factura.dni)
        c.drawString(187, 710, factura.cliente)

        Informes.drawLine(c, 697)
        Informes.drawLine(c, 105)

        Informes.pie(c, "FACTURAS CLIENTE")

    @staticmethod
    def informeFacturasCliente():
        try:

            if var.ui.editDNIFacturacion.text():

                factura = cFactura.Factura()
                factura.dni = var.ui.editDNIFacturacion.text()
                factura.cliente = var.ui.editApellidosNombreFacturacion.text()
                facturas = cFactura.ConexionFactura.buscarFacturaDB(factura)

                filename = '.\\informes/facturas-' + factura.dni + '.pdf'
                c = canvas.Canvas(filename)

                Informes.paginaBaseFacturasCliente(c, factura)

                index = 0
                subtotal_factura = 0
                subtotal_total = 0
                datos = [['Nº FACTURA', 'ESTADO', 'FECHA', 'SUBTOTAL']]

                ts = TableStyle([
                    ('FONTNAME', (0, 0), (3, 0), 'Helvetica-Bold'),
                    ('BACKGROUND', (0, 0), (3, 0), HexColor(0xC6CDFF)),
                    ('ALIGN', (0, 0), (3, 0), 'CENTER'),

                    ('ALIGN', (0, 1), (0, -1), 'CENTER'),
                    ('ALIGN', (2, 1), (2, -1), 'CENTER'),
                    ('ALIGN', (3, 1), (3, -1), 'RIGHT'),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
                ])


                for factura in facturas:
                    index += 1
                    if index == 32:
                        index = 0
                        tabla = Table(datos, colWidths=[70, 255, 70, 100])
                        tabla.setStyle(ts)
                        tabla.wrapOn(c, 700, 50)
                        tabla.drawOn(c, 50, 690 - (len(datos) * 18))
                        datos = [['Nº FACTURA', 'ESTADO', 'FECHA', 'SUBTOTAL']]
                        c.showPage()
                        Informes.paginaBaseFactura(c, factura)

                    subtotal_factura = Informes.calcularSubtotalFactura(factura.nfactura)
                    subtotal_total += subtotal_factura
                    datos.append([str(factura.nfactura), factura.estado, factura.fechafactura, "{:,.2f} €".format(subtotal_factura)])

                tabla = Table(datos, colWidths=[80, 215, 100, 100])
                tabla.setStyle(ts)
                tabla.wrapOn(c, 700, 50)
                tabla.drawOn(c, 50, 690 - (len(datos) * 18))

                datos = [['SUBTOTAL', 'IMPUESTOS(21%)', 'TOTAL'],
                         ["{:,.2f} €".format(subtotal_total), "{:,.2f} €".format(subtotal_total * 0.21), "{:,.2f} €".format(subtotal_total * 1.21)]]
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
                os.startfile(filename)

            else:
                ventanasDialogo.EventosVentanas.abrirDialogAviso("Seleccione un cliente en facturacion para imprimir sus facturas")

        except Exception as error:
            print('Error informeFacturasCliente: %s ' % str(error))

    @staticmethod
    def calcularSubtotalFactura(nfactura):
        subtotal = 0
        ventas = cFactura.ConexionVenta.buscarVentaDB(nfactura)
        for venta in ventas:
            subtotal += venta.precio * venta.unidades
        return subtotal
