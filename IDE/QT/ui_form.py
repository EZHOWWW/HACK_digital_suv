# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QTabWidget, QToolButton, QWidget)

class Ui_ADRudion(object):
    def setupUi(self, ADRudion):
        if not ADRudion.objectName():
            ADRudion.setObjectName(u"ADRudion")
        ADRudion.resize(1600, 900)
        ADRudion.setAutoFillBackground(False)
        ADRudion.setStyleSheet(u"background-color:#f4f2ed; \n"
"color:#181617;\n"
"")
        self.centralwidget = QWidget(ADRudion)
        self.centralwidget.setObjectName(u"centralwidget")
        self.File = QToolButton(self.centralwidget)
        self.File.setObjectName(u"File")
        self.File.setGeometry(QRect(0, 0, 100, 50))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.File.setFont(font)
        self.File.setAutoFillBackground(False)
        self.File.setStyleSheet(u"background-color:#849bfb; \\n\n"
"color: #181617; \\n\n"
"\n"
"")
        self.Settings = QToolButton(self.centralwidget)
        self.Settings.setObjectName(u"Settings")
        self.Settings.setGeometry(QRect(100, 0, 100, 50))
        self.Settings.setFont(font)
        self.Settings.setAutoFillBackground(False)
        self.Settings.setStyleSheet(u"background-color:#fb9c84; \\n\n"
"color: #181617; \\n\n"
"\n"
"")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 50, 1600, 760))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.tabWidget.setFont(font1)
        self.tabWidget.setStyleSheet(u"background-color:#f4f2ed; \n"
"color:#181617;\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.BlockS = QWidget()
        self.BlockS.setObjectName(u"BlockS")
        self.BlockswebEngineView = QWebEngineView(self.BlockS)
        self.BlockswebEngineView.setObjectName(u"BlockswebEngineView")
        self.BlockswebEngineView.setEnabled(True)
        self.BlockswebEngineView.setGeometry(QRect(0, 0, 1600, 700))
        self.BlockswebEngineView.setUrl(QUrl(u"about:blank"))
        self.tabWidget.addTab(self.BlockS, "")
        self.Shems = QWidget()
        self.Shems.setObjectName(u"Shems")
        self.SchemewebEngineView = QWebEngineView(self.Shems)
        self.SchemewebEngineView.setObjectName(u"SchemewebEngineView")
        self.SchemewebEngineView.setEnabled(True)
        self.SchemewebEngineView.setGeometry(QRect(0, 0, 1600, 700))
        self.SchemewebEngineView.setUrl(QUrl(u"about:blank"))
        self.tabWidget.addTab(self.Shems, "")
        self.Debug = QToolButton(self.centralwidget)
        self.Debug.setObjectName(u"Debug")
        self.Debug.setGeometry(QRect(1500, 0, 100, 50))
        self.Drive = QToolButton(self.centralwidget)
        self.Drive.setObjectName(u"Drive")
        self.Drive.setGeometry(QRect(1400, 0, 68, 24))
        ADRudion.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ADRudion)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1600, 22))
        ADRudion.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ADRudion)
        self.statusbar.setObjectName(u"statusbar")
        ADRudion.setStatusBar(self.statusbar)

        self.retranslateUi(ADRudion)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ADRudion)
    # setupUi

    def retranslateUi(self, ADRudion):
        ADRudion.setWindowTitle(QCoreApplication.translate("ADRudion", u"ADRudion", None))
        self.File.setText(QCoreApplication.translate("ADRudion", u"\u0424\u0430\u0439\u043b", None))
        self.Settings.setText(QCoreApplication.translate("ADRudion", u"\u041d\u0430\u0441\u0442\u0440\u0439\u043a\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BlockS), QCoreApplication.translate("ADRudion", u"Blocks", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Shems), QCoreApplication.translate("ADRudion", u"Scheme", None))
        self.Debug.setText(QCoreApplication.translate("ADRudion", u"\u0414\u0435\u0431\u0430\u0433", None))
        self.Drive.setText(QCoreApplication.translate("ADRudion", u"\u041f\u0440\u043e\u0448\u0438\u0442\u044c", None))
    # retranslateUi

