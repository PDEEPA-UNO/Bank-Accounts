from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

class BankWindow(QWidget):
    """
    This class contains the managing bank account(s) window
    """
    def __init__(self, username):
        """
        Initializes the bank window
        :param username: The username of the person attempting to login
        """
        super().__init__()
        self.setWindowTitle(f"{username}'s Dashboard")
        self.setFixedSize(300, 350)

        self.layout = QVBoxLayout(self)

        self.welcome_label = QLabel(f"Welcome, {username}!")
        self.layout.addWidget(self.welcome_label)

        self.checking_balance_btn = QPushButton("View Checking Balance")
        self.saving_balance_btn = QPushButton("View Saving Balance")

        self.deposit_checking_btn = QPushButton("Deposit to Checking")
        self.withdraw_checking_btn = QPushButton("Withdraw from Checking")

        self.deposit_saving_btn = QPushButton("Deposit to Saving")
        self.withdraw_saving_btn = QPushButton("Withdraw from Saving")

        self.logout_btn = QPushButton("Logout")

        for btn in [
            self.checking_balance_btn,
            self.saving_balance_btn,
            self.deposit_checking_btn,
            self.withdraw_checking_btn,
            self.deposit_saving_btn,
            self.withdraw_saving_btn,
            self.logout_btn,
        ]:
            self.layout.addWidget(btn)
