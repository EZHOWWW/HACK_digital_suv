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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 450)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.File = QToolButton(self.centralwidget)
        self.File.setObjectName(u"File")
        self.File.setGeometry(QRect(0, 0, 100, 50))
        self.Settings = QToolButton(self.centralwidget)
        self.Settings.setObjectName(u"Settings")
        self.Settings.setGeometry(QRect(100, 0, 100, 50))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 50, 800, 380))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.BlockS = QWidget()
        self.BlockS.setObjectName(u"BlockS")
        self.BlockswebEngineView = QWebEngineView(self.BlockS)
        self.BlockswebEngineView.setObjectName(u"BlockswebEngineView")
        self.BlockswebEngineView.setEnabled(True)
        self.BlockswebEngineView.setGeometry(QRect(0, 0, 800, 350))
        self.BlockswebEngineView.setUrl(QUrl(u"about:blank"))
        self.tabWidget.addTab(self.BlockS, "")
        self.Shems = QWidget()
        self.Shems.setObjectName(u"Shems")
        self.SchemewebEngineView = QWebEngineView(self.Shems)
        self.SchemewebEngineView.setObjectName(u"SchemewebEngineView")
        self.SchemewebEngineView.setEnabled(True)
        self.SchemewebEngineView.setGeometry(QRect(0, 0, 800, 350))
        self.SchemewebEngineView.setUrl(QUrl(u"about:blank"))
        self.tabWidget.addTab(self.Shems, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.File.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.Settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u0439\u043a\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BlockS), QCoreApplication.translate("MainWindow", u"Blocks", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Shems), QCoreApplication.translate("MainWindow", u"Scheme", None))
    # retranslateUi

