from PyQt4 import QtGui, QtCore
from libs.Tetris.Shape import Tetrominoes

class Rendering():

	"""
	This class defines rednering.
	timerEvent()
	shapeLocation()
	setShapeLocation()
	squareWidth()
	squareHeight()
	paintEvent()
	clearBoard()
	dropDown()
	oneLineDown()
	pieceDropped()
	removeFullLines()
	newPiece()
	tryMove()
	drawSquare()
	"""

	def timerEvent(self, event):
		if event.timerId() == self.timer.timerId():
			if self.isWaitingAfterLine:
				self.isWaitingAfterLine = False
				self.newPiece()
			else:
				self.oneLineDown()
		else:
			QtGui.QFrame.timerEvent(self, event)

	def shapeLocation(self, x, y):
		return self.board[(y * self.BoardWidth) + x]

	def setShapeLocation(self, x, y, shape):
		self.board[(y * self.BoardWidth) + x] = shape

	def squareWidth(self):
		return self.contentsRect().width() / self.BoardWidth

	def squareHeight(self):
		return self.contentsRect().height() / self.BoardHeight

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		rect = self.contentsRect()

		boardTop = rect.bottom() - self.BoardHeight * self.squareHeight()

		for i in range(self.BoardHeight):
			for j in range(self.BoardWidth):
				shape = self.shapeLocation(j, self.BoardHeight - i - 1)
				if shape != Tetrominoes.NoShape:
					self.drawSquare(painter,
						rect.left() + j * self.squareWidth(),
						boardTop + i * self.squareHeight(), shape
					)

		if self.curPiece.shape() != Tetrominoes.NoShape:
			for i in range(4):
				x = self.curX + self.curPiece.x(i)
				y = self.curY - self.curPiece.y(i)
				self.drawSquare(painter,
					rect.left() + x * self.squareWidth(),
					boardTop + (self.BoardHeight - y - 1) * self.squareHeight(),
					self.curPiece.shape()
				)

	def clearBoard(self):
		for i in range(self.BoardHeight * self.BoardWidth):
			self.board.append(Tetrominoes.NoShape)

	def dropDown(self):
		newY = self.curY
		while newY > 0:
			if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
				break
			newY -= 1
		self.pieceDropped()

	def oneLineDown(self):
		if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
			self.pieceDropped()

	def pieceDropped(self):
		for i in range(4):
			x = self.curX + self.curPiece.x(i)
			y = self.curY - self.curPiece.y(i)
			self.setShapeLocation(x, y, self.curPiece.shape())
		self.removeFullLines()
		if not self.isWaitingAfterLine:
			self.newPiece()

	def removeFullLines(self):
		numFullLines = 0

		rowsToRemove = []

		for i in range(self.BoardHeight):
			n = 0
			for j in range(self.BoardWidth):
				if not self.shapeLocation(j, i) == Tetrominoes.NoShape:
					n += 1

			if n == 10: # wtf is this magic number?
				rowsToRemove.append(i)

		rowsToRemove.reverse()

		for m in rowsToRemove:
			for k in range(m, self.BoardHeight):
				for l in range(self.BoardWidth):
					self.setShapeLocation(l, k, self.shapeLocation(l, k + 1))

		numFullLines += len(rowsToRemove)

		if numFullLines > 0:
			self.numLinesRemoved += numFullLines
			self.emit(QtCore.SIGNAL("messageToStatusbar(QString)"), str(self.numLinesRemoved))
			self.isWaitingAfterLine = True
			self.curPiece.setShape(Tetrominoes.NoShape)
			self.update()

	def newPiece(self):
		self.curPiece = self.nextPiece
		self.nextPiece.setRandomShape()
		self.curX = self.BoardWidth / 2 + 1
		self.curY = self.BoardHeight - 1 + self.curPiece.minY()

	def drawSquare(self, painter, x, y, shape):
		colorTable = [
			0x000000,
			0xCC6666,
			0x66CC66,
			0x6666CC,
			0xCCCC66,
			0xCC66CC,
			0x66CCCC,
			0xDAAA00
		]
		color = QtGui.QColor(colorTable[shape])

		painter.fillRect(
			x + 1,
			y + 1,
			self.squareWidth() - 2,
			self.squareHeight() - 2,
			color
		)
		painter.setPen(color.light())
		painter.drawLine(x, y + self.squareHeight() - 1, x, y)
		painter.drawLine(x, y, x + self.squareWidth() - 1, y)

	def tryMove(self, newPiece, newX, newY):
		for i in range(4):
			x = newX + newPiece.x(i)
			y = newY - newPiece.y(i)
			if x < 0 or x >= self.BoardWidth or y < 0 or y >= self.BoardHeight:
				return False
			if self.shapeLocation(x, y) != Tetrominoes.NoShape:
				return False

		self.curPiece = newPiece
		self.curX = newX
		self.curY = newY
		self.update()

		return True
