#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from libs.MainWindow import MainWindow

app = QtGui.QApplication(sys.argv)
tetris = MainWindow()
tetris.show()

sys.exit(app.exec_())
