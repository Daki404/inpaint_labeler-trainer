import subprocess
import threading

from PyQt5 import QtCore


class Worker(QtCore.QObject):
    outSignal = QtCore.pyqtSignal(str)

    def run_command(self, cmd, **kwargs):
        print('입력')
        threading.Thread(
            target=self._execute_command, args=(cmd,), kwargs=kwargs, daemon=True
        ).start()

    def _execute_command(self, cmd, **kwargs):
        print('출력')
        proc = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, **kwargs
        )
        for line in proc.stdout:
            self.outSignal.emit(line.decode())