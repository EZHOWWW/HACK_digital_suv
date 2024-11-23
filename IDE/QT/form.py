# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowform.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class IDR_mainwindow_ui(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        self.action_Create = QAction(mainWindow)
        self.action_Create.setObjectName(u"action_Create")
        self.action_Open = QAction(mainWindow)
        self.action_Open.setObjectName(u"action_Open")
        self.action_Save = QAction(mainWindow)
        self.action_Save.setObjectName(u"action_Save")
        self.action_SaveAs = QAction(mainWindow)
        self.action_SaveAs.setObjectName(u"action_SaveAs")
        self.action = QAction(mainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(mainWindow)
        self.action_2.setObjectName(u"action_2")
        self.bloklyWebWidget = QWidget(mainWindow)
        self.bloklyWebWidget.setObjectName(u"bloklyWebWidget")
        mainWindow.setCentralWidget(self.bloklyWebWidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Settings = QMenu(self.menubar)
        self.menu_Settings.setObjectName(u"menu_Settings")
        self.menu_Controller = QMenu(self.menubar)
        self.menu_Controller.setObjectName(u"menu_Controller")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Settings.menuAction())
        self.menubar.addAction(self.menu_Controller.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menu_File.addAction(self.action_Create)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_SaveAs)
        self.menu_Controller.addAction(self.action)
        self.menu.addAction(self.action_2)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"IDR Rudion Visual IDE", None))
        self.action_Create.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439", None))
        self.action_Open.setText(QCoreApplication.translate("mainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.action_Save.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043e\u0445\u0440\u0432\u043d\u0438\u0442\u044c", None))
        self.action_SaveAs.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
        self.action.setText(QCoreApplication.translate("mainWindow", u"\u041f\u0440\u043e\u0448\u0438\u0442\u044c", None))
        self.action_2.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043f\u0440\u043e\u0441\u0438\u0442\u044c \u0443 \u0418\u0418", None))
        self.menu_File.setTitle(QCoreApplication.translate("mainWindow", u"\u0424\u0430\u0438\u043b", None))
        self.menu_Settings.setTitle(QCoreApplication.translate("mainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.menu_Controller.setTitle(QCoreApplication.translate("mainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u043b\u0435\u0440", None))
        self.menu.setTitle(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

