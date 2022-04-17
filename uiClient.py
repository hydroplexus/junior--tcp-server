#!/usr/bin/python

import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, QProcess, QFile, QTextStream

from server import JServer
from uic.uiClient import Ui_JuniorTcpServer
#TODO: change server instance from QProcess/server.py to QThread/Server::
#from server import Server

class MainWidget(QWidget):
    class HBridge(JServer.HJServerBridge, QObject):
        #SIGNALS
        onMatchSignal = QtCore.Signal(str)
        onCatchSignal = QtCore.Signal(str)
        
        def __init__(self, parent) -> None:
            super(QObject).__init__(parent)
            
        @classmethod
        def onMatch(self, data: str) -> None:
            self.onMatch.emit(data)
            
        @classmethod
        def onCatch(self, data: str) -> None:
            self.onCatch.emit(data)
        
    SRV_ADDRESS_DEFAULT = '0.0.0.0'
    SRV_PORT_DEFAULT = 5000
    LOG_FILE_NAME = './results.log'
    SRV_FILE_NAME = './server.py'
    
    srv: JServer
    srvProcess = QProcess()
    srvAddress = ''
    srvPort = None
    srvIsCustom = False
    srvIsRunning = False
    logStream = QTextStream()
    
    #SIGNALS
    
    
    def __init__(self):
        super(MainWidget, self).__init__()
        self.ui = Ui_JuniorTcpServer()
        self.ui.setupUi(self)
        self.setUiLogic()
        self.setConnects()
        
    def setUiLogic(self):
        logFile = QFile(self.LOG_FILE_NAME)
        logFile.open(QFile.ReadOnly)
        self.logStream.setDevice(logFile)
        self.updateLog()
        self.ui.grpCustom.setChecked(self.srvIsCustom)
        
        self.srvProcess.setProgram('python3')
        self.srvProcess.setArguments({self.SRV_FILE_NAME})
    
    def setConnects(self):
        self.HBridge.onMatchSignal.connect(self.onMatchSlot)
        self.HBridge.onMatchSignal.connect(self.onCatchSlot)
        self.ui.grpCustom.toggled.connect(self.slotCustomToggled)
        self.ui.btnSrvStart.clicked.connect(self.slotStartSrv)
        self.ui.btnSrvStop.clicked.connect(self.slotStopSrv)
        self.ui.btnConnectTelnet.clicked.connect(self.slotConnectTelnet)

    def updateLog(self):
        while not self.logStream.atEnd():
            self.ui.teLog.appendPlainText(self.logStream.readLine())
            
    def srvToggle(self):
        self.srvIsRunning = False if self.srvProcess.state() == 0 else True
        self.ui.grpCustom.setEnabled(not self.srvIsRunning)
        self.ui.btnSrvStop.setEnabled(self.srvIsRunning)
        self.ui.btnConnectTelnet.setEnabled(self.srvIsRunning)
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
            #FIXME: set default values lineAddress/linePort after filds clearing
                self.srvProcess.setArguments({'--address', self.ui.lineAddress.text()})
                self.srvProcess.setArguments({'--port', self.ui.linePort.text.toint()})
            self.srvProcess.start()
        except Exception as exception:
            print(exception)
        finally:
            pass
        self.srvToggle()
    
    def slotStopSrv(self):
        self.srvProcess.terminate()
        self.srvProcess.waitForFinished()
        self.srvToggle()
    
    def slotConnectTelnet(self):
        pass  
    
    def onMatcSlot(self, data:str) -> None:
        print('MATCHED')
    
    def onCatchSlot(self, data:str) -> None:
        print('CATCHED')
       
def main():
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.setWindowTitle('JuniorTcpServer -- shakhov-vy')
    widget.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()