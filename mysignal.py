from PyQt5.QtCore import QObject, pyqtSignal

class mySignal(QObject):
    signalCancel = pyqtSignal(str)