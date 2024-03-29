# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login_window(object):
    def setupUi(self, Login_window):
        Login_window.setObjectName("Login_window")
        Login_window.resize(1020, 680)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login_window.sizePolicy().hasHeightForWidth())
        Login_window.setSizePolicy(sizePolicy)
        Login_window.setMaximumSize(QtCore.QSize(1020, 680))
        self.centralwidget = QtWidgets.QWidget(Login_window)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 1011, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Title_leftside_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.Title_leftside_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title_leftside_2.sizePolicy().hasHeightForWidth())
        self.Title_leftside_2.setSizePolicy(sizePolicy)
        self.Title_leftside_2.setMinimumSize(QtCore.QSize(7, 0))
        self.Title_leftside_2.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Title_leftside_2.setFont(font)
        self.Title_leftside_2.setStyleSheet("color: rgb(237, 51, 59);")
        self.Title_leftside_2.setScaledContents(False)
        self.Title_leftside_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Title_leftside_2.setObjectName("Title_leftside_2")
        self.horizontalLayout_6.addWidget(self.Title_leftside_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 60, 1011, 571))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(350, 100, 350, 100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_frame = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setObjectName("login_frame")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.login_frame)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(4, 10, 301, 381))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_title = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.login_title.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.login_title.setFont(font)
        self.login_title.setStyleSheet("color: rgb(237, 51, 59);")
        self.login_title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.login_title.setObjectName("login_title")
        self.verticalLayout.addWidget(self.login_title)
        self.username = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMaximumSize(QtCore.QSize(300, 40))
        self.username.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMaximumSize(QtCore.QSize(16777215, 40))
        self.password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password.setCursorPosition(0)
        self.password.setDragEnabled(True)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.login_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.login_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.login_btn.setStyleSheet("background-color: rgb(28, 113, 216);\n"
"color: rgb(255, 255, 255);")
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout.addWidget(self.login_btn)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 10)
        self.verticalLayout.setStretch(3, 10)
        self.horizontalLayout.addWidget(self.login_frame)
        Login_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login_window)
        self.statusbar.setObjectName("statusbar")
        Login_window.setStatusBar(self.statusbar)

        self.retranslateUi(Login_window)
        QtCore.QMetaObject.connectSlotsByName(Login_window)

    def retranslateUi(self, Login_window):
        _translate = QtCore.QCoreApplication.translate
        Login_window.setWindowTitle(_translate("Login_window", "MainWindow"))
        self.Title_leftside_2.setText(_translate("Login_window", "Crimson Tech : Qc weight Recorder"))
        self.login_title.setText(_translate("Login_window", "Login"))
        self.username.setPlaceholderText(_translate("Login_window", "username"))
        self.password.setPlaceholderText(_translate("Login_window", "password"))
        self.login_btn.setText(_translate("Login_window", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_window = QtWidgets.QMainWindow()
    ui = Ui_Login_window()
    ui.setupUi(Login_window)
    Login_window.show()
    sys.exit(app.exec_())