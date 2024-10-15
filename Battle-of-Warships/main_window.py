# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QWidget)
import atlas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1263, 820)
        MainWindow.setStyleSheet(u"background-color: #252525;\n"
"color: #fff;\n"
"font: 16pt url(:/newPrefix/Src/fonts/Montserrat.ttf);\n"
"text-align: center;")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_5.setCheckable(False)
        self.action_5.setChecked(False)
        self.action_5.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName(u"action_8")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.event = QSlider(self.centralwidget)
        self.event.setObjectName(u"event")
        self.event.setGeometry(QRect(360, 730, 321, 41))
        self.event.setStyleSheet(u"QSlider {\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    background: #ccc;\n"
"    height: 6px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #333333;\n"
"    border: 1px solid #555555;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #555555;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #444;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #dddddd;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.event.setOrientation(Qt.Orientation.Horizontal)
        self.speed_inp = QSpinBox(self.centralwidget)
        self.speed_inp.setObjectName(u"speed_inp")
        self.speed_inp.setGeometry(QRect(700, 670, 111, 41))
        self.event_inp = QSpinBox(self.centralwidget)
        self.event_inp.setObjectName(u"event_inp")
        self.event_inp.setGeometry(QRect(700, 730, 111, 41))
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(20, 730, 161, 41))
        self.start.setStyleSheet(u"QPushButton {\n"
"        background-color: #252525;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #333333;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #444444;\n"
"        padding-top: 2px;\n"
"    }")
        self.continue_2 = QPushButton(self.centralwidget)
        self.continue_2.setObjectName(u"continue_2")
        self.continue_2.setGeometry(QRect(20, 670, 161, 41))
        self.continue_2.setStyleSheet(u"QPushButton {\n"
"        background-color: #252525;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #333333;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #444444;\n"
"        padding-top: 2px;\n"
"    }")
        self.accuracy = QCheckBox(self.centralwidget)
        self.accuracy.setObjectName(u"accuracy")
        self.accuracy.setGeometry(QRect(1030, 670, 211, 41))
        self.accuracy.setStyleSheet(u"QCheckBox {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color: #252525;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 3px;\n"
"    border: 2px solid #555555;\n"
"    background-color: #333333;\n"
"	margin: 0px 9px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    border: 2px solid #777777;\n"
"    background-color: #555555;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #fff;\n"
"    border: 2px solid #ccc;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background-color: #ddd;\n"
"    border: 2px solid #aaa;\n"
"}\n"
"\n"
"")
        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(1030, 730, 211, 41))
        self.exit.setStyleSheet(u"QPushButton {\n"
"        background-color: #252525;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #333333;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #444444;\n"
"        padding-top: 2px;\n"
"    }")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 670, 91, 41))
        self.label.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"color: #252525;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 730, 91, 41))
        self.label_2.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"color: #252525;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(870, 670, 41, 41))
        self.label_3.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"color: #252525;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(870, 730, 31, 41))
        self.label_4.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"color: #252525;")
        self.bg = QLabel(self.centralwidget)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(0, -60, 1271, 841))
        self.bg.setAutoFillBackground(False)
        self.bg.setStyleSheet(u"")
        self.bg.setPixmap(QPixmap(u":/newPrefix/images/background.png"))
        self.bg.setScaledContents(True)
        self.settings_bg = QLabel(self.centralwidget)
        self.settings_bg.setObjectName(u"settings_bg")
        self.settings_bg.setGeometry(QRect(-40, 650, 1321, 241))
        self.settings_bg.setStyleSheet(u"background-color: rgba(255,255,255,0.5);")
        self.team_indicator = QLabel(self.centralwidget)
        self.team_indicator.setObjectName(u"team_indicator")
        self.team_indicator.setGeometry(QRect(920, 670, 41, 41))
        self.team_indicator.setStyleSheet(u"\n"
"border: 2px solid #ccc;\n"
"border-radius: 10px;")
        self.event_indicator = QLabel(self.centralwidget)
        self.event_indicator.setObjectName(u"event_indicator")
        self.event_indicator.setGeometry(QRect(920, 730, 41, 41))
        self.event_indicator.setStyleSheet(u"background-color: #f1d769;\n"
"border: 2px solid #ccc;\n"
"border-radius: 10px;")
        self.ship_1 = QLabel(self.centralwidget)
        self.ship_1.setObjectName(u"ship_1")
        self.ship_1.setGeometry(QRect(140, 110, 191, 81))
        self.ship_1.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.ship_1.setPixmap(QPixmap(u":/newPrefix/images/l-0-5.png"))
        self.ship_1.setScaledContents(True)
        self.mesh_1 = QLabel(self.centralwidget)
        self.mesh_1.setObjectName(u"mesh_1")
        self.mesh_1.setGeometry(QRect(50, 50, 551, 551))
        self.mesh_1.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.mesh_1.setPixmap(QPixmap(u":/newPrefix/images/mesh.png"))
        self.mesh_2 = QLabel(self.centralwidget)
        self.mesh_2.setObjectName(u"mesh_2")
        self.mesh_2.setGeometry(QRect(660, 50, 551, 551))
        self.mesh_2.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.mesh_2.setPixmap(QPixmap(u":/newPrefix/images/mesh.png"))
        self.hp_1 = QLabel(self.centralwidget)
        self.hp_1.setObjectName(u"hp_1")
        self.hp_1.setGeometry(QRect(140, 200, 191, 31))
        self.hp_1.setStyleSheet(u"background-color: rgba(255, 0,0,1);\n"
"border: 2px solid #fff;\n"
"border-radius: 5px;\n"
"font: 14pt url(:/newPrefix/Src/fonts/Montserrat.ttf);")
        self.hp_2 = QLabel(self.centralwidget)
        self.hp_2.setObjectName(u"hp_2")
        self.hp_2.setGeometry(QRect(390, 230, 191, 31))
        self.hp_2.setStyleSheet(u"background-color: rgba(255, 0,0,1);\n"
"border: 2px solid #fff;\n"
"border-radius: 5px;\n"
"font: 14pt url(:/newPrefix/Src/fonts/Montserrat.ttf);")
        self.hp_3 = QLabel(self.centralwidget)
        self.hp_3.setObjectName(u"hp_3")
        self.hp_3.setGeometry(QRect(390, 390, 191, 31))
        self.hp_3.setStyleSheet(u"background-color: rgba(255, 0,0,1);\n"
"border: 2px solid #fff;\n"
"border-radius: 5px;\n"
"font: 14pt url(:/newPrefix/Src/fonts/Montserrat.ttf);")
        self.hp_4 = QLabel(self.centralwidget)
        self.hp_4.setObjectName(u"hp_4")
        self.hp_4.setGeometry(QRect(180, 510, 191, 31))
        self.hp_4.setStyleSheet(u"background-color: rgba(255, 0,0,1);\n"
"border: 2px solid #fff;\n"
"border-radius: 5px;\n"
"font: 14pt url(:/newPrefix/Src/fonts/Montserrat.ttf);")
        self.hp_5 = QLabel(self.centralwidget)
        self.hp_5.setObjectName(u"hp_5")
        self.hp_5.setGeometry(QRect(100, 370, 191, 31))
        self.hp_5.setStyleSheet(u"background-color: rgba(255, 0,0,1);\n"
"border: 2px solid #fff;\n"
"border-radius: 5px;\n"
"font: 14pt url(:/newPrefix/Src/fonts/Montserrat.ttf);")
        self.hp_6 = QLabel(self.centralwidget)
        self.hp_6.setObjectName(u"hp_6")
        self.hp_6.setGeometry(QRect(740, 220, 191, 31))
        self.hp_6.setStyleSheet(u"background-color: rgba(255, 0,0,1);\n"
"border: 2px solid #fff;\n"
"border-radius: 5px;\n"
"font: 14pt url(:/newPrefix/Src/fonts/Montserrat.ttf);")
        self.hp_7 = QLabel(self.centralwidget)
        self.hp_7.setObjectName(u"hp_7")
        self.hp_7.setGeometry(QRect(1010, 250, 191, 31))
        self.hp_7.setStyleSheet(u"background-color: rgba(255, 0,0,1);\n"
"border: 2px solid #fff;\n"
"border-radius: 5px;\n"
"font: 14pt url(:/newPrefix/Src/fonts/Montserrat.ttf);")
        self.hp_8 = QLabel(self.centralwidget)
        self.hp_8.setObjectName(u"hp_8")
        self.hp_8.setGeometry(QRect(1000, 410, 191, 31))
        self.hp_8.setStyleSheet(u"background-color: rgba(255, 0,0,1);\n"
"border: 2px solid #fff;\n"
"border-radius: 5px;\n"
"font: 14pt url(:/newPrefix/Src/fonts/Montserrat.ttf);")
        self.hp_9 = QLabel(self.centralwidget)
        self.hp_9.setObjectName(u"hp_9")
        self.hp_9.setGeometry(QRect(850, 540, 191, 31))
        self.hp_9.setStyleSheet(u"background-color: rgba(255, 0,0,1);\n"
"border: 2px solid #fff;\n"
"border-radius: 5px;\n"
"font: 14pt url(:/newPrefix/Src/fonts/Montserrat.ttf);")
        self.hp_10 = QLabel(self.centralwidget)
        self.hp_10.setObjectName(u"hp_10")
        self.hp_10.setGeometry(QRect(700, 400, 191, 31))
        self.hp_10.setStyleSheet(u"background-color: rgba(255, 0,0,1);\n"
"border: 2px solid #fff;\n"
"border-radius: 5px;\n"
"font: 14pt url(:/newPrefix/Src/fonts/Montserrat.ttf);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 100, 31, 31))
        self.label_5.setStyleSheet(u"background-color: rgba(255, 0,0,0);\n"
"color: #f00;\n"
"font: 14pt url(:/newPrefix/Src/fonts/Montserrat.ttf);")
        self.speed = QSlider(self.centralwidget)
        self.speed.setObjectName(u"speed")
        self.speed.setGeometry(QRect(360, 670, 321, 41))
        self.speed.setStyleSheet(u"QSlider {\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    background: #ccc;\n"
"    height: 6px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #333333;\n"
"    border: 1px solid #555555;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #555555;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #444;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #dddddd;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.speed.setOrientation(Qt.Orientation.Horizontal)
        self.ship_2 = QLabel(self.centralwidget)
        self.ship_2.setObjectName(u"ship_2")
        self.ship_2.setGeometry(QRect(390, 140, 191, 81))
        self.ship_2.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.ship_2.setPixmap(QPixmap(u":/newPrefix/images/l-0-5.png"))
        self.ship_2.setScaledContents(True)
        self.ship_3 = QLabel(self.centralwidget)
        self.ship_3.setObjectName(u"ship_3")
        self.ship_3.setGeometry(QRect(390, 300, 191, 81))
        self.ship_3.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.ship_3.setPixmap(QPixmap(u":/newPrefix/images/l-0-5.png"))
        self.ship_3.setScaledContents(True)
        self.ship_4 = QLabel(self.centralwidget)
        self.ship_4.setObjectName(u"ship_4")
        self.ship_4.setGeometry(QRect(180, 420, 191, 81))
        self.ship_4.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.ship_4.setPixmap(QPixmap(u":/newPrefix/images/l-0-5.png"))
        self.ship_4.setScaledContents(True)
        self.ship_5 = QLabel(self.centralwidget)
        self.ship_5.setObjectName(u"ship_5")
        self.ship_5.setGeometry(QRect(100, 280, 191, 81))
        self.ship_5.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.ship_5.setPixmap(QPixmap(u":/newPrefix/images/l-0-5.png"))
        self.ship_5.setScaledContents(True)
        self.ship_6 = QLabel(self.centralwidget)
        self.ship_6.setObjectName(u"ship_6")
        self.ship_6.setGeometry(QRect(730, 130, 191, 81))
        self.ship_6.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.ship_6.setPixmap(QPixmap(u":/newPrefix/images/l-0-5.png"))
        self.ship_6.setScaledContents(True)
        self.ship_7 = QLabel(self.centralwidget)
        self.ship_7.setObjectName(u"ship_7")
        self.ship_7.setGeometry(QRect(1010, 160, 191, 81))
        self.ship_7.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.ship_7.setPixmap(QPixmap(u":/newPrefix/images/l-0-5.png"))
        self.ship_7.setScaledContents(True)
        self.ship_8 = QLabel(self.centralwidget)
        self.ship_8.setObjectName(u"ship_8")
        self.ship_8.setGeometry(QRect(1000, 320, 191, 81))
        self.ship_8.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.ship_8.setPixmap(QPixmap(u":/newPrefix/images/l-0-5.png"))
        self.ship_8.setScaledContents(True)
        self.ship_9 = QLabel(self.centralwidget)
        self.ship_9.setObjectName(u"ship_9")
        self.ship_9.setGeometry(QRect(850, 450, 191, 81))
        self.ship_9.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.ship_9.setPixmap(QPixmap(u":/newPrefix/images/l-0-5.png"))
        self.ship_9.setScaledContents(True)
        self.ship_10 = QLabel(self.centralwidget)
        self.ship_10.setObjectName(u"ship_10")
        self.ship_10.setGeometry(QRect(700, 310, 191, 81))
        self.ship_10.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.ship_10.setPixmap(QPixmap(u":/newPrefix/images/l-0-5.png"))
        self.ship_10.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.bg.raise_()
        self.mesh_1.raise_()
        self.mesh_2.raise_()
        self.settings_bg.raise_()
        self.event.raise_()
        self.speed_inp.raise_()
        self.event_inp.raise_()
        self.start.raise_()
        self.continue_2.raise_()
        self.accuracy.raise_()
        self.exit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.team_indicator.raise_()
        self.event_indicator.raise_()
        self.speed.raise_()
        self.ship_1.raise_()
        self.hp_1.raise_()
        self.hp_2.raise_()
        self.hp_3.raise_()
        self.hp_4.raise_()
        self.hp_5.raise_()
        self.hp_6.raise_()
        self.hp_7.raise_()
        self.hp_8.raise_()
        self.hp_9.raise_()
        self.hp_10.raise_()
        self.label_5.raise_()
        self.ship_2.raise_()
        self.ship_3.raise_()
        self.ship_4.raise_()
        self.ship_5.raise_()
        self.ship_6.raise_()
        self.ship_7.raise_()
        self.ship_8.raise_()
        self.ship_9.raise_()
        self.ship_10.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1263, 33))
        font = QFont()
        font.setFamilies([u":/newPrefix/Src/fonts/Montserrat.ttf"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet(u"selection-background-color: rgba(255,255,255,0.1);\n"
"font: 9pt url(:/newPrefix/Src/fonts/Montserrat.ttf);")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.action_5)
        self.menu.addAction(self.action_6)
        self.menu.addSeparator()
        self.menu.addAction(self.action_8)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)
        self.menu_3.addAction(self.action)
        self.menu_3.addAction(self.action_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u0440\u0430\u0431\u043b\u0438\u043a\u0438", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0430\u0432\u0442\u043e\u0440", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u043d\u0433 \u043a\u043e\u0440\u0430\u0431\u043b\u0435\u0439", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u0446\u0432\u0435\u0442\u0430 \u043a\u043e\u043c\u0430\u043d\u0434", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c ", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u0445\u043e\u0434", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0442\u0430\u0440\u0442", None))
        self.continue_2.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.accuracy.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0435\u0436\u0438\u043c \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u0438", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u0445\u043e\u0434", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0448\u0430\u043d\u0441 \u0410\u041b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0445\u043e\u0434", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0410\u041b", None))
        self.bg.setText("")
        self.settings_bg.setText("")
        self.team_indicator.setText("")
        self.event_indicator.setText("")
        self.ship_1.setText("")
        self.mesh_1.setText("")
        self.mesh_2.setText("")
        self.hp_1.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.hp_2.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.hp_3.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.hp_4.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.hp_5.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.hp_6.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.hp_7.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.hp_8.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.hp_9.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.hp_10.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"322", None))
        self.ship_2.setText("")
        self.ship_3.setText("")
        self.ship_4.setText("")
        self.ship_5.setText("")
        self.ship_6.setText("")
        self.ship_7.setText("")
        self.ship_8.setText("")
        self.ship_9.setText("")
        self.ship_10.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0444\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

