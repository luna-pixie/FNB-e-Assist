from PyQt5.QtWidgets import QApplication, QMainWindow
from login import Ui_LoginWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    LoginWindow = QMainWindow()
    ui = Ui_LoginWindow()
    ui.beginLogin(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
