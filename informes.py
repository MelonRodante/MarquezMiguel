import os
from datetime import datetime
from reportlab.lib import pagesizes
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus import PageBreak
from reportlab.rl_settings import defaultPageSize

import conexion
import var


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
        c.drawString(50, 30, str(textlistado))
        c.drawCentredString(A4[0] / 2, 30, str('Pagina %s' % c.getPageNumber()))
        c.drawRightString(A4[0] - 50, 30, str(fecha))

    @staticmethod
    def informeClientes():
        try:
            c = canvas.Canvas('informes/listadoclientes.pdf')

            Informes.basePaginaClientes(c, 'LISTADO CLIENTES')
            clientes = conexion.ConexionCliente.listarClientes()

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
                c.drawCentredString(i, j, cliente.dni)
                c.drawString(i + 50, j, cliente.apellidos)
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
    def cuerpoClientes(c):



        c.showPage()

        for cliente in clientes:
            c.drawCentredString(i, j, cliente.dni)
            c.drawString(i + 50, j, cliente.apellidos)
            c.drawString(i + 190, j, cliente.nombre)
            c.drawCentredString(i + 320, j, cliente.provincia)
            c.drawCentredString(i + 420, j, cliente.fechaAlta)
            j-=18

        '''c.drawCentredString(i, j, '54230060Q')
        c.drawString(i + 50, j, 'Dominguez Martin Farre')
        c.drawString(i + 190, j, 'Eva Katerina')
        c.drawCentredString(i + 320, j, 'Lugo')
        c.drawCentredString(i + 420, j, '5/5/2020')

        c.drawCentredString(i, j-18, '54230060Q')
        c.drawString(i + 50, j-18, 'Marquez Gutierrez')
        c.drawString(i + 190, j-18, 'Miguel')
        c.drawCentredString(i + 320, j-18, 'Pontevedra')
        c.drawCentredString(i + 420, j-18, '22/5/2020')

        c.drawCentredString(i, j-36, '54230060Q')
        c.drawString(i + 50, j-36, 'Dominguez Martin Farre')
        c.drawString(i + 190, j-36, 'Eva Katerina')
        c.drawCentredString(i + 320, j-36, 'Lugo')
        c.drawCentredString(i + 420, j-36, '5/5/2020')'''

    @staticmethod
    def drawLine(c, y):
        c.line(45, y, A4[0] - 45, y)

    @staticmethod
    def basePaginaClientes(c, textlistado):
        Informes.cabecera(c, textlistado)
        c.setFont('Helvetica-Bold', size=9)
        c.drawCentredString(80, 710, 'DNI')
        c.drawCentredString(190, 710, 'APELLIDOS')
        c.drawCentredString(310, 710, 'NOMBRE')
        c.drawCentredString(400, 710, 'PROVINCIA')
        c.drawCentredString(500, 710, 'FECHA ALTA')
        Informes.drawLine(c, 697)
        Informes.pie(c, textlistado)
