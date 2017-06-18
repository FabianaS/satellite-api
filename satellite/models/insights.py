from flask import jsonify
import psutil
import platform


class SysStats:
    def __init__(self):
        self.cpu_usage = psutil.cpu_percent(interval=1)
        self.cpu_freq = psutil.cpu_freq()
        self.cpu_cores = psutil.cpu_count(logical=False)
        self.mem_usage = psutil.virtual_memory()
        self.net_io = psutil.net_io_counters(pernic=True)
        self.system = platform.system()
        self.os_version = platform.release()
        self.machine = platform.machine()
        self.cpu_arch = platform.processor()
        self.py_ver = platform.python_compiler()

    def serialize(self):
        return {
                "os": self.system,
                "os_version": self.os_version,
                "machine": self.machine,
                "cpu_arch": self.cpu_arch,
                "python_compiler": self.py_ver,
                "cpu_percent_usage": self.cpu_usage,
                "cpu_freq": {"max": self.cpu_freq.max,
                             "min": self.cpu_freq.min,
                             "current": self.cpu_freq.current},
                "cpu_cores": self.cpu_cores,
                "mem_usage": self.mem_usage,
                "net_io": self.net_io
                }

    def as_json(self):
        return jsonify(self.serialize())
