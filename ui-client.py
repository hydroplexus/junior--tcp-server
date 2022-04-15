#!/usr/bin/python

import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile

from uic.ui-client import Ui_Form

from server import Server

class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUI(self)
        
        
if __name__ == 'main':
    app = QApplication(sys.argv)
    
    widget = MainWidget()
    widget.show()
    
    sys.exit(app.exec())
