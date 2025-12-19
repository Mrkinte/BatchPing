from PySide6.QtCore import Qt, QSize, QFile, QIODevice, QXmlStreamReader
from PySide6.QtGui import QPixmap, QPainter, QIcon
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QMainWindow, QFileDialog
from qfluentwidgets import InfoBar, InfoBarIcon, InfoBarPosition, ToolTipFilter, ToolTipPosition
from qframelesswindow.utils import getSystemAccentColor

from design.Ui_MainWindow import Ui_MainWindow
from widgets.ping_widget import PingWidget
from widgets.settings_widget import SettingsWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pingWidget = PingWidget(self)
        self.settingsWidget = SettingsWidget()
        self.ui.stackedWidget.addWidget(self.pingWidget)
        self.ui.stackedWidget.addWidget(self.settingsWidget)
        self.ui.backBtn.setHidden(True)
        self.ui.settingsBtn.installEventFilter(
            ToolTipFilter(self.ui.settingsBtn, showDelay=300, position=ToolTipPosition.BOTTOM))
        self.ui.exportBtn.installEventFilter(
            ToolTipFilter(self.ui.exportBtn, showDelay=300, position=ToolTipPosition.BOTTOM))

        self.ui.backBtn.clicked.connect(self.loadPingWidget)
        self.ui.settingsBtn.clicked.connect(self.loadSettingsWidget)
        self.ui.exportBtn.clicked.connect(self.exportBtnEventHandler)

        self.ui.backBtn.setIcon(self.createSvgIcon(":icons/back_icon.svg", width=32, height=32))
        self.ui.settingsBtn.setIcon(self.createSvgIcon(":icons/settings_icon.svg"))
        self.ui.exportBtn.setIcon(self.createSvgIcon(":icons/export_icon.svg"))

    def loadSettingsWidget(self):
        self.ui.titleLabel.setText("设 置")
        self.ui.stackedWidget.setCurrentWidget(self.settingsWidget)
        self.ui.backBtn.setHidden(False)
        self.ui.settingsBtn.setHidden(True)
        self.ui.exportBtn.setHidden(True)

    def loadPingWidget(self):
        self.ui.titleLabel.setText("批 量 PING")
        self.ui.stackedWidget.setCurrentWidget(self.pingWidget)
        self.ui.backBtn.setHidden(True)
        self.ui.settingsBtn.setHidden(False)
        self.ui.exportBtn.setHidden(False)

    def exportBtnEventHandler(self):
        if self.pingWidget.ping_finished:
            file_path, selected_filter = QFileDialog.getSaveFileName(
                self,
                "保存测试数据",
                "测试数据.xlsx",
                "Excel 工作簿(*.xlsx)"
            )
            if file_path:
                try:
                    self.pingWidget.wb.save(file_path)
                except IOError as e:
                    w = InfoBar(
                        icon=InfoBarIcon.ERROR,
                        title="错误",
                        content="文件被占用，无法导出，请关闭已打开的Excel表格或者重命名！",
                        orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.TOP,
                        duration=5000,
                        parent=self
                    )
                    w.show()
        else:
            w = InfoBar(
                icon=InfoBarIcon.INFORMATION,
                title="提示",
                content="无完整测试结果，无法导出！",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=3000,
                parent=self
            )
            w.show()

    @staticmethod
    def createSvgIcon(svg_path, width=24, height=24):
        file = QFile(svg_path)
        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            return QIcon()
        svg_data = str(file.readAll(), 'utf-8')
        file.close()

        svg_recolor = svg_data.replace('fill="#000000"', f'fill="{ getSystemAccentColor().name() }"')
        renderer = QSvgRenderer(QXmlStreamReader(svg_recolor))
        pixmap = QPixmap(width, height)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        return QIcon(pixmap)