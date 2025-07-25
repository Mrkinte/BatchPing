pyside6-uic MainWindow.ui -o ui_main_window.py
pyside6-uic PingWidget.ui -o ui_ping_widget.py
pyside6-uic SettingsWidget.ui -o ui_settings_widget.py

pyside6-rcc ./assets/assets.qrc -o ../assets_rc.py