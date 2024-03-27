import sys
from opening_window import Ui_MainWindow
from second_window import Ui_second_window
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.uic import loadUi



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi('opening_window.ui', self)  # Load the UI file into the main window
        self.cake_btn.clicked.connect(self.open_window)

    def open_window(self):
        print('i gotcha you')
        
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        loadUi('second_window.ui', self)  # Load the UI file into the second window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    #second_window = Ui_second_window()
    #second_window.show()
    main_window.show()
    sys.exit(app.exec_())
