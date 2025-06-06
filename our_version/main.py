from PyQt5.QtWidgets import QMainWindow, QApplication
from login import Ui_LoginWindow
import sys

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.beginLogin(self)  # Pass the window itself

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec_())
