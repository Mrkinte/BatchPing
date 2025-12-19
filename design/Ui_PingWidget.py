# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PingWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (LineEdit, PrimaryPushButton)

class Ui_PingWidget(object):
    def setupUi(self, PingWidget):
        if not PingWidget.objectName():
            PingWidget.setObjectName(u"PingWidget")
        PingWidget.resize(675, 517)
        self.baseLayout = QVBoxLayout(PingWidget)
        self.baseLayout.setSpacing(6)
        self.baseLayout.setObjectName(u"baseLayout")
        self.baseLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(PingWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 40))
        self.widget_2.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.widget_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(200, 24))
        self.progressBar.setMaximumSize(QSize(200, 24))
        self.progressBar.setStyleSheet(u"/* \u8fdb\u5ea6\u6761\u6574\u4f53\u6837\u5f0f */\n"
"QProgressBar {\n"
"    border: 1px solid #ffffff;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"/* \u8fdb\u5ea6\u6761\u524d\u666f\u6837\u5f0f */\n"
"QProgressBar::chunk {\n"
"    /* \u6a2a\u5411\u6e10\u53d8\u80cc\u666f */\n"
"    background:#009FAA;\n"
"    border-radius: 4px;\n"
"    /* \u5185\u9634\u5f71\u6548\u679c */\n"
"    border: 1px solid rgba(255, 255, 255, 30%);\n"
"    box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);\n"
"}")
        self.progressBar.setValue(0)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.ipEdit_1 = LineEdit(self.widget_2)
        self.ipEdit_1.setObjectName(u"ipEdit_1")
        self.ipEdit_1.setMinimumSize(QSize(56, 36))
        self.ipEdit_1.setMaximumSize(QSize(56, 36))
        self.ipEdit_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.ipEdit_1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.ipEdit_2 = LineEdit(self.widget_2)
        self.ipEdit_2.setObjectName(u"ipEdit_2")
        self.ipEdit_2.setMinimumSize(QSize(56, 36))
        self.ipEdit_2.setMaximumSize(QSize(56, 36))
        self.ipEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.ipEdit_2)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.ipEdit_3 = LineEdit(self.widget_2)
        self.ipEdit_3.setObjectName(u"ipEdit_3")
        self.ipEdit_3.setMinimumSize(QSize(56, 36))
        self.ipEdit_3.setMaximumSize(QSize(56, 36))
        self.ipEdit_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.ipEdit_3)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_5.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.startPingBtn = PrimaryPushButton(self.widget_2)
        self.startPingBtn.setObjectName(u"startPingBtn")
        self.startPingBtn.setMinimumSize(QSize(72, 36))
        self.startPingBtn.setMaximumSize(QSize(72, 36))

        self.horizontalLayout_2.addWidget(self.startPingBtn)

        self.stopPingBtn = PrimaryPushButton(self.widget_2)
        self.stopPingBtn.setObjectName(u"stopPingBtn")
        self.stopPingBtn.setEnabled(False)
        self.stopPingBtn.setMinimumSize(QSize(72, 36))
        self.stopPingBtn.setMaximumSize(QSize(72, 36))

        self.horizontalLayout_2.addWidget(self.stopPingBtn)


        self.baseLayout.addWidget(self.widget_2)

        self.tableWidget = QWidget(PingWidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: #ff0000;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")

        self.baseLayout.addWidget(self.tableWidget)

        self.widget_4 = QWidget(PingWidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 40))
        self.widget_4.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(20, 20))
        self.label_12.setMaximumSize(QSize(20, 20))
        self.label_12.setStyleSheet(u"QLabel {\n"
"	border-radius: 5px;\n"
"	background-color: #c0c0c0;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_12)

        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(20, 20))
        self.label_2.setMaximumSize(QSize(20, 20))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	border-radius: 5px;\n"
"	background-color: #50d050;\n"
"}")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(20, 20))
        self.label_7.setMaximumSize(QSize(20, 20))
        self.label_7.setStyleSheet(u"QLabel {\n"
"	border-radius: 5px;\n"
"	background-color: #70c8ff;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(20, 20))
        self.label_10.setMaximumSize(QSize(20, 20))
        self.label_10.setStyleSheet(u"QLabel {\n"
"	border-radius: 5px;\n"
"	background-color: #ffff70;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.label_16 = QLabel(self.widget_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(20, 20))
        self.label_16.setMaximumSize(QSize(20, 20))
        self.label_16.setStyleSheet(u"QLabel {\n"
"	border-radius: 5px;\n"
"	background-color: #ff8080;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_16)

        self.label_15 = QLabel(self.widget_4)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_3.addWidget(self.label_15)

        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(20, 20))
        self.label_14.setMaximumSize(QSize(20, 20))
        self.label_14.setStyleSheet(u"QLabel {\n"
"	border-radius: 5px;\n"
"	background-color: #ff5050;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_14)

        self.label_13 = QLabel(self.widget_4)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)


        self.baseLayout.addWidget(self.widget_4)


        self.retranslateUi(PingWidget)

        QMetaObject.connectSlotsByName(PingWidget)
    # setupUi

    def retranslateUi(self, PingWidget):
        self.progressBar.setFormat(QCoreApplication.translate("PingWidget", u"\u7b49\u5f85\u6d4b\u8bd5\u5f00\u59cb", None))
        self.ipEdit_1.setText(QCoreApplication.translate("PingWidget", u"192", None))
        self.ipEdit_1.setPlaceholderText(QCoreApplication.translate("PingWidget", u"192", None))
        self.label.setText(QCoreApplication.translate("PingWidget", u".", None))
        self.ipEdit_2.setText(QCoreApplication.translate("PingWidget", u"168", None))
        self.ipEdit_2.setPlaceholderText(QCoreApplication.translate("PingWidget", u"168", None))
        self.label_3.setText(QCoreApplication.translate("PingWidget", u".", None))
        self.ipEdit_3.setPlaceholderText(QCoreApplication.translate("PingWidget", u"0", None))
        self.label_4.setText(QCoreApplication.translate("PingWidget", u".", None))
        self.label_5.setText(QCoreApplication.translate("PingWidget", u"xxx", None))
        self.startPingBtn.setText(QCoreApplication.translate("PingWidget", u"\u5f00\u59cb", None))
        self.stopPingBtn.setText(QCoreApplication.translate("PingWidget", u"\u505c\u6b62", None))
        self.label_12.setText("")
        self.label_11.setText(QCoreApplication.translate("PingWidget", u"\u672a\u6d4b\u8bd5", None))
        self.label_2.setText("")
        self.label_6.setText(QCoreApplication.translate("PingWidget", u"<50ms", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("PingWidget", u"<100ms", None))
        self.label_10.setText("")
        self.label_9.setText(QCoreApplication.translate("PingWidget", u"<200ms", None))
        self.label_16.setText("")
        self.label_15.setText(QCoreApplication.translate("PingWidget", u">=200ms \u6216 \u5b58\u5728\u4e22\u5305", None))
        self.label_14.setText("")
        self.label_13.setText(QCoreApplication.translate("PingWidget", u"\u6d4b\u8bd5\u8d85\u65f6", None))
        pass
    # retranslateUi

