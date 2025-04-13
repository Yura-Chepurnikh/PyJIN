from enum import Enum

class SyntaxKind(Enum):
	UNKNOWN_TOKEN = 0
	NUMBER_TOKEN = 1
	ALPHA_TOKEN = 2
	PLUS_TOKEN = 3
	MINUS_TOKEN = 4
	MULTIPLY_TOKEN = 5
	DEVIDE_TOKEN = 6
	LEFT_PARENTHESIS = 7
	RIGHT_PARENTHESIS = 8	
	SPACE_TOKEN = 9
	EOF_TOKEN = 10

	def __str__(self):
		return f"{self.name}"