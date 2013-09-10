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

		self.timer = QtCore.QBasicTimer()

	def start(self):

		self.timer.start(Board.Speed, self)
