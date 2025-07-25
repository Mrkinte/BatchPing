import os
import sys

from PySide6.QtWidgets import QApplication
from qfluentwidgets import setThemeColor
from qframelesswindow.utils import getSystemAccentColor

from widgets.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication()

    config_dir = os.getenv('LOCALAPPDATA') + "\\BatchPing"
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    if sys.platform in ["win32", "darwin"]:
        setThemeColor(getSystemAccentColor(), save=False)

    main_window = MainWindow()
    main_window.show()

    app.exec()