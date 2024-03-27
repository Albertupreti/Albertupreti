
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(2000, 2000))
        MainWindow.setStyleSheet("background-color: rgb(209, 216, 195)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setStyleSheet("color: rgb(224, 27, 36);")
        self.Title.setObjectName("Title")
        self.horizontalLayout_4.addWidget(self.Title)
        spacerItem = QtWidgets.QSpacerItem(37, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.production_unit = QtWidgets.QLabel(self.centralwidget)
        self.production_unit.setStyleSheet("color:rgb(224, 27, 36)")
        self.production_unit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.production_unit.setTextFormat(QtCore.Qt.AutoText)
        self.production_unit.setScaledContents(True)
        self.production_unit.setAlignment(QtCore.Qt.AlignCenter)
        self.production_unit.setObjectName("production_unit")
        self.horizontalLayout_4.addWidget(self.production_unit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.top_line = QtWidgets.QFrame(self.centralwidget)
        self.top_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.top_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_line.setObjectName("top_line")
        self.gridLayout.addWidget(self.top_line, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.weight_recorder = QtWidgets.QLabel(self.centralwidget)
        self.weight_recorder.setObjectName("weight_recorder")
        self.horizontalLayout.addWidget(self.weight_recorder)
        spacerItem1 = QtWidgets.QSpacerItem(360, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.search_bar = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy)
        self.search_bar.setMinimumSize(QtCore.QSize(222, 28))
        self.search_bar.setMaximumSize(QtCore.QSize(201, 39))
        self.search_bar.setStyleSheet("padding-right: 20px;\n"
"padding-left: 5px;\n"
"background: ;\n"
"background-position: right;\n"
"background-repeat: no-repeat;\n"
" \n"
"border: 1px solid black;\n"
"border-radius: 10px;")
        self.search_bar.setText("")
        self.search_bar.setObjectName("search_bar")
        self.horizontalLayout.addWidget(self.search_bar)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.middle_line = QtWidgets.QFrame(self.centralwidget)
        self.middle_line.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.middle_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.middle_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.middle_line.setObjectName("middle_line")
        self.gridLayout.addWidget(self.middle_line, 3, 0, 1, 1)
        self.Non_Veg = QtWidgets.QTabWidget(self.centralwidget)
        self.Non_Veg.setStyleSheet("color: rgb(36, 122, 33);")
        self.Non_Veg.setObjectName("Non_Veg")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 22, 761, 293))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.cake_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cake_btn.sizePolicy().hasHeightForWidth())
        self.cake_btn.setSizePolicy(sizePolicy)
        self.cake_btn.setMinimumSize(QtCore.QSize(240, 260))
        self.cake_btn.setMaximumSize(QtCore.QSize(16777215, 16777214))
        self.cake_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cake_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cake_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("wai-wai-Chicken-.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("wai-wai-Chicken-.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cake_btn.setIcon(icon)
        self.cake_btn.setIconSize(QtCore.QSize(240, 200))
        self.cake_btn.setProperty("picture", QtGui.QPixmap("Search_Icon.png"))
        self.cake_btn.setObjectName("cake_btn")
        self.horizontalLayout_7.addWidget(self.cake_btn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.packet_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packet_btn.sizePolicy().hasHeightForWidth())
        self.packet_btn.setSizePolicy(sizePolicy)
        self.packet_btn.setMinimumSize(QtCore.QSize(240, 260))
        self.packet_btn.setMaximumSize(QtCore.QSize(16777215, 16777214))
        self.packet_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.packet_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.packet_btn.setText("")
        self.packet_btn.setIcon(icon)
        self.packet_btn.setIconSize(QtCore.QSize(228, 195))
        self.packet_btn.setProperty("picture", QtGui.QPixmap("Search_Icon.png"))
        self.packet_btn.setObjectName("packet_btn")
        self.horizontalLayout_7.addWidget(self.packet_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.twin_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twin_btn.sizePolicy().hasHeightForWidth())
        self.twin_btn.setSizePolicy(sizePolicy)
        self.twin_btn.setMinimumSize(QtCore.QSize(240, 260))
        self.twin_btn.setMaximumSize(QtCore.QSize(16777215, 16777214))
        self.twin_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.twin_btn.setMouseTracking(True)
        self.twin_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.twin_btn.setText("")
        self.twin_btn.setIcon(icon)
        self.twin_btn.setIconSize(QtCore.QSize(228, 195))
        self.twin_btn.setProperty("picture", QtGui.QPixmap("Search_Icon.png"))
        self.twin_btn.setObjectName("twin_btn")
        self.horizontalLayout_7.addWidget(self.twin_btn, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(52, 21, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.cake_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cake_3.sizePolicy().hasHeightForWidth())
        self.cake_3.setSizePolicy(sizePolicy)
        self.cake_3.setMinimumSize(QtCore.QSize(0, 0))
        self.cake_3.setMaximumSize(QtCore.QSize(120, 30))
        self.cake_3.setAccessibleDescription("")
        self.cake_3.setStyleSheet("color: rgb(36, 31, 49);\n"
"background-color: rgb(143, 240, 164)")
        self.cake_3.setScaledContents(False)
        self.cake_3.setAlignment(QtCore.Qt.AlignCenter)
        self.cake_3.setWordWrap(False)
        self.cake_3.setObjectName("cake_3")
        self.horizontalLayout_8.addWidget(self.cake_3)
        spacerItem5 = QtWidgets.QSpacerItem(51, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.packet_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packet_3.sizePolicy().hasHeightForWidth())
        self.packet_3.setSizePolicy(sizePolicy)
        self.packet_3.setMinimumSize(QtCore.QSize(6, 0))
        self.packet_3.setMaximumSize(QtCore.QSize(120, 30))
        self.packet_3.setStyleSheet("background-color: rgb(143, 240, 164);\n"
"color: rgb(36, 31, 49);")
        self.packet_3.setAlignment(QtCore.Qt.AlignCenter)
        self.packet_3.setObjectName("packet_3")
        self.horizontalLayout_8.addWidget(self.packet_3)
        spacerItem6 = QtWidgets.QSpacerItem(151, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.twin_sachet_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twin_sachet_3.sizePolicy().hasHeightForWidth())
        self.twin_sachet_3.setSizePolicy(sizePolicy)
        self.twin_sachet_3.setMaximumSize(QtCore.QSize(120, 30))
        self.twin_sachet_3.setStyleSheet("background-color: rgb(143, 240, 164);\n"
"color: rgb(36, 31, 49);")
        self.twin_sachet_3.setAlignment(QtCore.Qt.AlignCenter)
        self.twin_sachet_3.setObjectName("twin_sachet_3")
        self.horizontalLayout_8.addWidget(self.twin_sachet_3)
        spacerItem7 = QtWidgets.QSpacerItem(51, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.Non_Veg.addTab(self.tab_1, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 22, 761, 293))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_6.setMaximumSize(QtCore.QSize(16777215, 16777214))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QtCore.QSize(240, 200))
        self.pushButton_6.setProperty("picture", QtGui.QPixmap("Search_Icon.png"))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_7.setMaximumSize(QtCore.QSize(16777215, 16777214))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(228, 195))
        self.pushButton_7.setProperty("picture", QtGui.QPixmap("Search_Icon.png"))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_8.setMaximumSize(QtCore.QSize(16777215, 16777214))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setMouseTracking(True)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(228, 195))
        self.pushButton_8.setProperty("picture", QtGui.QPixmap("Search_Icon.png"))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_5.addWidget(self.pushButton_8, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(52, 21, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.cake_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cake_2.sizePolicy().hasHeightForWidth())
        self.cake_2.setSizePolicy(sizePolicy)
        self.cake_2.setMinimumSize(QtCore.QSize(0, 0))
        self.cake_2.setMaximumSize(QtCore.QSize(120, 30))
        self.cake_2.setAccessibleDescription("")
        self.cake_2.setStyleSheet("color: rgb(36, 31, 49);\n"
"background-color: rgb(143, 240, 164)")
        self.cake_2.setScaledContents(False)
        self.cake_2.setAlignment(QtCore.Qt.AlignCenter)
        self.cake_2.setWordWrap(False)
        self.cake_2.setObjectName("cake_2")
        self.horizontalLayout_6.addWidget(self.cake_2)
        spacerItem11 = QtWidgets.QSpacerItem(51, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.packet_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packet_2.sizePolicy().hasHeightForWidth())
        self.packet_2.setSizePolicy(sizePolicy)
        self.packet_2.setMinimumSize(QtCore.QSize(6, 0))
        self.packet_2.setMaximumSize(QtCore.QSize(120, 30))
        self.packet_2.setStyleSheet("background-color: rgb(143, 240, 164);\n"
"color: rgb(36, 31, 49);")
        self.packet_2.setAlignment(QtCore.Qt.AlignCenter)
        self.packet_2.setObjectName("packet_2")
        self.horizontalLayout_6.addWidget(self.packet_2)
        spacerItem12 = QtWidgets.QSpacerItem(151, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.twin_sachet_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twin_sachet_2.sizePolicy().hasHeightForWidth())
        self.twin_sachet_2.setSizePolicy(sizePolicy)
        self.twin_sachet_2.setMaximumSize(QtCore.QSize(120, 30))
        self.twin_sachet_2.setStyleSheet("background-color: rgb(143, 240, 164);\n"
"color: rgb(36, 31, 49);")
        self.twin_sachet_2.setAlignment(QtCore.Qt.AlignCenter)
        self.twin_sachet_2.setObjectName("twin_sachet_2")
        self.horizontalLayout_6.addWidget(self.twin_sachet_2)
        spacerItem13 = QtWidgets.QSpacerItem(51, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.Non_Veg.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.Non_Veg, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar_3)

        self.retranslateUi(MainWindow)
        self.Non_Veg.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "CRIMSON TECH"))
        self.production_unit.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\"></span></p><p align=\"justify\"><span style=\" font-size:12pt;\">Procuction Unit </span></p></body></html>"))
        self.weight_recorder.setText(_translate("MainWindow", "QC WEIGHT RECORDER"))
        self.search_bar.setPlaceholderText(_translate("MainWindow", "search"))
        self.cake_3.setText(_translate("MainWindow", "CAKE"))
        self.packet_3.setText(_translate("MainWindow", " Packet Sachet"))
        self.twin_sachet_3.setText(_translate("MainWindow", "TWIN Sachet"))
        self.Non_Veg.setTabText(self.Non_Veg.indexOf(self.tab_1), _translate("MainWindow", "Non-Veg"))
        self.cake_2.setText(_translate("MainWindow", "CAKE"))
        self.packet_2.setText(_translate("MainWindow", " Packet Sachet"))
        self.twin_sachet_2.setText(_translate("MainWindow", "TWIN Sachet"))
        self.Non_Veg.setTabText(self.Non_Veg.indexOf(self.tab_4), _translate("MainWindow", "Veg"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
