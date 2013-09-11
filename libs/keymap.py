from PyQt4 import QtGui, QtCore

class keyPressEvent():
	def keyPressEvent(self, event):

		"""
		Handles keypress events.
		Defines keymap.

		Up/Down = Rotate R/L
		Left/Right = Move L/R
		Space = Drop to the bottom
		D = Drop one line
		P = Pause game
		"""

		if not self.isStarted:
			QtGui.QWidget.keyPressEvent(self, event)
			return

		pressedKey = event.key()

		if pressedKey == QtCore.Qt.Key_P:
			self.pause()
			return
		if self.isPaused:
			return
# Other keys such as U/D/L/R, Space, and D comes here.
		else:
			QtGui.QWidget.keyPressEvent(self, event)
