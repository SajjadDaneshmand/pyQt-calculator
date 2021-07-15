import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,
                             QLabel, QPushButton, QVBoxLayout)


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(1680, 30, 250, 80)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
top = QPushButton('Top', parent=window)
center = QPushButton('Center', parent=window)
bottom = QPushButton('Bottom', parent=window)
layout = QVBoxLayout()

layout.addWidget(helloMsg)
layout.addWidget(top)
layout.addWidget(center)
layout.addWidget(bottom)

window.setLayout(layout)

window.show()
sys.exit(app.exec_())