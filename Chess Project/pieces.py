class Piece:
	"""Makes an object piece and assigns the basic attributes of every piece."""
	def __init__(self, rank, color, position):
		self.rank = rank
		self.color = color
		self.current_position = position
	def __str__(self):
		return (f"{self.rank}{self.color}{self.current_position}")

