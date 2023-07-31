# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'soar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1033, 741)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Map = QOpenGLWidget(self.centralwidget)
        self.Map.setObjectName(u"Map")
        self.Map.setGeometry(QRect(20, 20, 431, 301))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 340, 431, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.PointCloud = QOpenGLWidget(self.centralwidget)
        self.PointCloud.setObjectName(u"PointCloud")
        self.PointCloud.setGeometry(QRect(20, 380, 431, 301))
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(710, 50, 291, 91))
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(520, 60, 121, 81))
        self.lcdNumber_2 = QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(520, 240, 121, 81))
        self.lcdNumber_3 = QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setGeometry(QRect(690, 240, 121, 81))
        self.lcdNumber_4 = QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        self.lcdNumber_4.setGeometry(QRect(870, 240, 121, 81))
        self.Trajectory = QOpenGLWidget(self.centralwidget)
        self.Trajectory.setObjectName(u"Trajectory")
        self.Trajectory.setGeometry(QRect(550, 380, 431, 301))
        self.Altitude = QTextEdit(self.centralwidget)
        self.Altitude.setObjectName(u"Altitude")
        self.Altitude.setGeometry(QRect(530, 150, 104, 31))
        self.Altitude_2 = QTextEdit(self.centralwidget)
        self.Altitude_2.setObjectName(u"Altitude_2")
        self.Altitude_2.setGeometry(QRect(530, 330, 104, 31))
        self.Altitude_3 = QTextEdit(self.centralwidget)
        self.Altitude_3.setObjectName(u"Altitude_3")
        self.Altitude_3.setGeometry(QRect(700, 330, 104, 31))
        self.Altitude_4 = QTextEdit(self.centralwidget)
        self.Altitude_4.setObjectName(u"Altitude_4")
        self.Altitude_4.setGeometry(QRect(880, 330, 104, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1033, 22))
        self.menuSoar_ver_01 = QMenu(self.menubar)
        self.menuSoar_ver_01.setObjectName(u"menuSoar_ver_01")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSoar_ver_01.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Altitude.setDocumentTitle("")
        self.Altitude.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.Altitude_2.setDocumentTitle("")
        self.Altitude_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Vx</p></body></html>", None))
        self.Altitude_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.Altitude_3.setDocumentTitle("")
        self.Altitude_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Vy</p></body></html>", None))
        self.Altitude_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.Altitude_4.setDocumentTitle("")
        self.Altitude_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Vz</p></body></html>", None))
        self.Altitude_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.menuSoar_ver_01.setTitle(QCoreApplication.translate("MainWindow", u"Soar_ver_01", None))
    # retranslateUi

