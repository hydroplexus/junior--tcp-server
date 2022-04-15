# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiClient.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_JuniorTcpServer(object):
    def setupUi(self, JuniorTcpServer):
        if not JuniorTcpServer.objectName():
            JuniorTcpServer.setObjectName(u"JuniorTcpServer")
        JuniorTcpServer.resize(640, 480)
        self.verticalLayout_5 = QVBoxLayout(JuniorTcpServer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelLog = QLabel(JuniorTcpServer)
        self.labelLog.setObjectName(u"labelLog")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setKerning(True)
        self.labelLog.setFont(font)
        self.labelLog.setAutoFillBackground(True)
        self.labelLog.setScaledContents(False)
        self.labelLog.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelLog)

        self.teLog = QPlainTextEdit(JuniorTcpServer)
        self.teLog.setObjectName(u"teLog")
        self.teLog.setEnabled(True)
        self.teLog.setFrameShape(QFrame.Box)
        self.teLog.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.teLog)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelStdOut = QLabel(JuniorTcpServer)
        self.labelStdOut.setObjectName(u"labelStdOut")
        self.labelStdOut.setFont(font)
        self.labelStdOut.setAutoFillBackground(True)
        self.labelStdOut.setScaledContents(False)
        self.labelStdOut.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelStdOut)

        self.teStdOut = QPlainTextEdit(JuniorTcpServer)
        self.teStdOut.setObjectName(u"teStdOut")
        self.teStdOut.setFrameShape(QFrame.Box)
        self.teStdOut.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.teStdOut)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.grpCustom = QGroupBox(JuniorTcpServer)
        self.grpCustom.setObjectName(u"grpCustom")
        self.grpCustom.setEnabled(True)
        self.grpCustom.setStyleSheet(u"")
        self.grpCustom.setFlat(True)
        self.grpCustom.setCheckable(True)
        self.grpCustom.setChecked(False)
        self.gridLayout_2 = QGridLayout(self.grpCustom)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.linePort = QLineEdit(self.grpCustom)
        self.linePort.setObjectName(u"linePort")
        self.linePort.setEnabled(True)

        self.gridLayout_2.addWidget(self.linePort, 1, 0, 1, 1)

        self.lineAddress = QLineEdit(self.grpCustom)
        self.lineAddress.setObjectName(u"lineAddress")
        self.lineAddress.setEnabled(True)

        self.gridLayout_2.addWidget(self.lineAddress, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.grpCustom)

        self.btnSrvStart = QPushButton(JuniorTcpServer)
        self.btnSrvStart.setObjectName(u"btnSrvStart")
        self.btnSrvStart.setFlat(False)

        self.verticalLayout.addWidget(self.btnSrvStart)

        self.btnSrvStop = QPushButton(JuniorTcpServer)
        self.btnSrvStop.setObjectName(u"btnSrvStop")
        self.btnSrvStop.setEnabled(False)
        self.btnSrvStop.setFlat(False)

        self.verticalLayout.addWidget(self.btnSrvStop)

        self.line = QFrame(JuniorTcpServer)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.btnConnectTelnet = QPushButton(JuniorTcpServer)
        self.btnConnectTelnet.setObjectName(u"btnConnectTelnet")
        self.btnConnectTelnet.setEnabled(False)
        self.btnConnectTelnet.setFlat(False)

        self.verticalLayout.addWidget(self.btnConnectTelnet)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.retranslateUi(JuniorTcpServer)

        QMetaObject.connectSlotsByName(JuniorTcpServer)
    # setupUi

    def retranslateUi(self, JuniorTcpServer):
        JuniorTcpServer.setWindowTitle(QCoreApplication.translate("JuniorTcpServer", u"Form", None))
        self.labelLog.setText(QCoreApplication.translate("JuniorTcpServer", u"results.log", None))
        self.labelStdOut.setText(QCoreApplication.translate("JuniorTcpServer", u"server stdout", None))
        self.grpCustom.setTitle(QCoreApplication.translate("JuniorTcpServer", u"Use custom server params", None))
        self.linePort.setPlaceholderText(QCoreApplication.translate("JuniorTcpServer", u"server port (:5000)", None))
        self.lineAddress.setInputMask("")
        self.lineAddress.setPlaceholderText(QCoreApplication.translate("JuniorTcpServer", u"server address (0.0.0.0)", None))
        self.btnSrvStart.setText(QCoreApplication.translate("JuniorTcpServer", u"Start server", None))
        self.btnSrvStop.setText(QCoreApplication.translate("JuniorTcpServer", u"Stop server", None))
        self.btnConnectTelnet.setText(QCoreApplication.translate("JuniorTcpServer", u"Connect telnet", None))
    # retranslateUi

