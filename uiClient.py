#!/usr/bin/python

import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QProcess, QFile, QTextStream

from uic.uiClient import Ui_Form
#TODO: change server instance from QProcess/server.py to QThread/Server::
#from server import Server

class MainWidget(QWidget):
    
    logFile = QFile('./results.log')
    logStream = QTextStream()
    srvFile = './server.py'
    srvProcess = QProcess()
    srvIsCustom = False
    srvIsRunning = False
    
    #SIGNALS
    
    def __init__(self):
        super(MainWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setUiLogic()
        self.setConnects()
        
    def setUiLogic(self):
        self.logFile.open(QFile.ReadOnly)
        self.logStream.setDevice(self.logFile)
        self.updateLog()
        self.ui.grpCustom.setChecked(self.srvIsCustom)
        
        self.srvProcess.setProgram('python3')
        self.srvProcess.setArguments({self.srvFile})
    
    def setConnects(self):
        self.ui.grpCustom.toggled.connect(self.slotCustomToggled)
        self.ui.btnSrvStart.clicked.connect(self.slotStartSrv)
        self.ui.btnSrvStop.clicked.connect(self.slotStopSrv)

    def updateLog(self):
        while not self.logStream.atEnd():
            self.ui.teLog.appendPlainText(self.logStream.readLine())
            
    def srvToggle(self):
        self.srvIsRunning = False if self.srvProcess.state() == 0 else True
        print(self.srvIsRunning)
        self.ui.grpCustom.setEnabled(not self.srvIsRunning)
        self.ui.btnSrvStop.setEnabled(self.srvIsRunning)
        self.ui.btnClientConnect.setEnabled(self.srvIsRunning)
        self.ui.btnSrvStart.setEnabled(not self.srvIsRunning)
     
    def closeEvent(self, event):
        self.slotStopSrv()
        event.accept()
                
#SLOTS
    def slotCustomToggled(self, on):
        self.srvIsCustom = on
    
    def slotStartSrv(self):
        #FIXME: prevent server start with incorrect arguments through fallback them to defaults
        try:
            if self.srvIsCustom:
            #FIXME: set default values lineAddress/linePort after clear fields
                self.srvProcess.setArguments({'--address', self.ui.lineAddress.text()})
                self.srvProcess.setArguments({'--port', self.ui.linePort.text.toint()})
            self.srvProcess.start()
        except Exception as exception:
            print(exception)
        finally:
            pass
        
        self.srvToggle()
    
    def slotStopSrv(self):
        #FIXME: wait for srv process finishes correctly
        self.srvProcess.terminate()
        self.srvToggle()
            
       
def main():
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()