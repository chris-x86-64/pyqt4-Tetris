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
		elif pressedKey == QtCore.Qt.Key_Left:
			self.tryMove(self.curPiece, self.curX - 1, self.curY)
		elif pressedKey == QtCore.Qt.Key_Right:
			self.tryMove(self.curPiece, self.curX + 1, self.curY)
		elif pressedKey == QtCore.Qt.Key_Down:
			self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
		elif pressedKey == QtCore.Qt.Key_Up:
			self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
		elif pressedKey == QtCore.Qt.Key_Space:
			self.dropDown()
		elif pressedKey == QtCore.Qt.Key_D:
			self.oneLineDown()
		else:
			QtGui.QWidget.keyPressEvent(self, event)
