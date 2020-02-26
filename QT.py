# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(QtWidgets.QMainWindow):
    def setupUi(self, Form):
        super(Ui_Form, self).__init__()
        Form.setObjectName("Form")
        Form.resize(817, 640)
        Form.setMouseTracking(False)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(60, 150, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.comboBox.setFont(font)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(240, 150, 341, 87))
        self.textEdit.setObjectName("textEdit")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setEnabled(False)
        self.radioButton.setGeometry(QtCore.QRect(60, 280, 95, 20))
        self.radioButton.setMouseTracking(True)
        self.radioButton.setToolTip("")
        self.radioButton.setAutoFillBackground(True)
        self.radioButton.setText("")
        self.radioButton.setCheckable(True)
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 320, 95, 20))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setGeometry(QtCore.QRect(60, 360, 95, 20))
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setEnabled(False)
        self.radioButton_4.setGeometry(QtCore.QRect(60, 400, 95, 20))
        self.radioButton_4.setText("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Form)
        self.radioButton_5.setEnabled(False)
        self.radioButton_5.setGeometry(QtCore.QRect(60, 440, 95, 20))
        self.radioButton_5.setText("")
        self.radioButton_5.setObjectName("radioButton_5")

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "1"))
        self.comboBox.setItemText(1, _translate("Form", "2"))
        self.comboBox.setItemText(2, _translate("Form", "3"))
        self.comboBox.setItemText(3, _translate("Form", "4"))
        self.comboBox.setItemText(4, _translate("Form", "5"))
        self.comboBox.setItemText(5, _translate("Form", "6"))

app = QtWidgets.QApplication([])
application = Ui_Form()
application.show()
sys.exit(app.exec())