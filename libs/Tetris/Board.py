from PyQt4 import QtGui, QtCore
from libs.Tetris.Shape import Shape, Tetrominoes
from libs.keymap import keyPressEvent

class Board(QtGui.QFrame, keyPressEvent):
	BoardWidth = 10  # This defines the width of the game board (10 blocks)
	BoardHeight = 22 # This defines the height of the game board (22 blocks)
	Speed = 300 # This defines the game's speed (300 milliseconds)

	def __init__(self, parent):

		"""
		Initializes QFrame.
		Initializes attributes.
		Sets timer.
		"""

		QtGui.QFrame.__init__(self, parent)

		self.timer = QtCore.QBasicTimer()

# begin: attributes
		self.isWaitingAfterLine = False
		self.curPiece = Shape()
		self.nextPiece = Shape()
		self.curX = 0
		self.curY = 0
		self.numLinesRemoved = 0
		self.isStarted = False
		self.isPaused = False
		self.board = []
# end: attributes

		self.clearBoard()
		self.setFocusPolicy(QtCore.Qt.StrongFocus)
		self.nextPiece.setRandomShape()

	def start(self):

		"""
		Starts the timer if not paused.
		"""

		if self.isPaused:
			return

		self.isStarted = True
		self.numLinesRemoved = 0

		self.emit(QtCore.SIGNAL("messageToStatusbar(QString)"), str(self.numLinesRemoved))
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
			self.emit(QtCore.SIGNAL("messageToStatusbar(QString)"), str(self.numLinesRemoved))

		self.update()

	def clearBoard(self):
		for i in range(Board.BoardHeight * Board.BoardWidth):
			self.board.append(Tetrominoes.NoShape)

