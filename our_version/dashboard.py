from PyQt5 import QtWidgets
from api_chatgpt import send_to_gpt
from response_page import ResponsePage
from history import save_to_history

class Dashboard(QtWidgets.QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setWindowTitle(f"Welcome {username}")
        self.setGeometry(100, 100, 500, 400)

        self.layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel("Choose a question or ask your own:")
        self.layout.addWidget(self.label)

        # Predefined Questions A–E
        self.btnA = QtWidgets.QPushButton("A. What is my current account balance?")
        self.btnB = QtWidgets.QPushButton("B. Show my recent transactions")
        self.btnC = QtWidgets.QPushButton("C. How can I open a savings account?")
        self.btnD = QtWidgets.QPushButton("D. Explain my credit card charges")
        self.btnE = QtWidgets.QPushButton("E. Help me set up a budget")

        for btn in [self.btnA, self.btnB, self.btnC, self.btnD, self.btnE]:
            self.layout.addWidget(btn)

        # Connect buttons
        self.btnA.clicked.connect(lambda: self.ask_gpt("What is my current account balance?"))
        self.btnB.clicked.connect(lambda: self.ask_gpt("Show my recent transactions"))
        self.btnC.clicked.connect(lambda: self.ask_gpt("How can I open a savings account?"))
        self.btnD.clicked.connect(lambda: self.ask_gpt("Explain my credit card charges"))
        self.btnE.clicked.connect(lambda: self.ask_gpt("Help me set up a budget"))

        # Custom user question input
        self.inputBox = QtWidgets.QLineEdit()
        self.inputBox.setPlaceholderText("Type your own question here...")
        self.layout.addWidget(self.inputBox)

        self.submitBtn = QtWidgets.QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit_custom_question)
        self.layout.addWidget(self.submitBtn)

        self.setLayout(self.layout)

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
