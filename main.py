import sys
from PyQt5.QtWidgets import *
from GUI.LoginScreen import LoginScreen

#main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginScreen()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
