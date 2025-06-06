from PyQt5 import QtWidgets, QtGui, QtCore
from api_chatgpt import send_to_gpt
from response_page import ResponsePage
from history import save_to_history

class Eassist(QtWidgets.QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setWindowTitle(f"FNB e-Assist — Welcome {username}")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: #002663;
            }
            QLabel#headerLabel {
                font-size: 22px;
                font-weight: 700;
                margin-bottom: 15px;
                color: #002663;
            }
            QPushButton {
                background-color: #FFD100;
                border-radius: 8px;
                font-size: 16px;
                font-weight: 600;
                padding: 12px;
                color: #002663;
                transition: background-color 0.3s;
            }
            QPushButton:hover {
                background-color: #e6b800;
            }
            QLineEdit {
                padding: 10px;
                font-size: 16px;
                border: 2px solid #ccc;
                border-radius: 8px;
                margin-top: 15px;
                margin-bottom: 15px;
            }
            QLineEdit:focus {
                border-color: #FFD100;
            }
        """)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(40, 40, 40, 40)
        self.layout.setSpacing(20)

        self.logo = QtWidgets.QLabel()
        logo_pixmap = QtGui.QPixmap("images/fnb_logo.png")
        if not logo_pixmap.isNull():
            self.logo.setPixmap(logo_pixmap.scaled(120, 120, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            self.logo.setAlignment(QtCore.Qt.AlignCenter)
            self.layout.addWidget(self.logo)

        self.label = QtWidgets.QLabel("Choose a question or ask your own:")
        self.label.setObjectName("headerLabel")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Buttons for predefined questions with consistent styling
        question_texts = [
            "A. What is my current account balance?",
            "B. Show my recent transactions",
            "C. How can I open a savings account?",
            "D. Explain my credit card charges",
            "E. Help me set up a budget"
        ]

        self.buttons = []
        for q in question_texts:
            btn = QtWidgets.QPushButton(q)
            self.layout.addWidget(btn)
            self.buttons.append(btn)

        # Connect buttons to ask_gpt with proper question text
        self.buttons[0].clicked.connect(lambda: self.ask_gpt(question_texts[0][3:].strip()))
        self.buttons[1].clicked.connect(lambda: self.ask_gpt(question_texts[1][3:].strip()))
        self.buttons[2].clicked.connect(lambda: self.ask_gpt(question_texts[2][3:].strip()))
        self.buttons[3].clicked.connect(lambda: self.ask_gpt(question_texts[3][3:].strip()))
        self.buttons[4].clicked.connect(lambda: self.ask_gpt(question_texts[4][3:].strip()))

        # question input
        self.inputBox = QtWidgets.QLineEdit()
        self.inputBox.setPlaceholderText("Type your own question here...")
        self.layout.addWidget(self.inputBox)

        # Submit button for custom question
        self.submitBtn = QtWidgets.QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit_custom_question)
        self.layout.addWidget(self.submitBtn)

    def ask_gpt(self, question):
        response = send_to_gpt(question)
        save_to_history(question, response)
        self.response_window = ResponsePage(response)
        self.response_window.show()

    def submit_custom_question(self):
        question = self.inputBox.text().strip()
        if question:
            self.ask_gpt(question)
        else:
            QtWidgets.QMessageBox.warning(self, "Oops!", "Please enter a question first.")
