from PySide6.QtCore import QProcess

s = QProcess()
s.setProgram('')
s.setArguments(['./server.py', '--host', '0.0.0.0', '--port', '50000'])
print(s.arguments())
s.start()