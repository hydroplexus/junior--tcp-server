#!/usr/bin/python

import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QProcess
from PySide6.QtCore import QFile, QFileSystemWatcher, QTextStream

from uic.uiClient import Ui_JuniorTcpServer
#TODO: change server instance from QProcess/server.py to QThread/Server::
#from server import Server

class MainWidget(QWidget):
    
    def __initAttributes(self) -> None:
        self.__SRV_HOST_DEFAULT = '0.0.0.0'
        self.__SRV_PORT_DEFAULT = 50000
        self.__LOG_FILE_NAME = './results.log'
        self.__SRV_FILE_NAME = './server.py'
        
        self.__srvProcess = QProcess()
        self.__srvAddress: str
        self.__srvPort: int
        self.__srvIsCustom = False
        self.__srvIsRunning = False
        self.__logWatcher = QFileSystemWatcher()
        self.__logStream = QTextStream()
        
    def __init__(self) -> None:
        super(MainWidget, self).__init__()
        self.ui = Ui_JuniorTcpServer()
        self.ui.setupUi(self)
        self.__initAttributes()
        self.__initUi()
        self.__initConnections()
        
    def __initUi(self) -> None:
        logFile = QFile(self.__LOG_FILE_NAME)
        logFile.open(QFile.ReadOnly)
        self.__logStream.setDevice(logFile)
        self.slotUpdateLog()
        self.__srvProcess.setProgram('python')
        self.__srvProcess.setProcessChannelMode(QProcess.ForwardedChannels)
        self.ui.lineHost.setPlaceholderText(f'default Host is: {self.__SRV_HOST_DEFAULT}')
        self.ui.linePort.setPlaceholderText(f'default Port is: {self.__SRV_PORT_DEFAULT}')
        self.ui.grpCustom.setChecked(self.__srvIsCustom)
        self.__logWatcher.addPath(self.__LOG_FILE_NAME)
    
    def __initConnections(self) -> None:
        self.ui.grpCustom.toggled.connect(self.slotCustomToggled)
        self.ui.btnSrvStart.clicked.connect(self.slotStartSrv)
        self.ui.btnSrvStop.clicked.connect(self.slotStopSrv)
        self.ui.btnConnectTelnet.clicked.connect(self.slotConnectTelnet)
        self.__srvProcess.readyRead.connect(self.slotSrvSTDOUT)
        self.__srvProcess.readyReadStandardOutput.connect(self.slotSrvSTDOUT)
        self.__srvProcess.readyReadStandardError.connect(self.slotSrvSTDOUT)
        self.__logWatcher.fileChanged.connect(self.slotUpdateLog)

            
    def srvToggle(self) -> None:
        self.__srvIsRunning = False if self.__srvProcess.state() == 0 else True
        self.ui.grpCustom.setEnabled(not self.__srvIsRunning)
        self.ui.btnSrvStop.setEnabled(self.__srvIsRunning)
        self.ui.btnConnectTelnet.setEnabled(self.__srvIsRunning)
        self.ui.btnSrvStart.setEnabled(not self.__srvIsRunning)
     
    def closeEvent(self, event) -> None:
        self.slotStopSrv()
        event.accept()
                
#SLOTS
    def slotCustomToggled(self, on) ->None:
        self.__srvIsCustom = on
    
    def slotStartSrv(self) -> None:
        host = self.__SRV_HOST_DEFAULT
        port = self.__SRV_PORT_DEFAULT
        if self.__srvIsCustom:
            host = self.ui.lineHost.text()
            port = self.ui.linePort.text()
        self.__srvProcess.setArguments([self.__SRV_FILE_NAME, '--host', host, '--port', str(port)])
        self.__srvProcess.start()
        if self.__srvProcess.waitForStarted():
            self.srvToggle()
    
    def slotStopSrv(self) -> None:
        self.__srvProcess.kill()
        self.__srvProcess.waitForFinished()
        self.srvToggle()
    
    def slotConnectTelnet(self) -> None:
        pass  
    
    def slotUpdateLog(self) -> None:
        while not self.__logStream.atEnd():
            self.ui.teLog.appendPlainText(self.__logStream.readLine())
            
    def slotSrvSTDOUT(self) -> None:
        print('INCOME---')
        self.ui.teStdOut.appendPlainText(self.__srvProcess.readAllErrorOutput())
    
    def slotSrvSTDERR(self) -> None:
        pass
    
    
def main():
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.setWindowTitle('JuniorTcpServer -- shakhov-vy')
    widget.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()