# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)
import assets_rc

class Ui_AboutWidget(object):
    def setupUi(self, AboutWidget):
        if not AboutWidget.objectName():
            AboutWidget.setObjectName(u"AboutWidget")
        AboutWidget.resize(400, 300)
        AboutWidget.setMinimumSize(QSize(400, 300))
        AboutWidget.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u":/icons/favicon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        AboutWidget.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(AboutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(AboutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(48, 48))
        self.pushButton.setMaximumSize(QSize(48, 48))
        self.pushButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: None;\n"
"")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(48, 48))

        self.horizontalLayout.addWidget(self.pushButton)

        self.textBrowser = QTextBrowser(AboutWidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)


        self.retranslateUi(AboutWidget)

        QMetaObject.connectSlotsByName(AboutWidget)
    # setupUi

    def retranslateUi(self, AboutWidget):
        AboutWidget.setWindowTitle(QCoreApplication.translate("AboutWidget", u"\u8f6f\u4ef6\u4fe1\u606f", None))
    # retranslateUi

