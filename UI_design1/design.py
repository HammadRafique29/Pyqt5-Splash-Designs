from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
global count_time
count_time = 0


class Ui_Form(object):
    def __init__(self):
        self.label_4 = None
        self.loadingcount = None
        self.time = None
        self.label_3 = None
        self.progressbase_2 = None
        self.widget = None
        self.verticalLayout = None
        self.progresstext = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(234, 215)
        Form.setMinimumSize(QtCore.QSize(234, 215))
        Form.setMaximumSize(QtCore.QSize(234, 215))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.progressbase_2 = QtWidgets.QWidget(self.widget)
        self.progressbase_2.setGeometry(QtCore.QRect(0, 0, 191, 191))
        self.progressbase_2.setStyleSheet(
            "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90.0, stop:0.753408 rgba(255, 255, 255, 255), stop:0.755886 rgba(117, 0, 176, 255));\n""border-radius: 95")
        self.progressbase_2.setObjectName("progressbase_2")
        self.progresstext = QtWidgets.QWidget(self.widget)
        self.progresstext.setGeometry(QtCore.QRect(6, 5, 180, 180))
        self.progresstext.setStyleSheet("background-color: rgb(188, 143, 255);\n""border-radius:90\n""\n""\n""")
        self.progresstext.setObjectName("progresstext")
        self.label_3 = QtWidgets.QLabel(self.progresstext)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 91, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.progresstext)
        self.label_4.setGeometry(QtCore.QRect(50, 30, 91, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.loadingcount = QtWidgets.QLabel(self.progresstext)
        self.loadingcount.setGeometry(QtCore.QRect(55, 60, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.loadingcount.setFont(font)
        self.loadingcount.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingcount.setObjectName("loadingcount")
        self.label_3.raise_()
        self.loadingcount.raise_()
        self.label_4.raise_()
        self.verticalLayout.addWidget(self.widget)
        # self.progress(0)
        self.retranslateUi(Form)
        self.time = QtCore.QTimer()
        self.time.timeout.connect(lambda: self.loadingtime())
        self.time.start(30)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setWindowFlag(Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Loading ..."))
        self.label_4.setText(_translate("Form", "Staring Up"))
        self.loadingcount.setText(_translate("Form",
                                             f"<html><head/><body><p><span style=\" font-size:26pt;\">{count_time}</span><span style=\" font-size:26pt; vertical-align:super;\">%</span></p></body></html>"))

    def progress(self, value):
        _translate = QtCore.QCoreApplication.translate
        newstylesheet3 = "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90.0, stop:{stop1} rgba(255, 255, 255, 255), stop:{stop2} rgba(117, 0, 176, 255));\n""border-radius: 95"

        progressvalue = (100 - value) / 100
        newstylesheet3 = newstylesheet3.replace("{stop1}", str(progressvalue - 0.00999)).replace("{stop2}",
                                                                                                 str(progressvalue))
        self.progressbase_2.setStyleSheet(newstylesheet3)
        self.loadingcount.setText(_translate("Form",
                                             f"<html><head/><body><p><span style=\" font-size:26pt;\">{count_time}</span><span style=\" font-size:26pt; vertical-align:super;\">%</span></p></body></html>"))

    def loadingtime(self):
        import time
        global count_time

        if count_time > 100:
            self.time.stop()
            time.sleep(1)
            exit()
        else:
            self.progress(count_time)
            count_time += 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
