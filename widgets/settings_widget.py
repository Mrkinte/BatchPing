import os

from PySide6.QtWidgets import QWidget, QSpacerItem, QSizePolicy
from qfluentwidgets import HyperlinkCard, FluentIcon, PrimaryPushSettingCard, RangeSettingCard

from design.Ui_SettingsWidget import Ui_SettingsWidget
from widgets.config import cfg
from widgets.config import version

class SettingsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SettingsWidget()
        self.ui.setupUi(self)

        self.max_thread_nums = RangeSettingCard(
            cfg.maxThreadNums,
            FluentIcon.SPEED_HIGH,
            title="最大线程数",
            content=f"允许同时对多少个IP进行测试"
        )

        self.update_card = HyperlinkCard(
            url="https://github.com/Mrkinte/BatchPing",
            text="跳转至Github",
            icon=FluentIcon.UPDATE,
            title=f"获取最新版本（当前版本{version}）",
            content="在Github中获取最新版本"
        )

        self.issue_card = HyperlinkCard(
            url="https://github.com/Mrkinte/BatchPing/issues",
            text="跳转至Github",
            icon=FluentIcon.QUESTION,
            title="问题反馈",
            content="在Github中反馈遇到的Bug"
        )

        self.open_config_card = PrimaryPushSettingCard(
            text="打开",
            icon=FluentIcon.HELP,
            title="配置文件夹",
            content=os.getenv('LOCALAPPDATA') + "\\BatchPing"
        )
        self.open_config_card.clicked.connect(self.openConfigDir)

        self.ui.settingsLayout.addWidget(self.max_thread_nums)
        self.ui.settingsLayout.addWidget(self.open_config_card)
        self.ui.settingsLayout.addWidget(self.update_card)
        self.ui.settingsLayout.addWidget(self.issue_card)
        self.ui.settingsLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Fixed, QSizePolicy.Expanding))

    def openConfigDir(self):
        os.startfile(self.open_config_card.contentLabel.text())