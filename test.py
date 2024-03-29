import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowTitle("Names from Database")
        self.setGeometry(100, 100, 400, 300)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.verticalLayout = QVBoxLayout(self.centralWidget)

        # Connect to the SQLite database
        self.conn = sqlite3.connect('your_database.db')
        self.cursor = self.conn.cursor()

        # Create buttons and load names from the database
        self.create_buttons()

    def create_buttons(self):
        # Example query to fetch names from a 'names' table
        self.cursor.execute("SELECT name FROM names LIMIT 5")
        names = self.cursor.fetchall()

        for name in names:
            button = QPushButton(name[0], self.centralWidget)
            self.verticalLayout.addWidget(button)
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
