import os
from datetime import datetime
from reportlab.lib import pagesizes
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.rl_settings import defaultPageSize


class Informes():

    @staticmethod
    def cabecera(c):
        logo = '.\\img\logo.png'

        c.setTitle('INFORMES')
        c.setAuthor('Administracion')
        c.setFont('Helvetica', size=10)

        c.line(45, 820, 525, 820)
        c.line(45, 745, 525, 745)

        textcif = 'CIF: A00000000H'
        textnom = 'FERRETERIA MARQUEZ, S.L.'
        textdir = 'Avenida Galicia, 101 - Vigo'
        texttlfo = '986 33 22 11'

        c.drawImage(logo, 450, 752)
        c.drawString(50, 800, textcif)
        c.drawString(50, 785, textnom)
        c.drawString(50, 770, textdir)
        c.drawString(50, 755, texttlfo)

    @staticmethod
    def pie(c, textlistado):

        fecha = datetime.today()
        fecha = fecha.strftime('%d/%m/%Y - %H:%M:%S')
        c.setFont('Helvetica-Oblique', size=7)

        c.line(50, 50, 525, 50)
        c.drawString(460, 30, str(fecha))
        c.drawString(275, 30, str('Pagina %s' % c.getPageNumber()))
        c.drawString(50, 30, str(textlistado))

    @staticmethod
    def informeClientes():
        try:
            c = canvas.Canvas('informes/listadoclientes.pdf')
            Informes.cabecera(c)
            Informes.cuerpoClientes(c)
            Informes.pie(c, 'LISTADO CLIENTES')
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

        PAGE_WIDTH = defaultPageSize[0]
        PAGE_HEIGHT = defaultPageSize[1]

        print(defaultPageSize)

        c.setFont('Helvetica-Bold', size=9)

        #c.drawString(255, 734, 'LISTADO CLIENTES')
        x = 200
        Informes.drawCenter(c, x, 734, 'LISTADO CLIENTES')
        c.line(45, 729, 525, 729)

        c.drawString(70, 710, 'DNI')
        c.drawString(160, 710, 'APELLIDOS')
        c.drawString(270, 710, 'NOMBRE')
        c.drawString(360, 710, 'PROVINCIA')
        c.drawString(450, 710, 'FECHA ALTA')

        i = 55
        j = 690

        c.drawString(i, j, '54230060Q')
        c.drawString(i+90, j, 'Marquez Gutierrez')
        c.drawString(i+220, j, 'Miguel')
        c.drawString(i+405, j, '22/5/2020')



    @staticmethod
    def drawCenter(c, x, y, text):
        text_width = stringWidth(text, 'Helvetica-Bold', 9)
        print(text_width)
        c.drawString(x - (text_width/2), y, text)
