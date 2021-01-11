# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'venPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_venPrincipal(object):
    def setupUi(self, venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.resize(800, 600)
        venPrincipal.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(venPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.panel = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.panel.setFont(font)
        self.panel.setObjectName("panel")
        self.panelCliente = QtWidgets.QWidget()
        self.panelCliente.setObjectName("panelCliente")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.panelCliente)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout1 = QtWidgets.QHBoxLayout()
        self.layout1.setObjectName("layout1")
        self.lblDNI = QtWidgets.QLabel(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDNI.sizePolicy().hasHeightForWidth())
        self.lblDNI.setSizePolicy(sizePolicy)
        self.lblDNI.setMinimumSize(QtCore.QSize(60, 25))
        self.lblDNI.setMaximumSize(QtCore.QSize(60, 25))
        self.lblDNI.setObjectName("lblDNI")
        self.layout1.addWidget(self.lblDNI)
        self.editDNI = QtWidgets.QLineEdit(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editDNI.sizePolicy().hasHeightForWidth())
        self.editDNI.setSizePolicy(sizePolicy)
        self.editDNI.setMinimumSize(QtCore.QSize(90, 20))
        self.editDNI.setMaximumSize(QtCore.QSize(90, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.editDNI.setFont(font)
        self.editDNI.setText("")
        self.editDNI.setMaxLength(9)
        self.editDNI.setObjectName("editDNI")
        self.layout1.addWidget(self.editDNI)
        self.lblValido = QtWidgets.QLabel(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblValido.sizePolicy().hasHeightForWidth())
        self.lblValido.setSizePolicy(sizePolicy)
        self.lblValido.setMinimumSize(QtCore.QSize(25, 25))
        self.lblValido.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.lblValido.setFont(font)
        self.lblValido.setText("")
        self.lblValido.setObjectName("lblValido")
        self.layout1.addWidget(self.lblValido)
        self.btnBuscar = QtWidgets.QPushButton(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(32)
        sizePolicy.setVerticalStretch(32)
        sizePolicy.setHeightForWidth(self.btnBuscar.sizePolicy().hasHeightForWidth())
        self.btnBuscar.setSizePolicy(sizePolicy)
        self.btnBuscar.setMinimumSize(QtCore.QSize(32, 32))
        self.btnBuscar.setMaximumSize(QtCore.QSize(32, 32))
        self.btnBuscar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/lupa/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon)
        self.btnBuscar.setIconSize(QtCore.QSize(24, 24))
        self.btnBuscar.setObjectName("btnBuscar")
        self.layout1.addWidget(self.btnBuscar)
        self.btnRecargar = QtWidgets.QPushButton(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(32)
        sizePolicy.setVerticalStretch(32)
        sizePolicy.setHeightForWidth(self.btnRecargar.sizePolicy().hasHeightForWidth())
        self.btnRecargar.setSizePolicy(sizePolicy)
        self.btnRecargar.setMinimumSize(QtCore.QSize(32, 32))
        self.btnRecargar.setMaximumSize(QtCore.QSize(32, 32))
        self.btnRecargar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/recargar/recargar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRecargar.setIcon(icon1)
        self.btnRecargar.setIconSize(QtCore.QSize(24, 24))
        self.btnRecargar.setObjectName("btnRecargar")
        self.layout1.addWidget(self.btnRecargar)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout1.addItem(spacerItem)
        self.lblFechaAlta = QtWidgets.QLabel(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblFechaAlta.sizePolicy().hasHeightForWidth())
        self.lblFechaAlta.setSizePolicy(sizePolicy)
        self.lblFechaAlta.setMinimumSize(QtCore.QSize(90, 25))
        self.lblFechaAlta.setMaximumSize(QtCore.QSize(90, 25))
        self.lblFechaAlta.setObjectName("lblFechaAlta")
        self.layout1.addWidget(self.lblFechaAlta)
        self.editFechaAlta = QtWidgets.QLineEdit(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editFechaAlta.sizePolicy().hasHeightForWidth())
        self.editFechaAlta.setSizePolicy(sizePolicy)
        self.editFechaAlta.setMinimumSize(QtCore.QSize(90, 20))
        self.editFechaAlta.setMaximumSize(QtCore.QSize(90, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.editFechaAlta.setFont(font)
        self.editFechaAlta.setText("")
        self.editFechaAlta.setAlignment(QtCore.Qt.AlignCenter)
        self.editFechaAlta.setReadOnly(True)
        self.editFechaAlta.setObjectName("editFechaAlta")
        self.layout1.addWidget(self.editFechaAlta)
        self.btnCalendario = QtWidgets.QPushButton(self.panelCliente)
        self.btnCalendario.setMinimumSize(QtCore.QSize(32, 32))
        self.btnCalendario.setMaximumSize(QtCore.QSize(32, 32))
        self.btnCalendario.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/calendario/calendario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalendario.setIcon(icon2)
        self.btnCalendario.setIconSize(QtCore.QSize(32, 32))
        self.btnCalendario.setObjectName("btnCalendario")
        self.layout1.addWidget(self.btnCalendario)
        self.verticalLayout.addLayout(self.layout1)
        self.layout2 = QtWidgets.QHBoxLayout()
        self.layout2.setObjectName("layout2")
        self.lblApellidos = QtWidgets.QLabel(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblApellidos.sizePolicy().hasHeightForWidth())
        self.lblApellidos.setSizePolicy(sizePolicy)
        self.lblApellidos.setMinimumSize(QtCore.QSize(60, 25))
        self.lblApellidos.setMaximumSize(QtCore.QSize(60, 25))
        self.lblApellidos.setObjectName("lblApellidos")
        self.layout2.addWidget(self.lblApellidos)
        self.editApellidos = QtWidgets.QLineEdit(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editApellidos.sizePolicy().hasHeightForWidth())
        self.editApellidos.setSizePolicy(sizePolicy)
        self.editApellidos.setMinimumSize(QtCore.QSize(350, 20))
        self.editApellidos.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.editApellidos.setFont(font)
        self.editApellidos.setText("")
        self.editApellidos.setObjectName("editApellidos")
        self.layout2.addWidget(self.editApellidos)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layout2.addItem(spacerItem1)
        self.lblNombre = QtWidgets.QLabel(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNombre.sizePolicy().hasHeightForWidth())
        self.lblNombre.setSizePolicy(sizePolicy)
        self.lblNombre.setMinimumSize(QtCore.QSize(50, 25))
        self.lblNombre.setMaximumSize(QtCore.QSize(50, 25))
        self.lblNombre.setObjectName("lblNombre")
        self.layout2.addWidget(self.lblNombre)
        self.editNombre = QtWidgets.QLineEdit(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editNombre.sizePolicy().hasHeightForWidth())
        self.editNombre.setSizePolicy(sizePolicy)
        self.editNombre.setMinimumSize(QtCore.QSize(250, 20))
        self.editNombre.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.editNombre.setFont(font)
        self.editNombre.setText("")
        self.editNombre.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.editNombre.setObjectName("editNombre")
        self.layout2.addWidget(self.editNombre)
        self.verticalLayout.addLayout(self.layout2)
        self.layout3 = QtWidgets.QHBoxLayout()
        self.layout3.setObjectName("layout3")
        self.lblDireccion = QtWidgets.QLabel(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDireccion.sizePolicy().hasHeightForWidth())
        self.lblDireccion.setSizePolicy(sizePolicy)
        self.lblDireccion.setMinimumSize(QtCore.QSize(60, 25))
        self.lblDireccion.setMaximumSize(QtCore.QSize(60, 25))
        self.lblDireccion.setObjectName("lblDireccion")
        self.layout3.addWidget(self.lblDireccion)
        self.editDireccion = QtWidgets.QLineEdit(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editDireccion.sizePolicy().hasHeightForWidth())
        self.editDireccion.setSizePolicy(sizePolicy)
        self.editDireccion.setMinimumSize(QtCore.QSize(300, 20))
        self.editDireccion.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.editDireccion.setFont(font)
        self.editDireccion.setText("")
        self.editDireccion.setObjectName("editDireccion")
        self.layout3.addWidget(self.editDireccion)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layout3.addItem(spacerItem2)
        self.lblProvincia = QtWidgets.QLabel(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblProvincia.sizePolicy().hasHeightForWidth())
        self.lblProvincia.setSizePolicy(sizePolicy)
        self.lblProvincia.setMinimumSize(QtCore.QSize(60, 25))
        self.lblProvincia.setMaximumSize(QtCore.QSize(60, 25))
        self.lblProvincia.setObjectName("lblProvincia")
        self.layout3.addWidget(self.lblProvincia)
        self.cmbProvincia = QtWidgets.QComboBox(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbProvincia.sizePolicy().hasHeightForWidth())
        self.cmbProvincia.setSizePolicy(sizePolicy)
        self.cmbProvincia.setMinimumSize(QtCore.QSize(120, 20))
        self.cmbProvincia.setMaximumSize(QtCore.QSize(120, 20))
        self.cmbProvincia.setCurrentText("")
        self.cmbProvincia.setObjectName("cmbProvincia")
        self.layout3.addWidget(self.cmbProvincia)
        self.verticalLayout.addLayout(self.layout3)
        self.layout4 = QtWidgets.QHBoxLayout()
        self.layout4.setObjectName("layout4")
        self.lblSexo = QtWidgets.QLabel(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSexo.sizePolicy().hasHeightForWidth())
        self.lblSexo.setSizePolicy(sizePolicy)
        self.lblSexo.setMinimumSize(QtCore.QSize(60, 25))
        self.lblSexo.setMaximumSize(QtCore.QSize(60, 25))
        self.lblSexo.setObjectName("lblSexo")
        self.layout4.addWidget(self.lblSexo)
        self.rbtFemenino = QtWidgets.QRadioButton(self.panelCliente)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rbtFemenino.setFont(font)
        self.rbtFemenino.setObjectName("rbtFemenino")
        self.grpSexo = QtWidgets.QButtonGroup(venPrincipal)
        self.grpSexo.setObjectName("grpSexo")
        self.grpSexo.addButton(self.rbtFemenino)
        self.layout4.addWidget(self.rbtFemenino)
        self.rbtMasculino = QtWidgets.QRadioButton(self.panelCliente)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rbtMasculino.setFont(font)
        self.rbtMasculino.setObjectName("rbtMasculino")
        self.grpSexo.addButton(self.rbtMasculino)
        self.layout4.addWidget(self.rbtMasculino)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layout4.addItem(spacerItem3)
        self.lblEdad = QtWidgets.QLabel(self.panelCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblEdad.sizePolicy().hasHeightForWidth())
        self.lblEdad.setSizePolicy(sizePolicy)
        self.lblEdad.setMinimumSize(QtCore.QSize(35, 25))
        self.lblEdad.setMaximumSize(QtCore.QSize(35, 25))
        self.lblEdad.setObjectName("lblEdad")
        self.layout4.addWidget(self.lblEdad)
        self.spinEdad = QtWidgets.QSpinBox(self.panelCliente)
        self.spinEdad.setMinimum(18)
        self.spinEdad.setObjectName("spinEdad")
        self.layout4.addWidget(self.spinEdad)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layout4.addItem(spacerItem4)
        self.lblPago = QtWidgets.QLabel(self.panelCliente)
        self.lblPago.setMinimumSize(QtCore.QSize(110, 25))
        self.lblPago.setMaximumSize(QtCore.QSize(110, 25))
        self.lblPago.setObjectName("lblPago")
        self.layout4.addWidget(self.lblPago)
        self.chkTransferencia = QtWidgets.QCheckBox(self.panelCliente)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.chkTransferencia.setFont(font)
        self.chkTransferencia.setObjectName("chkTransferencia")
        self.grpPago = QtWidgets.QButtonGroup(venPrincipal)
        self.grpPago.setObjectName("grpPago")
        self.grpPago.setExclusive(False)
        self.grpPago.addButton(self.chkTransferencia)
        self.layout4.addWidget(self.chkTransferencia)
        self.chkTarjeta = QtWidgets.QCheckBox(self.panelCliente)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.chkTarjeta.setFont(font)
        self.chkTarjeta.setObjectName("chkTarjeta")
        self.grpPago.addButton(self.chkTarjeta)
        self.layout4.addWidget(self.chkTarjeta)
        self.chkEfectivo = QtWidgets.QCheckBox(self.panelCliente)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.chkEfectivo.setFont(font)
        self.chkEfectivo.setObjectName("chkEfectivo")
        self.grpPago.addButton(self.chkEfectivo)
        self.layout4.addWidget(self.chkEfectivo)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.layout4)
        self.tablaClientes = QtWidgets.QTableWidget(self.panelCliente)
        self.tablaClientes.setObjectName("tablaClientes")
        self.tablaClientes.setColumnCount(3)
        self.tablaClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaClientes.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tablaClientes)
        self.layout5 = QtWidgets.QHBoxLayout()
        self.layout5.setContentsMargins(-1, -1, -1, 0)
        self.layout5.setObjectName("layout5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout5.addItem(spacerItem6)
        self.btnClienteAlta = QtWidgets.QPushButton(self.panelCliente)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnClienteAlta.setFont(font)
        self.btnClienteAlta.setObjectName("btnClienteAlta")
        self.layout5.addWidget(self.btnClienteAlta)
        self.btnClienteModificar = QtWidgets.QPushButton(self.panelCliente)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnClienteModificar.setFont(font)
        self.btnClienteModificar.setObjectName("btnClienteModificar")
        self.layout5.addWidget(self.btnClienteModificar)
        self.btnClienteBaja = QtWidgets.QPushButton(self.panelCliente)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnClienteBaja.setFont(font)
        self.btnClienteBaja.setObjectName("btnClienteBaja")
        self.layout5.addWidget(self.btnClienteBaja)
        self.btnClienteLimpiar = QtWidgets.QPushButton(self.panelCliente)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnClienteLimpiar.setFont(font)
        self.btnClienteLimpiar.setObjectName("btnClienteLimpiar")
        self.layout5.addWidget(self.btnClienteLimpiar)
        self.btnClienteSalir = QtWidgets.QPushButton(self.panelCliente)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnClienteSalir.setFont(font)
        self.btnClienteSalir.setObjectName("btnClienteSalir")
        self.layout5.addWidget(self.btnClienteSalir)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout5.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.layout5)
        self.panel.addTab(self.panelCliente, "")
        self.panelFacturacion = QtWidgets.QWidget()
        self.panelFacturacion.setObjectName("panelFacturacion")
        self.panel.addTab(self.panelFacturacion, "")
        self.panelProductos = QtWidgets.QWidget()
        self.panelProductos.setObjectName("panelProductos")
        self.panel.addTab(self.panelProductos, "")
        self.verticalLayout_2.addWidget(self.panel)
        venPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(venPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        venPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(venPrincipal)
        self.statusbar.setObjectName("statusbar")
        venPrincipal.setStatusBar(self.statusbar)
        self.actionAbrir = QtWidgets.QAction(venPrincipal)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionImprimir = QtWidgets.QAction(venPrincipal)
        self.actionImprimir.setObjectName("actionImprimir")
        self.actionSalir = QtWidgets.QAction(venPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionImprimir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(venPrincipal)
        self.panel.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(venPrincipal)

    def retranslateUi(self, venPrincipal):
        _translate = QtCore.QCoreApplication.translate
        venPrincipal.setWindowTitle(_translate("venPrincipal", "Gestion Miguel Marquez"))
        self.lblDNI.setText(_translate("venPrincipal", "DNI:"))
        self.lblFechaAlta.setText(_translate("venPrincipal", "Fecha de Alta:"))
        self.lblApellidos.setText(_translate("venPrincipal", "Apellidos:"))
        self.lblNombre.setText(_translate("venPrincipal", "Nombre:"))
        self.lblDireccion.setText(_translate("venPrincipal", "Direccion:"))
        self.lblProvincia.setText(_translate("venPrincipal", "Provincia:"))
        self.lblSexo.setText(_translate("venPrincipal", "Sexo:"))
        self.rbtFemenino.setText(_translate("venPrincipal", "Femenino"))
        self.rbtMasculino.setText(_translate("venPrincipal", "Masculino"))
        self.lblEdad.setText(_translate("venPrincipal", "Edad:"))
        self.lblPago.setText(_translate("venPrincipal", "Metodos de Pago:"))
        self.chkTransferencia.setText(_translate("venPrincipal", "Transferencia"))
        self.chkTarjeta.setText(_translate("venPrincipal", "Tarjeta"))
        self.chkEfectivo.setText(_translate("venPrincipal", "Efectivo"))
        item = self.tablaClientes.horizontalHeaderItem(0)
        item.setText(_translate("venPrincipal", "DNI"))
        item = self.tablaClientes.horizontalHeaderItem(1)
        item.setText(_translate("venPrincipal", "Apellidos"))
        item = self.tablaClientes.horizontalHeaderItem(2)
        item.setText(_translate("venPrincipal", "Nombre"))
        self.btnClienteAlta.setText(_translate("venPrincipal", "Alta"))
        self.btnClienteModificar.setText(_translate("venPrincipal", "Modificar"))
        self.btnClienteBaja.setText(_translate("venPrincipal", "Baja"))
        self.btnClienteLimpiar.setText(_translate("venPrincipal", "Limpiar"))
        self.btnClienteSalir.setText(_translate("venPrincipal", "Salir"))
        self.panel.setTabText(self.panel.indexOf(self.panelCliente), _translate("venPrincipal", "Clientes"))
        self.panel.setTabText(self.panel.indexOf(self.panelFacturacion), _translate("venPrincipal", "Facturacion"))
        self.panel.setTabText(self.panel.indexOf(self.panelProductos), _translate("venPrincipal", "Productos"))
        self.menuArchivo.setTitle(_translate("venPrincipal", "Archivo"))
        self.actionAbrir.setText(_translate("venPrincipal", "Abrir..."))
        self.actionImprimir.setText(_translate("venPrincipal", "Imprimir..."))
        self.actionSalir.setText(_translate("venPrincipal", "Salir"))
import rc_botonesInterfaz_rc
