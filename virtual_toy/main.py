from PyQt5 import QtWidgets
from virtual_toy.dashboard import Dashboard
import sys

def launch():
    app = QtWidgets.QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    launch()
