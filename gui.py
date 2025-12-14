from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton

class LoginWindow(QMainWindow):
    """
    This class contains the login or create new user window
    """
    def __init__(self):
        """
        Initializes the login window
        """
        super().__init__()
        self.setWindowTitle("Bank Login")
        self.setFixedSize(300, 250)

        self.username_label = QLabel("Username:", self)
        self.username_label.setGeometry(20, 20, 100, 30)

        self.username_input = QLineEdit(self)
        self.username_input.setGeometry(120, 20, 150, 30)

        self.password_label = QLabel("Password:", self)
        self.password_label.setGeometry(20, 60, 100, 30)

        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(120, 60, 150, 30)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.setGeometry(50, 120, 90, 40)

        self.create_button = QPushButton("Create New User", self)
        self.create_button.setGeometry(160, 120, 120, 40)