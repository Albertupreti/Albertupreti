
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_second_window(object):
    def setupUi(self, second_window):
        second_window.setObjectName("second_window")
        second_window.resize(722, 495)
        second_window.setStyleSheet("/* Style for the main window */\n"
"QMainWindow {\n"
"    background-color: #f0f0f0; /* Light gray background */\n"
"}\n"
"\n"
"/* Style for the central widget (the area inside the main window) */\n"
"QWidget#centralWidget {\n"
"    background-color: white; /* White background */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    border: 2px solid #3498db; /* Blue border */\n"
"}\n"
"\n"
"/* Style for the title bar */\n"
"QMainWindow::titleBar {\n"
"    background-color: #3498db; /* Blue background for the title bar */\n"
"    color: white; /* White text color */\n"
"    padding: 6px; /* Padding around the title text */\n"
"}\n"
"\n"
"/* Style for the window title */\n"
"QMainWindow::title {\n"
"    font-size: 18px; /* Larger font size for the title */\n"
"    font-weight: bold; /* Bold text */\n"
"}\n"
"\n"
"/* Style for the window close button */\n"
"QMainWindow::close-button {\n"
"    background-color: transparent; /* Transparent background */\n"
"    icon-size: 30px; /* Larger icon size */\n"
"}\n"
"\n"
"/* Hover style for the window close button */\n"
"QMainWindow::close-button:hover {\n"
"    background-color: #e74c3c; /* Red background on hover */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"/* Pressed style for the window close button */\n"
"QMainWindow::close-button:pressed {\n"
"    background-color: #c0392b; /* Dark red background when pressed */\n"
"}\n"
"\n"
"/* Style for the window minimize button */\n"
"QMainWindow::minimize-button {\n"
"    background-color: transparent; /* Transparent background */\n"
"    icon-size: 20px; /* Smaller icon size */\n"
"}\n"
"\n"
"/* Hover style for the window minimize button */\n"
"QMainWindow::minimize-button:hover {\n"
"    background-color: #e67e22; /* Orange background on hover */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"/* Pressed style for the window minimize button */\n"
"QMainWindow::minimize-button:pressed {\n"
"    background-color: #d35400; /* Dark orange background when pressed */\n"
"}\n"
"\n"
"/* Style for the window maximize button */\n"
"QMainWindow::maximize-button {\n"
"    background-color: transparent; /* Transparent background */\n"
"    icon-size: 20px; /* Smaller icon size */\n"
"}\n"
"\n"
"/* Hover style for the window maximize button */\n"
"QMainWindow::maximize-button:hover {\n"
"    background-color: #2ecc71; /* Green background on hover */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"/* Pressed style for the window maximize button */\n"
"QMainWindow::maximize-button:pressed {\n"
"    background-color: #27ae60; /* Dark green background when pressed */\n"
"}\n"
"")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(second_window)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 691, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Title = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Title.setStyleSheet("color: rgb(224, 27, 36);")
        self.Title.setObjectName("Title")
        self.horizontalLayout_2.addWidget(self.Title)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.production_unit_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.production_unit_2.setStyleSheet("color:rgb(224, 27, 36)")
        self.production_unit_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.production_unit_2.setTextFormat(QtCore.Qt.AutoText)
        self.production_unit_2.setScaledContents(True)
        self.production_unit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.production_unit_2.setObjectName("production_unit_2")
        self.horizontalLayout_2.addWidget(self.production_unit_2)
        self.line = QtWidgets.QFrame(second_window)
        self.line.setGeometry(QtCore.QRect(10, 50, 691, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(second_window)
        self.line_2.setGeometry(QtCore.QRect(163, 60, 20, 431))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(second_window)
        self.line_3.setGeometry(QtCore.QRect(190, 140, 511, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Home_icon = QtWidgets.QLabel(second_window)
        self.Home_icon.setGeometry(QtCore.QRect(560, 100, 41, 31))
        self.Home_icon.setText("")
        self.Home_icon.setPixmap(QtGui.QPixmap("Weight_counter_first/fugue-icons-3.5.6/icons/application-home.png"))
        self.Home_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.Home_icon.setObjectName("Home_icon")
        self.label_2 = QtWidgets.QLabel(second_window)
        self.label_2.setGeometry(QtCore.QRect(600, 100, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(second_window)
        self.label_3.setGeometry(QtCore.QRect(190, 106, 101, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(second_window)
        self.label_4.setGeometry(QtCore.QRect(290, 110, 21, 17))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Weight_counter_first/fugue-icons-3.5.6/icons/arrow-curve-000-left.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(second_window)
        self.label_5.setGeometry(QtCore.QRect(320, 110, 67, 17))
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget = QtWidgets.QWidget(second_window)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 160, 521, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton1.sizePolicy().hasHeightForWidth())
        self.pushButton1.setSizePolicy(sizePolicy)
        self.pushButton1.setMinimumSize(QtCore.QSize(120, 90))
        self.pushButton1.setSizeIncrement(QtCore.QSize(100, 100))
        self.pushButton1.setBaseSize(QtCore.QSize(50, 50))
        self.pushButton1.setStyleSheet("QPushButton { color: red; background-color: rgb(143, 240, 164) }\n"
"QPushButton:enabled { color: red }\n"
"QPushButton:hover { color: blue }")
        self.pushButton1.setObjectName("pushButton1")
        self.gridLayout.addWidget(self.pushButton1, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setMinimumSize(QtCore.QSize(121, 90))
        self.pushButton_10.setStyleSheet("QPushButton { color: red; background-color: rgb(143, 240, 164) }\n"
"QPushButton:enabled { color: red }\n"
"QPushButton:hover { color: blue }")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 2, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setMinimumSize(QtCore.QSize(120, 90))
        self.pushButton_11.setStyleSheet("QPushButton { color: red; background-color: rgb(143, 240, 164) }\n"
"QPushButton:enabled { color: red }\n"
"QPushButton:hover { color: blue }")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 2, 2, 1, 1)
        self.pushButton6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton6.setMinimumSize(QtCore.QSize(120, 90))
        self.pushButton6.setStyleSheet("QPushButton { color: red; background-color: rgb(143, 240, 164) }\n"
"QPushButton:enabled { color: red }\n"
"QPushButton:hover { color: blue }")
        self.pushButton6.setObjectName("pushButton6")
        self.gridLayout.addWidget(self.pushButton6, 1, 1, 1, 1)
        self.pushButton2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton2.sizePolicy().hasHeightForWidth())
        self.pushButton2.setSizePolicy(sizePolicy)
        self.pushButton2.setMinimumSize(QtCore.QSize(12, 15))
        self.pushButton2.setSizeIncrement(QtCore.QSize(9, 4))
        self.pushButton2.setStyleSheet("QPushButton { color: red; background-color: rgb(143, 240, 164) }\n"
"QPushButton:enabled { color: red }\n"
"QPushButton:hover { color: blue }")
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout.addWidget(self.pushButton2, 0, 1, 1, 1)
        self.pushButton5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton5.setMinimumSize(QtCore.QSize(120, 90))
        self.pushButton5.setStyleSheet("QPushButton { color: red; background-color: rgb(143, 240, 164) }\n"
"QPushButton:enabled { color: red }\n"
"QPushButton:hover { color: blue }")
        self.pushButton5.setObjectName("pushButton5")
        self.gridLayout.addWidget(self.pushButton5, 1, 0, 1, 1)
        self.pushButton9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton9.setMinimumSize(QtCore.QSize(120, 90))
        self.pushButton9.setStyleSheet("QPushButton { color: red; background-color: rgb(143, 240, 164) }\n"
"QPushButton:enabled { color: red }\n"
"QPushButton:hover { color: blue }")
        self.pushButton9.setObjectName("pushButton9")
        self.gridLayout.addWidget(self.pushButton9, 2, 0, 1, 1)
        self.pushButton8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton8.setMinimumSize(QtCore.QSize(120, 90))
        self.pushButton8.setStyleSheet("QPushButton { color: red; background-color: rgb(143, 240, 164) }\n"
"QPushButton:enabled { color: red }\n"
"QPushButton:hover { color: blue }")
        self.pushButton8.setObjectName("pushButton8")
        self.gridLayout.addWidget(self.pushButton8, 1, 3, 1, 1)
        self.pushButton4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton4.setMinimumSize(QtCore.QSize(120, 90))
        self.pushButton4.setStyleSheet("QPushButton { color: red; background-color: rgb(143, 240, 164) }\n"
"QPushButton:enabled { color: red }\n"
"QPushButton:hover { color: blue }")
        self.pushButton4.setObjectName("pushButton4")
        self.gridLayout.addWidget(self.pushButton4, 0, 3, 1, 1)
        self.pushButton7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton7.setMinimumSize(QtCore.QSize(120, 90))
        self.pushButton7.setStyleSheet("QPushButton { color: red; background-color: rgb(143, 240, 164) }\n"
"QPushButton:enabled { color: red }\n"
"QPushButton:hover { color: blue }")
        self.pushButton7.setObjectName("pushButton7")
        self.gridLayout.addWidget(self.pushButton7, 1, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMinimumSize(QtCore.QSize(120, 90))
        self.pushButton_12.setStyleSheet("QPushButton { color: red; background-color: rgb(143, 240, 164) }\n"
"QPushButton:enabled { color: red }\n"
"QPushButton:hover { color: blue }")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 2, 3, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton3.setMinimumSize(QtCore.QSize(120, 90))
        self.pushButton3.setStyleSheet("QPushButton { color: red; background-color: rgb(143, 240, 164) }\n"
"QPushButton:enabled { color: red }\n"
"QPushButton:hover { color: blue }")
        self.pushButton3.setObjectName("pushButton3")
        self.gridLayout.addWidget(self.pushButton3, 0, 2, 1, 1)
        self.frame = QtWidgets.QFrame(second_window)
        self.frame.setGeometry(QtCore.QRect(0, 70, 151, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 151, 81))
        self.treeWidget.setStyleSheet("QTreeWidget::branch:has-siblings:!adjoins-item {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QTreeWidget::branch:has-siblings:adjoins-item {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QTreeWidget::branch:!has-children:!has-siblings:adjoins-item {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QTreeWidget::branch:closed:has-children:has-siblings {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QTreeWidget::branch:open:has-children:has-siblings {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: lightblue;\n"
"    border: 1px solid black;\n"
"    padding: 2px;\n"
"}\n"
"")
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.frame)
        self.treeWidget_2.setGeometry(QtCore.QRect(0, 60, 151, 71))
        self.treeWidget_2.setStyleSheet("QTreeWidget::branch:has-siblings:!adjoins-item {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QTreeWidget::branch:has-siblings:adjoins-item {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QTreeWidget::branch:!has-children:!has-siblings:adjoins-item {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QTreeWidget::branch:closed:has-children:has-siblings {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QTreeWidget::branch:open:has-children:has-siblings {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: lightblue;\n"
"    border: 1px solid black;\n"
"    padding: 2px;\n"
"}\n"
"")
        self.treeWidget_2.setObjectName("treeWidget_2")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        self.treeWidget_3 = QtWidgets.QTreeWidget(self.frame)
        self.treeWidget_3.setGeometry(QtCore.QRect(0, 120, 151, 81))
        self.treeWidget_3.setStyleSheet("QTreeWidget::branch:has-siblings:!adjoins-item {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QTreeWidget::branch:has-siblings:adjoins-item {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QTreeWidget::branch:!has-children:!has-siblings:adjoins-item {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QTreeWidget::branch:closed:has-children:has-siblings {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QTreeWidget::branch:open:has-children:has-siblings {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: lightblue;\n"
"    border: 1px solid black;\n"
"    padding: 2px;\n"
"}\n"
"")
        self.treeWidget_3.setObjectName("treeWidget_3")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)

        self.retranslateUi(second_window)
        QtCore.QMetaObject.connectSlotsByName(second_window)

    def retranslateUi(self, second_window):
        _translate = QtCore.QCoreApplication.translate
        second_window.setWindowTitle(_translate("second_window", "Form"))
        self.Title.setText(_translate("second_window", "CRIMSON TECH"))
        self.production_unit_2.setText(_translate("second_window", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\"></span></p><p align=\"justify\"><span style=\" font-size:12pt;\">Procuction Unit </span></p></body></html>"))
        self.label_2.setText(_translate("second_window", "Home"))
        self.label_3.setText(_translate("second_window", "Packet Sachet"))
        self.label_5.setText(_translate("second_window", "Non-veg"))
        self.pushButton1.setText(_translate("second_window", "Wai Wai chicken "))
        self.pushButton_10.setText(_translate("second_window", "PushButton"))
        self.pushButton_11.setText(_translate("second_window", "PushButton"))
        self.pushButton6.setText(_translate("second_window", "PushButton"))
        self.pushButton2.setText(_translate("second_window", "PushButton"))
        self.pushButton5.setText(_translate("second_window", "PushButton"))
        self.pushButton9.setText(_translate("second_window", "PushButton"))
        self.pushButton8.setText(_translate("second_window", "PushButton"))
        self.pushButton4.setText(_translate("second_window", "PushButton"))
        self.pushButton7.setText(_translate("second_window", "PushButton"))
        self.pushButton_12.setText(_translate("second_window", "wai wai"))
        self.pushButton3.setText(_translate("second_window", "PushButton"))
        self.treeWidget.headerItem().setText(0, _translate("second_window", "Cake"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("second_window", "Veg"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("second_window", "Non-veg"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget_2.headerItem().setText(0, _translate("second_window", "Packet-Sachet"))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("second_window", "Veg"))
        self.treeWidget_2.topLevelItem(1).setText(0, _translate("second_window", "Non-veg"))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.treeWidget_3.headerItem().setText(0, _translate("second_window", "Twin Sachet"))
        __sortingEnabled = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        self.treeWidget_3.topLevelItem(0).setText(0, _translate("second_window", "Veg"))
        self.treeWidget_3.topLevelItem(1).setText(0, _translate("second_window", "Non-veg"))
        self.treeWidget_3.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    second_window = QtWidgets.QWidget()
    ui = Ui_second_window()
    ui.setupUi(second_window)
    second_window.show()
    sys.exit(app.exec_())
