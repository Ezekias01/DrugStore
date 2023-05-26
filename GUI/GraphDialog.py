import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.uic import *
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtGui, QtCore

class GraphDialog(QDialog):
    def __init__(self):
        super(GraphDialog, self).__init__()
        loadUi("graphDialog.ui", self)
        self.showPlot = QLabel(self)
        self.showPlot.setAlignment(PyQt5.QtCore.Qt.AlignVCenter)

    def setGraph(self,title):
        self.pixmap1 = QPixmap(title)
        self.pixmap = self.pixmap1.scaled(600, 600, PyQt5.QtCore.Qt.KeepAspectRatio)
        self.showPlot.clear()
        self.showPlot.setPixmap(self.pixmap)
        self.showPlot.adjustSize()
        self.show()