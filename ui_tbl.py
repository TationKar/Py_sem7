# Form implementation generated from reading ui file 'ui_tbl.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 825)
        MainWindow.setStyleSheet("background-color: grey")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 921, 80))
        self.frame.setStyleSheet("background-color: black")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(260, 30, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.rows = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.rows.setGeometry(QtCore.QRect(230, 130, 113, 50))
        self.rows.setStyleSheet("background-color: white")
        self.rows.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.rows.setObjectName("rows")
        self.clmn = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.clmn.setGeometry(QtCore.QRect(580, 130, 113, 51))
        self.clmn.setStyleSheet("background-color: white")
        self.clmn.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.clmn.setObjectName("clmn")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 110, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 110, 161, 20))
        self.label_3.setObjectName("label_3")
        self.resButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.resButton.setGeometry(QtCore.QRect(350, 200, 231, 32))
        self.resButton.setObjectName("resButton")
        self.table_res = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.table_res.setGeometry(QtCore.QRect(30, 250, 861, 541))
        self.table_res.setStyleSheet("background-color: white")
        self.table_res.setObjectName("table_res")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ТАБЛИЦА УМНОЖЕНИЯ"))
        self.label_2.setText(_translate("MainWindow", "Введите число строк"))
        self.label_3.setText(_translate("MainWindow", "Введите число столбцов"))
        self.resButton.setText(_translate("MainWindow", "ПОКАЗАТЬ РЕЗУЛЬТАТ"))