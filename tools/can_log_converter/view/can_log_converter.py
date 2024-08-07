# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'can_log_converter.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QListView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"../../Nodejs/can-bus.io-electron/can-bus.io/resources/img/favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.action_load = QAction(MainWindow)
        self.action_load.setObjectName(u"action_load")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_ad = QAction(MainWindow)
        self.action_ad.setObjectName(u"action_ad")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.rbtn_asc = QRadioButton(self.centralwidget)
        self.rbtn_asc.setObjectName(u"rbtn_asc")
        self.rbtn_asc.setGeometry(QRect(300, 20, 50, 22))
        self.rbtn_blf = QRadioButton(self.centralwidget)
        self.rbtn_blf.setObjectName(u"rbtn_blf")
        self.rbtn_blf.setGeometry(QRect(360, 20, 50, 22))
        self.rbtn_csv = QRadioButton(self.centralwidget)
        self.rbtn_csv.setObjectName(u"rbtn_csv")
        self.rbtn_csv.setGeometry(QRect(420, 20, 50, 22))
        self.rbtn_db = QRadioButton(self.centralwidget)
        self.rbtn_db.setObjectName(u"rbtn_db")
        self.rbtn_db.setGeometry(QRect(480, 20, 50, 22))
        self.rbtn_log = QRadioButton(self.centralwidget)
        self.rbtn_log.setObjectName(u"rbtn_log")
        self.rbtn_log.setGeometry(QRect(540, 20, 50, 22))
        self.rbtn_mf4 = QRadioButton(self.centralwidget)
        self.rbtn_mf4.setObjectName(u"rbtn_mf4")
        self.rbtn_mf4.setGeometry(QRect(600, 20, 50, 22))
        self.rbtn_trc = QRadioButton(self.centralwidget)
        self.rbtn_trc.setObjectName(u"rbtn_trc")
        self.rbtn_trc.setGeometry(QRect(660, 20, 50, 22))
        self.pbtn_convert = QPushButton(self.centralwidget)
        self.pbtn_convert.setObjectName(u"pbtn_convert")
        self.pbtn_convert.setGeometry(QRect(710, 15, 88, 32))
        self.outputDir = QLineEdit(self.centralwidget)
        self.outputDir.setObjectName(u"outputDir")
        self.outputDir.setGeometry(QRect(10, 15, 210, 32))
        self.pbtn_setTargetDir = QPushButton(self.centralwidget)
        self.pbtn_setTargetDir.setObjectName(u"pbtn_setTargetDir")
        self.pbtn_setTargetDir.setGeometry(QRect(225, 15, 60, 32))
        self.inputFilesList = QListView(self.centralwidget)
        self.inputFilesList.setObjectName(u"inputFilesList")
        self.inputFilesList.setGeometry(QRect(10, 60, 780, 450))
        self.pbtn_loadInputFiles = QPushButton(self.centralwidget)
        self.pbtn_loadInputFiles.setObjectName(u"pbtn_loadInputFiles")
        self.pbtn_loadInputFiles.setGeometry(QRect(340, 512, 120, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 32))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_load)
        self.menu_file.addAction(self.action_exit)
        self.menu_help.addAction(self.action_ad)
        self.menu_help.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CAN Log Converter", None))
        self.action_load.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.action_ad.setText(QCoreApplication.translate("MainWindow", u"CAN-BUS.IO", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.rbtn_asc.setText(QCoreApplication.translate("MainWindow", u".asc", None))
        self.rbtn_blf.setText(QCoreApplication.translate("MainWindow", u".blf", None))
        self.rbtn_csv.setText(QCoreApplication.translate("MainWindow", u".csv", None))
        self.rbtn_db.setText(QCoreApplication.translate("MainWindow", u".db", None))
        self.rbtn_log.setText(QCoreApplication.translate("MainWindow", u".log", None))
        self.rbtn_mf4.setText(QCoreApplication.translate("MainWindow", u".mf4", None))
        self.rbtn_trc.setText(QCoreApplication.translate("MainWindow", u".trc", None))
        self.pbtn_convert.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.pbtn_setTargetDir.setText(QCoreApplication.translate("MainWindow", u"OutPut", None))
        self.pbtn_loadInputFiles.setText(QCoreApplication.translate("MainWindow", u"Load Input Files", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

