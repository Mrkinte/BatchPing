import concurrent.futures

from PySide6.QtCore import QObject, Signal, QMutex
from pythonping import ping

from widgets.config import cfg


class PingWorker(QObject):
    progress_signal = Signal(int, dict)     # 进度信号(序号, 结果字典)
    finished_signal = Signal(bool)  # 完成信号(True:正常结束  False:手动停止)
    ping_error_signal = Signal()

    def __init__(self, ip_prefix):
        super().__init__()
        self.ip_prefix = ip_prefix
        self.thread_pool = None
        self.running = True
        self.lock = QMutex()

    def stop(self):
        """停止所有Ping任务"""
        self.lock.lock()
        self.running = False
        self.lock.unlock()
        if self.thread_pool:
            self.thread_pool.shutdown(wait=False)

    def isRunning(self):
        """检查是否仍在运行"""
        self.lock.lock()
        running = self.running
        self.lock.unlock()
        return running

    def pingIp(self, ip: str):
        """执行Ping操作并返回结果"""
        if not self.isRunning():
            return None

        try:
            response = ping(ip, timeout=1)
            rtt_max_ms = response.rtt_max_ms
            rtt_min_ms = response.rtt_min_ms
            rtt_avg_ms = response.rtt_avg_ms
            packet_loss = response.packet_loss * 100

            if packet_loss < 100.0:
                return {"结果": "成功", "丢包率": packet_loss, "最大延迟": rtt_max_ms , "最小延迟": rtt_min_ms, "平均延迟": rtt_avg_ms, "进度": 0}
            else:
                return {"结果": "失败", "丢包率": packet_loss, "最大延迟": rtt_max_ms , "最小延迟": rtt_min_ms, "平均延迟": rtt_avg_ms, "进度": 0}
        except OSError as e:
            self.ping_error_signal.emit()
            self.stop()

    def run(self):
        """线程执行主函数 - 使用线程池执行多个Ping任务"""
        self.thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=cfg.get(cfg.maxThreadNums))
        futures = {}

        # 提交所有Ping任务
        for idx in range(1, 255):
            if not self.isRunning():
                break

            ip = f"{self.ip_prefix}{idx}"
            future = self.thread_pool.submit(self.pingIp, ip)
            future.idx = idx
            futures[future] = idx

        # 处理完成的任务
        completed = 0
        for future in concurrent.futures.as_completed(futures):
            if not self.isRunning():
                break

            idx = futures[future]
            result = future.result()
            if result is not None:
                completed += 1
                result["进度"] = completed
                self.progress_signal.emit(idx, result)

        if completed >= 254:
            self.finished_signal.emit(True)
        else:
            self.finished_signal.emit(False)