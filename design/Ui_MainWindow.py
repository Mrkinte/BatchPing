# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 700)
        icon = QIcon()
        icon.addFile(u":/icons/favicon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleWidget = QWidget(self.centralwidget)
        self.titleWidget.setObjectName(u"titleWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.titleWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.titleWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.backBtn = QPushButton(self.widget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setMinimumSize(QSize(36, 36))
        self.backBtn.setMaximumSize(QSize(36, 36))
        self.backBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"	border-radius: 5px 5px 5px 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 0, 0, 0.1);\n"
"	border-radius: 5px 5px 5px 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 0.3);\n"
"	border-radius: 5px 5px 5px 5px;\n"
"    border: none;\n"
"}")
        self.backBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.backBtn)

        self.horizontalSpacer_4 = QSpacerItem(246, 45, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_2.addWidget(self.widget)

        self.titleLabel = QLabel(self.titleWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(200, 48))
        self.titleLabel.setMaximumSize(QSize(200, 48))
        font = QFont()
        font.setPointSize(13)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.titleLabel)

        self.widget_2 = QWidget(self.titleWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(246, 45, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.settingsBtn = QPushButton(self.widget_2)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(36, 36))
        self.settingsBtn.setMaximumSize(QSize(36, 36))
        self.settingsBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"	border-radius: 5px 5px 5px 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 0, 0, 0.1);\n"
"	border-radius: 5px 5px 5px 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 0.3);\n"
"	border-radius: 5px 5px 5px 5px;\n"
"    border: none;\n"
"}")
        self.settingsBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.settingsBtn)

        self.exportBtn = QPushButton(self.widget_2)
        self.exportBtn.setObjectName(u"exportBtn")
        self.exportBtn.setMinimumSize(QSize(36, 36))
        self.exportBtn.setMaximumSize(QSize(36, 36))
        self.exportBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"	border-radius: 5px 5px 5px 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 0, 0, 0.1);\n"
"	border-radius: 5px 5px 5px 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 0.3);\n"
"	border-radius: 5px 5px 5px 5px;\n"
"    border: none;\n"
"}")
        self.exportBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.exportBtn)


        self.horizontalLayout_2.addWidget(self.widget_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addWidget(self.titleWidget)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6279\u91cfPING", None))
        self.backBtn.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"\u6279 \u91cf PING \u6d4b \u8bd5", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText("")
#if QT_CONFIG(tooltip)
        self.exportBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5bfc\u51fa\uff08.xlsx\uff09", None))
#endif // QT_CONFIG(tooltip)
        self.exportBtn.setText("")
#if QT_CONFIG(whatsthis)
        self.stackedWidget.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
    # retranslateUi

