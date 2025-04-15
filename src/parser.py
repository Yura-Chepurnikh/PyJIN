from lexer import Lexer
from syntax_kind import SyntaxKind

class Parser: 
	def __init__(self, text, tokens, position = 0):
		self.position = position
		self.text = text
		self.tokens = tokens

		lexer = Lexer(text)

		while True:
			token = lexer.get_next_token()

			if token.kind == SyntaxKind.EOF_TOKEN:
				break

			if token.kind != SyntaxKind.SPACE_TOKEN or token.kind != SyntaxKind.UNKNOWN_TOKEN:
				tokens.append(token)

	def parse():
		

	def peek(self, shift):
		index = self.position + shift

		if index > len(self.tokens):
			return tokens[len(tokens) - 1]

		return tokens[index]

	def current_token():
		return peek(0)

	def get_parser_next_token(self):
		current = current_token()
		self.position += 1
		return current

	def match(kind):
		if (current_token.kind == kind):
			return get_parser_next_token()
		return SyntaxToken(kind, current_token, None)



