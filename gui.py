#!/usr/bin/python3
"""the main gui component"""
import graph
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
quest = QLabel('Which graph would you like to see?')

delta = QPushButton('Delta')
american = QPushButton('American Airlines')
spirit = QPushButton('Spirit')
jblue = QPushButton('jetBlue')

jblue.clicked.connect(graph.graph_jetblue)
american.clicked.connect(graph.graph_american)
spirit.clicked.connect(graph.graph_spirit)
delta.clicked.connect(graph.graph_delta)

layout.addWidget(quest)
layout.addWidget(jblue)
layout.addWidget(delta)
layout.addWidget(american)
layout.addWidget(spirit)
window.setLayout(layout)
window.show()

app.exec_()
