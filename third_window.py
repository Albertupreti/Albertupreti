


from PyQt5 import QtCore, QtGui, QtWidgets

#testing 
class Ui_third_window(object):
    def setupUi(self, third_window):
        third_window.setObjectName("third_window")
        third_window.resize(800, 600)
        third_window.setMinimumSize(QtCore.QSize(800, 600))
        third_window.setStyleSheet("background-color: rgb(160, 193, 223);\n""")
        self.horizontalLayoutWidget = QtWidgets.QWidget(third_window)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 761, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(458, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.line = QtWidgets.QFrame(third_window)
        self.line.setGeometry(QtCore.QRect(20, 90, 760, 20))
        self.line.setMinimumSize(QtCore.QSize(700, 16))
        self.line.setMaximumSize(QtCore.QSize(760, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(third_window)
        self.line_2.setGeometry(QtCore.QRect(140, 100, 20, 500))
        self.line_2.setMinimumSize(QtCore.QSize(16, 461))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame = QtWidgets.QFrame(third_window)
        self.frame.setGeometry(QtCore.QRect(10, 110, 131, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        self.treeWidget.setGeometry(QtCore.QRect(0, 10, 131, 81))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.frame)
        self.treeWidget_2.setGeometry(QtCore.QRect(0, 90, 131, 81))
        self.treeWidget_2.setObjectName("treeWidget_2")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        self.label_3 = QtWidgets.QLabel(third_window)
        self.label_3.setGeometry(QtCore.QRect(220, 120, 331, 17))
        self.label_3.setObjectName("label_3")
        self.line_3 = QtWidgets.QFrame(third_window)
        self.line_3.setGeometry(QtCore.QRect(220, 140, 581, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_4 = QtWidgets.QLabel(third_window)
        self.label_4.setGeometry(QtCore.QRect(730, 117, 41, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(third_window)
        self.label_5.setGeometry(QtCore.QRect(710, 120, 21, 16))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("home_icon.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.graphicsView = QtWidgets.QGraphicsView(third_window)
        self.graphicsView.setGeometry(QtCore.QRect(400, 160, 391, 61))
        self.graphicsView.setStyleSheet("background-color: rgb(246, 97, 81);")
        self.graphicsView.setObjectName("graphicsView")
        self.label_6 = QtWidgets.QLabel(third_window)
        self.label_6.setGeometry(QtCore.QRect(460, 169, 281, 41))
        self.label_6.setStyleSheet("background-color: rgb(246, 97, 81);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.groupBox = QtWidgets.QGroupBox(third_window)
        self.groupBox.setGeometry(QtCore.QRect(400, 230, 381, 211))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 50, 171, 131))
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(30, 30, 91, 71))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(third_window)
        QtCore.QMetaObject.connectSlotsByName(third_window)

    def retranslateUi(self, third_window):
        _translate = QtCore.QCoreApplication.translate
        third_window.setWindowTitle(_translate("third_window", "Form"))
        self.label.setText(_translate("third_window", "Crimson Tech"))
        self.label_2.setText(_translate("third_window", "Production 1"))
        self.treeWidget.headerItem().setText(0, _translate("third_window", "Veg"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("third_window", "Cake"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("third_window", "Packet Sachet"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("third_window", "Twin Sachet"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget_2.headerItem().setText(0, _translate("third_window", "Non-Veg"))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("third_window", "Cake"))
        self.treeWidget_2.topLevelItem(1).setText(0, _translate("third_window", "Packet Sachet"))
        self.treeWidget_2.topLevelItem(2).setText(0, _translate("third_window", "Twin Sachet"))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("third_window", "Non-veg > Twin Sachet >  Wai Wai Chicken 60 gm"))
        self.label_4.setText(_translate("third_window", "Home"))
        self.label_6.setText(_translate("third_window", "Wai Wai Chicken 60 gm"))
        self.groupBox.setTitle(_translate("third_window", "weight"))
        self.label_7.setText(_translate("third_window", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    third_window = QtWidgets.QWidget()
    ui = Ui_third_window()
    ui.setupUi(third_window)
    third_window.show()
    sys.exit(app.exec_())
