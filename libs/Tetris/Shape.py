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
