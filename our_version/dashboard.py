from PyQt5 import QtCore, QtGui, QtWidgets
from e_Assist import Eassist

class Dashboard(QtWidgets.QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setWindowTitle("FNB e-Assist Dashboard")
        self.setFixedSize(1366, 768)  # FIXED size window
        self.setStyleSheet("background-color: white;")

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QtWidgets.QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # TOP IMAGE - fixed height
        self.top_image = QtWidgets.QLabel()
        top_pixmap = QtGui.QPixmap("images/top_desktop.png")
        scaled_top = top_pixmap.scaledToWidth(1366, QtCore.Qt.SmoothTransformation)
        self.top_image.setPixmap(scaled_top)
        self.top_image.setFixedHeight(436)  #
        self.top_image.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        main_layout.addWidget(self.top_image)

        # BUTTON - center aligned
        self.ask_button = QtWidgets.QPushButton("Ask E-Assist")
        self.ask_button.setFixedSize(700, 70)  # Wider button
        self.ask_button.setStyleSheet("""
            QPushButton {
                background-color: #FFD100;
                color: #002663;
                font-size: 24px;
                font-weight: bold;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #e6b800;
            }
        """)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.ask_button)
        button_layout.addStretch()
        main_layout.addLayout(button_layout)

        # Spacer to push the bottom image to bottom
        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        main_layout.addItem(spacer)

        # BOTTOM IMAGE - fixed height 250 (adjusted size)
        self.bottom_image = QtWidgets.QLabel()
        bottom_pixmap = QtGui.QPixmap("images/bottom_widgets.jpg")  # Adjusted to 1366x250 in your editor
        scaled_bottom = bottom_pixmap.scaled(1366, 250, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        self.bottom_image.setPixmap(scaled_bottom)
        self.bottom_image.setFixedHeight(250)
        self.bottom_image.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.bottom_image)

        self.ask_button.clicked.connect(self.open_e_assist_feature)

    def open_e_assist_feature(self):
        self.e_assist_window = Eassist(username=self.username)
        self.e_assist_window.show()
