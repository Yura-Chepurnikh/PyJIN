from syntax_token import SyntaxToken
from syntax_kind import SyntaxKind

class Lexer:
	def __init__(self, pos, text):
		self.pos = 0
		self.text = text

	def get_next_token(self):
		if self.pos > len(self.text):
			return SyntaxToken(self.pos, self.text[self.pos], SyntaxKind.EOF_TOKEN)

		elif self.pos < len(self.text) and self.text[self.pos].isdigit():
			begin = self.pos
			while self.pos < len(self.text) and self.text[self.pos].isdigit():
				self.increment_pos()
			str = self.text[begin:self.pos]
			return SyntaxToken(begin, str, SyntaxKind.NUMBER_TOKEN)

		elif self.pos < len(self.text) and self.text[self.pos].isalpha():
			begin = self.pos
			while self.pos < len(self.text) and self.text[self.pos].isalpha():
				self.increment_pos()
			str = self.text[begin:self.pos]
			return SyntaxToken(begin, str, SyntaxKind.ALPHA_TOKEN)

		elif self.pos < len(self.text) and self.text[self.pos].isspace():
			begin = self.pos
			while self.pos < len(self.text) and self.text[self.pos].isspace():
				self.increment_pos()
			str = self.text[begin:self.pos]
			return SyntaxToken(begin, str, SyntaxKind.SPACE_TOKEN)

		if self.pos < len(self.text):
			if (self.text[self.pos] == '+'):
				current_pos = self.pos
				self.increment_pos()
				return SyntaxToken(current_pos, '+', SyntaxKind.PLUS_TOKEN)

			elif (self.text[self.pos] == '-'):
				current_pos = self.pos
				self.increment_pos()
				return SyntaxToken(current_pos, '-', SyntaxKind.MINUS_TOKEN)

			elif (self.text[self.pos] == '*'):
				current_pos = self.pos
				self.increment_pos()
				return SyntaxToken(current_pos, '*', SyntaxKind.MULTIPLY_TOKEN)
				
			elif (self.text[self.pos] == '/'):
				current_pos = self.pos
				self.increment_pos()
				return SyntaxToken(current_pos, '/', SyntaxKind.DEVIDE_TOKEN)
				
			elif (self.text[self.pos] == '('):
				current_pos = self.pos
				self.increment_pos()
				return SyntaxToken(current_pos, '(', SyntaxKind.LEFT_PARENTHESIS)
				
			elif (self.text[self.pos] == ')'):
				current_pos = self.pos
				self.increment_pos()
				return SyntaxToken(current_pos, ')', SyntaxKind.RIGHT_PARENTHESIS)

			else:
				current_pos = self.pos
				self.increment_pos()
				return SyntaxToken(current_pos, '?', SyntaxKind.UNKNOWN_TOKEN)

	def increment_pos(self):
		self.pos += 1
