from random import randint

class Tetrominoes(object):

	"""
	Defines each shape's name and No. so human reads the name while the program reads the numeric id.
	The numbers are also used as the index for tuple 'Shape.coordTable'

	For example, Shape.coordsTable[Tetrominoes.TShape] will point to Shape.coordsTable[5],
	which will return ((-1, 0),   (0, 0),    (1, 0),    (0, 1))
	"""

	NoShape = 0
	ZShape = 1
	SShape = 2
	LineShape = 3
	TShape = 4
	SquareShape = 5
	LShape = 6
	MirroredLShape = 7

class Shape(object):
	coordsTable = (
		((0, 0),    (0, 0),    (0, 0),    (0, 0)),  # NoShape
		((0, -1),   (0, 0),    (1, 0),    (1, 1)),  # ZShape
		((0, -1),   (0, 0),    (-1, 0),   (-1, 1)), # SShape
		((0, -1),   (0, 0),    (0, 1),    (0, 2)),  # LineShape
		((-1, 0),   (0, 0),    (1, 0),    (0, 1)),  # TShape
		((0, 0),    (0, 1),    (1, 1),    (1, 0)),  # SquareShape
		((1, -1),   (0, -1),   (0, 0),    (0, 1)),  # LShape
		((-1, -1),  (0, -1),   (0, 0),    (0, 1)),  # MirroredLShape
	)

	def __init__(self):
		self.coords = [ [0, 0] for i in range(4) ]
		self.pieceShape = Tetrominoes.NoShape
		self.setShape(Tetrominoes.NoShape)

	def shape(self):
		return self.pieceShape

	def setShape(self, shape):

		"""
		Reads arrangement data from Shape.coordsTable of the 
		specified shape defined via the argument 'shape',
		then set self.coords[i][j] to the shape's arrangement.
		"""

		arrangement = Shape.coordsTable[shape]

		for i in range(4):
			for j in range(2):
				self.coords[i][j] = arrangement[i][j]

		self.pieceShape = shape

	def setRandomShape(self):
		self.setShape(randint(1, 7))

	def x(self, index):
		return self.coords[index][0]

	def y(self, index):
		return self.coords[index][1]

	def setX(self, index, x):
		self.coords[index][0] = x

	def setY(self, index, y):
		self.coords[index][1] = y

	def minX(self):
		m = self.coords[0][0]
		for i in range(4):
			m = min(m, self.coords[i][0])

		return m

	def minY(self):
		m = self.coords[0][1]
		for i in range(4):
			m = min(m, self.coords[i][1])

		return m

	def maxX(self):
		m = self.coords[0][0]
		for i in range(4):
			m = max(m, self.coords[i][0])

		return m

	def maxY(self):
		m = self.coords[0][1]
		for i in range(4):
			m = max(m, self.coords[i][1])

		return m

	def rotateLeft(self):
		if self.pieceShape == Tetrominoes.SquareShape:
			return self # There's no need to rotate SquareShape because the result will be the exact same shape.

		result = Shape()
		result.pieceShape = self.pieceShape
		for i in range(4):
			result.setX(i, self.y(i))
			result.setY(i, -self.x(i))

		return result

	def rotateRight(self):
		if self.pieceShape == Tetrominoes.SquareShape:
			return self # There's no need to rotate SquareShape because the result will be the exact same shape.

		result = Shape()
		result.pieceShape = self.pieceShape
		for i in range(4):
			result.setX(i, -self.y(i))
			result.setY(i, self.x(i))

		return result
