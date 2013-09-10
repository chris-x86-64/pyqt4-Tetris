from PyQt4 import QtGui, QtCore
from libs.Tetris.Board import Board

class MainWindow(QtGui.QMainWindow):
	def __init__(self):

		"""
		Initialization of MainWindow.
		Geometry is set to 180*380.
		Window title ie set to 'Tetris'.
		Window will appear in the center using self.center().
		"""

		QtGui.QMainWindow.__init__(self)

		self.setGeometry(300, 300, 180, 380)
		self.setWindowTitle('Tetris')

		self.tetrisboard = Board(self)

		self.tetrisboard.start()
		self.center()

	def center(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move(
			(screen.width() - size.width()) / 2,
			(screen.height() - size.height()) / 2
		)
