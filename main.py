import sys
from PyQt6.QtWidgets import QApplication
import logic

def main() -> None:
    """
    Launches the login window
    """
    app = QApplication(sys.argv)
    logic.setup_app()
    logic.show_login()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
