from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from dashboard import Dashboard

class Ui_LoginWindow(object):
    def beginLogin(self, LoginWindow):
        LoginWindow.setWindowTitle("FNB - Login")
        LoginWindow.resize(1366, 768)  
        LoginWindow.setStyleSheet("background-color: #f5f5f5;")  # Light background

        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.setContentsMargins(100, 100, 100, 100)
        layout.setSpacing(20)

        # FNB Logo 
        self.logo = QtWidgets.QLabel()
        self.logo.setPixmap(QtGui.QPixmap("images/fnb_logo.png").scaled(300, 300, QtCore.Qt.KeepAspectRatio))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.logo)

        # Welcome label
        self.title = QtWidgets.QLabel("Welcome to FNB")
        self.title.setStyleSheet("font-size: 24px; font-weight: bold; color: #002663;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.title)

        # Username field
        self.username_input = QtWidgets.QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet("""
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
        """)
        layout.addWidget(self.username_input)

        # Password field
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setStyleSheet("""
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
        """)
        layout.addWidget(self.password_input)

        # Login button
        self.login_button = QtWidgets.QPushButton("Login")
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #FFD100;
                color: #002663;
                font-weight: bold;
                padding: 10px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #e6b800;
            }
        """)
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

