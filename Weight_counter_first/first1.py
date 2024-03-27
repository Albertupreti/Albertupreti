

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtUiTools import QUiLoader

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.click_me_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it())
        self.click_me_button.setGeometry(QtCore.QRect(180, 300, 471, 221))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.click_me_button.setFont(font)
        self.click_me_button.setObjectName("click_me_button")
        self.hello_world_label = QtWidgets.QLabel(self.centralwidget)
        self.hello_world_label.setGeometry(QtCore.QRect(150, 110, 511, 181))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(44)
        font.setBold(True)
        font.setWeight(75)
        self.hello_world_label.setFont(font)
        self.hello_world_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.hello_world_label.setObjectName("hello_world_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def press_it(self):
        self.hello_world_label.setText("Boom!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.click_me_button.setText(_translate("MainWindow", "Click me!"))
        self.hello_world_label.setText(_translate("MainWindow", "           Hello world!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
