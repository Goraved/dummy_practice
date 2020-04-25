import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication, QLabel, QMessageBox


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.window_property = (50, 50, 500, 500)
        self.window_title = 'PyQT test'
        self.main_label = None
        self.close_btn = None
        self.main_window_init()

    def main_window_init(self):
        self.setGeometry(*self.window_property)
        self.setWindowTitle(self.window_title)
        self.close_button_init()
        self.main_label_init()
        self.show()

    def main_label_init(self):
        self.main_label = QLabel(self)
        self.main_label.setText('My first PyQT test app')
        self.main_label.setGeometry(2, 1, 400, 100)
        self.main_label.show()

    def close_button_init(self):
        self.close_btn = QPushButton('PyQt5 button', self)
        self.close_btn.setText('Quit')
        self.close_btn.setGeometry(200, 200, 100, 100)
        self.close_btn.clicked.connect(self.close_app)

    @pyqtSlot()
    def close_app(self):
        close_message = QMessageBox.question(self, 'Close App?', 'Are you sure you wanna close app?', QMessageBox.Yes,
                                             QMessageBox.No)
        if close_message == QMessageBox.Yes:
            QMessageBox.warning(self, 'Kurwa', 'Kurwa!')
            self.close()
        else:
            QMessageBox.about(self, 'OK', "Dat's right")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
