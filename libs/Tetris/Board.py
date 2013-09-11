from PyQt4 import QtGui, QtCore

class Board(QtGui.QFrame):
	BoardWidth = 10  # This defines the width of the game board (10 blocks)
	BoardHeight = 22 # This defines the height of the game board (22 blocks)
	Speed = 300 # This defines the game's speed (300 milliseconds)

	def __init__(self, parent):

		"""
		Initializes QFrame.
		Sets timer.
		"""

		QtGui.QFrame.__init__(self, parent)

		self.setFocusPolicy(QtCore.Qt.StrongFocus)
		self.isStarted = False
		self.isPaused = False
		self.timer = QtCore.QBasicTimer()

	def start(self):

		"""
		Starts the timer if not paused.
		"""

		if self.isPaused:
			return

		self.isStarted = True
		self.timer.start(Board.Speed, self)

	def pause(self):

		"""
		Allows users to pause the game by pressing a key defined at ${method}.
		This will cause the timer to stop counting.
		"""

		if not self.isStarted:
			return

		self.isPaused = not self.isPaused # Revert its value
		if self.isPaused:
			self.timer.stop()
			self.emit(QtCore.SIGNAL("messageToStatusbar(QString)"), "Paused")
		else:
			self.timer.start(Board.Speed, self)
			self.emit(QtCore.SIGNAL("messageToStatusbar(QString)"), "") # After numLinesRemoved is implemented, make the status bar show it.

		self.update()

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
