from PyQt5 import QtWidgets

class ResponsePage(QtWidgets.QWidget):
    def __init__(self, response_text, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Response Page")
        self.resize(400, 300)

        layout = QtWidgets.QVBoxLayout(self)

        self.label = QtWidgets.QLabel("Response from AI Teller:")
        layout.addWidget(self.label)

        self.textbox = QtWidgets.QTextEdit()
        self.textbox.setReadOnly(True)
        self.textbox.setText(response_text)
        layout.addWidget(self.textbox)
