# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogAviso.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialogAviso(object):
    def setupUi(self, dialogAviso):
        dialogAviso.setObjectName("dialogAviso")
        dialogAviso.setWindowModality(QtCore.Qt.ApplicationModal)
        dialogAviso.resize(94, 97)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogAviso.sizePolicy().hasHeightForWidth())
        dialogAviso.setSizePolicy(sizePolicy)
        dialogAviso.setMinimumSize(QtCore.QSize(0, 97))
        dialogAviso.setMaximumSize(QtCore.QSize(16777215, 97))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconoWarning/aviso.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogAviso.setWindowIcon(icon)
        dialogAviso.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialogAviso)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setObjectName("layout")
        self.iconAviso = QtWidgets.QLabel(dialogAviso)
        self.iconAviso.setMinimumSize(QtCore.QSize(48, 48))
        self.iconAviso.setMaximumSize(QtCore.QSize(48, 48))
        self.iconAviso.setText("")
        self.iconAviso.setPixmap(QtGui.QPixmap(":/iconoWarning/aviso.png"))
        self.iconAviso.setObjectName("iconAviso")
        self.layout.addWidget(self.iconAviso)
        self.lblAviso = QtWidgets.QLabel(dialogAviso)
        self.lblAviso.setText("")
        self.lblAviso.setObjectName("lblAviso")
        self.layout.addWidget(self.lblAviso)
        self.verticalLayout.addLayout(self.layout)
        self.botones = QtWidgets.QDialogButtonBox(dialogAviso)
        self.botones.setOrientation(QtCore.Qt.Horizontal)
        self.botones.setStandardButtons(QtWidgets.QDialogButtonBox.NoButton)
        self.botones.setObjectName("botones")
        self.verticalLayout.addWidget(self.botones)

        self.retranslateUi(dialogAviso)
        self.botones.accepted.connect(dialogAviso.accept)
        self.botones.rejected.connect(dialogAviso.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogAviso)

    def retranslateUi(self, dialogAviso):
        _translate = QtCore.QCoreApplication.translate
        dialogAviso.setWindowTitle(_translate("dialogAviso", "Aviso"))
import rc_iconosDialog_rc
