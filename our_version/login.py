from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from dashboard import Dashboard

class Ui_LoginWindow(object):
    def beginLogin(self, LoginWindow):
        LoginWindow.setWindowTitle("Login Page")
        LoginWindow.resize(400, 250)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)

        layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.username_input = QtWidgets.QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_button = QtWidgets.QPushButton("Login")
        layout.addWidget(self.login_button)

        LoginWindow.setCentralWidget(self.centralwidget)
        self.login_button.clicked.connect(self.login_user)

    def login_user(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "1234":
            self.open_dashboard()
        else:
            self.show_message("Error", "Invalid credentials!")

    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    def open_dashboard(self):
        self.window = Dashboard(self.username_input.text())
        self.window.show()
        self.centralwidget.window().close() 


