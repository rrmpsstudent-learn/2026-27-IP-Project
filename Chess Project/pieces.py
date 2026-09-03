class Piece:
	"""Makes an object piece and assigns the basic attributes of every piece."""
	def __init__(self, rank, color, position):
		self.rank = rank
		self.color = color
		self.current_position = position


