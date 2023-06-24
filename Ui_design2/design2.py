# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
count_time = 0


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(333, 250)
        self.border_area = QtWidgets.QWidget(Form)
        self.border_area.setGeometry(QtCore.QRect(70, 20, 200, 200))
        self.border_area.setStyleSheet("border: 5px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 100px;\n"
"\n"
"\n"
"")
        self.border_area.setObjectName("border_area")
        self.loading_base = QtWidgets.QWidget(Form)
        self.loading_base.setGeometry(QtCore.QRect(62, 15, 215, 210))
        self.loading_base.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"border-radius: 105px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.738158 rgba(197, 208, 200, 255), stop:0.740971 rgba(105, 0, 158, 255));")
        self.loading_base.setObjectName("loading_base")
        self.data_base = QtWidgets.QWidget(Form)
        self.data_base.setGeometry(QtCore.QRect(75, 25, 190, 190))
        self.data_base.setStyleSheet("border-radius:95px;\n"
"background-color: rgb(255, 170, 0);\n"
"")
        self.data_base.setObjectName("data_base")
        self.label = QtWidgets.QLabel(self.data_base)
        self.label.setGeometry(QtCore.QRect(55, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 0, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.data_base)
        self.label_2.setGeometry(QtCore.QRect(40, 142, 121, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.data_base)
        self.label_3.setGeometry(QtCore.QRect(30, 115, 131, 20))
        self.label_3.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(203, 203, 203);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.data_base)
        self.label_4.setGeometry(QtCore.QRect(60, 60, 81, 51))
        self.label_4.setStyleSheet("\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.loading_base.raise_()
        self.border_area.raise_()
        self.data_base.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.time = QtCore.QTimer()
        self.time.timeout.connect(lambda: self.progress())
        self.time.start(20)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(25)

        # adding shadow to the label
        self.data_base.setGraphicsEffect(self.shadow)

        Form.setWindowFlag(Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def progress(self):
        global count_time
        _translate = QtCore.QCoreApplication.translate
        newstylesheet = f"<html><head/><body><p><span style=\" font-size:26pt;\">{count_time}</span><span style=\" font-size:26pt; vertical-align:super;\">%</span></p></body></html>"

        progress = (100 - count_time) / 100
        if count_time <= 100:
            self.loading_base.setStyleSheet(
                f"background-color: rgb(85, 255, 0);\n""border-radius: 105px;\n"f"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{str(progress - 0.009)} rgba(197, 208, 200, 255), stop:{str(progress)} rgba(105, 0, 158, 255));")
            self.label_4.setText(_translate("Form", newstylesheet))
            count_time += 1
        else:
            exit()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "SkyTrust"))
        self.label_2.setText(_translate("Form", "Loading... Please Wait"))
        self.label_3.setText(_translate("Form", "Verion 1.1.0.9"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:26pt;\">0</span><span style=\" font-size:26pt; vertical-align:super;\">%</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
