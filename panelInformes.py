import os
import panelCliente
import panelProducto

from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class Informes():

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
    def pie(c, textlistado):
        fecha = datetime.today()
        fecha = fecha.strftime('%d/%m/%Y - %H:%M:%S')

        c.setFont('Helvetica-Oblique', size=7)

        Informes.drawLine(c, 50)
        c.drawString(65, 30, str(textlistado))
        c.drawCentredString(A4[0] / 2, 30, str('Pagina %s' % c.getPageNumber()))
        c.drawRightString(A4[0] - 65, 30, str(fecha))

    @staticmethod
    def informeClientes():
        try:
            c = canvas.Canvas('informes/listadoclientes.pdf')

            Informes.basePaginaClientes(c, 'LISTADO CLIENTES')
            clientes = panelCliente.ConexionCliente.listarClientes()

            index=0
            i = 80
            j = 680
            for cliente in clientes:
                if index == 35:
                    c.showPage()
                    Informes.basePaginaClientes(c, 'LISTADO CLIENTES')
                    j = 680
                    index=0

                c.setFont('Helvetica', size=9)
                c.drawCentredString(i + 10, j, cliente.dni)
                c.drawString(i + 65, j, cliente.apellidos)
                c.drawString(i + 190, j, cliente.nombre)
                c.drawCentredString(i + 320, j, cliente.provincia)
                c.drawCentredString(i + 420, j, cliente.fechaAlta)

                j -= 18
                index+=1


            c.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error: %s ' % str(error))

    @staticmethod
    def informeProductos():
        try:
            c = canvas.Canvas('informes/listadoproductos.pdf')

            Informes.basePaginaClientes(c, 'LISTADO PRODUCTOS')
            productos = panelProducto.ConexionProducto.listarProductos()

            index = 0
            i = 80
            j = 680
            for producto in productos:
                if index == 35:
                    c.showPage()
                    Informes.basePaginaClientes(c, 'LISTADO PRODUCTOS')
                    j = 680
                    index = 0

                c.setFont('Helvetica', size=9)
                c.drawCentredString(i, j, str(producto.codigoProducto))
                c.drawString(i + 50, j, producto.producto)
                c.drawCentredString(i + 320, j, str(producto.stock))
                c.drawCentredString(i + 420, j, str(producto.precio))

                j -= 18
                index += 1

            c.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error: %s ' % str(error))

    @staticmethod
    def drawLine(c, y):
        c.line(45, y, A4[0] - 45, y)

    @staticmethod
    def basePaginaClientes(c, textlistado):
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
    def basePaginaProductos(c, textlistado):
        Informes.cabecera(c, textlistado)
        c.setFont('Helvetica-Bold', size=9)
        c.drawCentredString(80, 710, 'DNI')
        c.drawCentredString(190, 710, 'APELLIDOS')
        c.drawCentredString(310, 710, 'NOMBRE')
        c.drawCentredString(400, 710, 'PROVINCIA')
        c.drawCentredString(500, 710, 'FECHA ALTA')
        Informes.drawLine(c, 697)
        Informes.pie(c, textlistado)
