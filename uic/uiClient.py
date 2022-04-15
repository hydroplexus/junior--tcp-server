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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelLog = QLabel(Form)
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

        self.teLog = QPlainTextEdit(Form)
        self.teLog.setObjectName(u"teLog")
        self.teLog.setEnabled(True)
        self.teLog.setFrameShape(QFrame.Box)
        self.teLog.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.teLog)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelStdOut = QLabel(Form)
        self.labelStdOut.setObjectName(u"labelStdOut")
        self.labelStdOut.setFont(font)
        self.labelStdOut.setAutoFillBackground(True)
        self.labelStdOut.setScaledContents(False)
        self.labelStdOut.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelStdOut)

        self.teStdOut = QPlainTextEdit(Form)
        self.teStdOut.setObjectName(u"teStdOut")
        self.teStdOut.setFrameShape(QFrame.Box)
        self.teStdOut.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.teStdOut)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.grpCustom = QGroupBox(Form)
        self.grpCustom.setObjectName(u"grpCustom")
        self.grpCustom.setEnabled(True)
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

        self.btnSrvStart = QPushButton(Form)
        self.btnSrvStart.setObjectName(u"btnSrvStart")
        self.btnSrvStart.setFlat(False)

        self.verticalLayout.addWidget(self.btnSrvStart)

        self.btnSrvStop = QPushButton(Form)
        self.btnSrvStop.setObjectName(u"btnSrvStop")
        self.btnSrvStop.setEnabled(False)
        self.btnSrvStop.setFlat(False)

        self.verticalLayout.addWidget(self.btnSrvStop)

        self.btnClientConnect = QPushButton(Form)
        self.btnClientConnect.setObjectName(u"btnClientConnect")
        self.btnClientConnect.setEnabled(False)
        self.btnClientConnect.setFlat(False)

        self.verticalLayout.addWidget(self.btnClientConnect)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.labelClient = QLabel(Form)
        self.labelClient.setObjectName(u"labelClient")
        self.labelClient.setEnabled(False)
        self.labelClient.setFont(font)
        self.labelClient.setAutoFillBackground(True)
        self.labelClient.setScaledContents(False)
        self.labelClient.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelClient)

        self.teClient = QPlainTextEdit(Form)
        self.teClient.setObjectName(u"teClient")
        self.teClient.setEnabled(False)
        self.teClient.setFrameShape(QFrame.Box)

        self.verticalLayout.addWidget(self.teClient)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelLog.setText(QCoreApplication.translate("Form", u"results.log", None))
        self.labelStdOut.setText(QCoreApplication.translate("Form", u"server stdout", None))
        self.grpCustom.setTitle(QCoreApplication.translate("Form", u"Use custom server params", None))
        self.linePort.setPlaceholderText(QCoreApplication.translate("Form", u"server port (:5000)", None))
        self.lineAddress.setInputMask("")
        self.lineAddress.setPlaceholderText(QCoreApplication.translate("Form", u"server address (0.0.0.0)", None))
        self.btnSrvStart.setText(QCoreApplication.translate("Form", u"Start server", None))
        self.btnSrvStop.setText(QCoreApplication.translate("Form", u"Stop server", None))
        self.btnClientConnect.setText(QCoreApplication.translate("Form", u"Connect client", None))
        self.labelClient.setText(QCoreApplication.translate("Form", u"client input", None))
    # retranslateUi

