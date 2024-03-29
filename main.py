import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
from PyQt5.uic import loadUi
from login_window1 import Ui_Login_window
from opening_window import Ui_MainWindow
from download import Ui_Frame

class DownloadFrame(QWidget, Ui_Frame):
    def __init__(self):
        super(DownloadFrame, self).__init__()
        self.setupUi(self)


class Ui_MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        #download window button 
        self.Download_btn.clicked.connect(self.show_download_frame)
        #opening different widget Main_page
        self.cake_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.packet_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.twin_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.cake_btn2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.packet_btn2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.twin_btn2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.Home_btn1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1))
        self.Home_btn2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 2))
        ## item_page
        self.pushButton1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.pushButton2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.pushButton3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.pushButton4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.pushButton5.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.pushButton6.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.pushButton7.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.pushButton8.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.pushButton9.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.pushButton_10.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.pushButton_11.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
        self.pushButton_12.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1))
    
    def show_download_frame(self):
        # Create an instance of the download frame and show it
        self.w = DownloadFrame()
        self.w.show()

class LoginWindow(QMainWindow, Ui_Login_window):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.open_window)
        

    def open_window(self):
        USERNAME = self.username.text()
        PASSWORD = self.password.text()
        
        if self.username.text() == "admin" and self.password.text() == "pass123":
            self.opening_window = Ui_MainWindow()
            self.opening_window.show()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
