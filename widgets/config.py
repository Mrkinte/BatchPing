import os

from qfluentwidgets import QConfig, BoolValidator, ConfigItem, RangeValidator, qconfig, ConfigValidator, RangeConfigItem


class Config(QConfig):
    maxThreadNums = RangeConfigItem("PingWork", "MaxThreadNums", 127, RangeValidator(1, 254))


version = "1.0.0"
cfg = Config()
qconfig.load(os.getenv('LOCALAPPDATA') + "\\BatchPing\\config.json", cfg)