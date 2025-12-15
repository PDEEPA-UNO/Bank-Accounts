from PyQt6.QtWidgets import QMessageBox, QInputDialog
from gui import LoginWindow
from bank_window import BankWindow

login_view = None
bankwindow_view = None
users = {}
current_user = None

def setup_app() -> None:
    """
    Connects the buttons to logic for login page
    """
    global login_view
    login_view = LoginWindow()
    login_view.login_button.clicked.connect(handle_login)
    login_view.create_button.clicked.connect(create_user)

def show_login() -> None:
    """
    Display the login window
    """
    login_view.show()

def handle_login() -> None:
    """
    Handles the login information provided, including any invalid entries
    """
    global current_user, bankwindow_view

    username = login_view.username_input.text().strip()
    password = login_view.password_input.text().strip()

    if username in users and users[username]["password"] == password:
        current_user = username
        open_dashboard()
        login_view.close()
    else:
        QMessageBox.warning(login_view, "Login Failed", "Invalid username or password")

def create_user() -> None:
    username, ok = QInputDialog.getText(login_view, "Create User", "Username:")
    if not ok or not username.strip():
        return

    if username in users:
        QMessageBox.warning(login_view, "Error", "Username already exists")
        return

    password, ok = QInputDialog.getText(login_view, "Create User", "Password:")
    if ok and password.strip():
        users[username] = {"password": password, "checking": 0.0, "saving": 100.0}
        QMessageBox.information(login_view, "Success", "User created successfully")

def open_dashboard() -> None:
    """
    Connects the buttons to logic for dashboard/ bank page
    :return:
    """
    global bankwindow_view
    bankwindow_view = BankWindow(current_user)

    bankwindow_view.checking_balance_btn.clicked.connect(lambda: show_balance("checking"))
    bankwindow_view.saving_balance_btn.clicked.connect(lambda: show_balance("saving"))
    bankwindow_view.deposit_checking_btn.clicked.connect(lambda: deposit("checking"))
    bankwindow_view.withdraw_checking_btn.clicked.connect(lambda: withdraw("checking"))
    bankwindow_view.deposit_saving_btn.clicked.connect(lambda: deposit("saving"))
    bankwindow_view.withdraw_saving_btn.clicked.connect(lambda: withdraw("saving"))
    bankwindow_view.logout_btn.clicked.connect(logout)

    bankwindow_view.show()

def show_balance(account) -> None:
    """
    Displays account balance
    :param account: (str) Either the "checking" or "saving" account
    """
    balance = users[current_user][account]
    QMessageBox.information(bankwindow_view, "Balance", f"{account.capitalize()} Balance: ${balance:.2f}")

def deposit(account) -> None:
    """
    Handles depositing amount logic
    :param account: (str) Either the "checking" or "saving" account
    """
    amount, ok = QInputDialog.getDouble(bankwindow_view, "Deposit", "Amount:", 0, 0)
    if ok and amount > 0:
        users[current_user][account] += amount
        QMessageBox.information(bankwindow_view, "Success", "Deposit successful")

def withdraw(account) -> None:
    """
    Handles withdraw logic
    :param account: (str) Either the "checking" or "saving" account
    """
    if not current_user or not bankwindow_view:
        return

    amount, ok = QInputDialog.getDouble(
        bankwindow_view,
        "Withdraw",
        f"Amount to withdraw from {account}:",
        0,
        0
    )

    if not ok:
        return

    current_balance = users[current_user][account]

    if account == "saving" and current_balance - amount < 100:
        QMessageBox.warning(
            bankwindow_view,
            "Error",
            "Cannot withdraw. Savings account must maintain a minimum balance of $100."
        )
        return

    if 0 < amount <= current_balance:
        users[current_user][account] -= amount
        QMessageBox.information(
            bankwindow_view,
            "Success",
            f"Withdrawal of ${amount:.2f} successful."
        )
    else:
        QMessageBox.warning(
            bankwindow_view,
            "Error",
            "Invalid withdrawal amount"
        )

def logout() -> None:
    """
    Logs out the user once logout button is pressed
    """
    global current_user
    bankwindow_view.close()
    current_user = None
    show_login()