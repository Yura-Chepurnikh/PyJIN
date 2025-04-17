from lexer import Lexer
from syntax_kind import SyntaxKind
from syntax_tree import SyntaxTree
from syntax_token import SyntaxToken
from expression_syntax import ExpressionSyntax
from parenthesized_expression_syntax import ParenthesizedExpressionSyntax
from number_expression_syntax import NumberExpressionSyntax
from binary_expression_syntax import BinaryExpressionSyntax

class Parser: 
	def __init__(self, text, tokens = [], diagnostics = [], position = 0):
		self.position = position
		self.text = text
		self.tokens = tokens
		self.diagnostics = diagnostics

		lexer = Lexer(text)

		while True:
			token = lexer.get_next_token()

			if token.kind == SyntaxKind.EOF_TOKEN:
				break

			if token.kind != SyntaxKind.SPACE_TOKEN and token.kind != SyntaxKind.UNKNOWN_TOKEN:
				self.tokens.append(token)

	def peek(self, shift):
		index = self.position + shift

		if index >= len(self.tokens):
			return self.tokens[len(self.tokens) - 1]

		return self.tokens[index]

	def get_current_token(self):
		return self.peek(0)

	def get_parser_next_token(self):
		current = self.get_current_token()
		self.position += 1
		return current

	def match(self, kind):
		if (self.get_current_token().kind == kind):
			return self.get_parser_next_token()

		self.diagnostics.append(f"ERROR: Unexpected token <{self.get_current_token().kind}>, expected <{kind}>")
		return SyntaxToken(kind, self.get_current_token(), None)
	
	def parse(self):
		#print("---Startin parsing---")
		expression = self.parse_expression()
		end_of_file_token = self.match(SyntaxKind.EOF_TOKEN)
		#print("---Ending parsing---")
		return SyntaxTree(self.diagnostics, expression, end_of_file_token)


	def parse_expression(self):
		return self.parse_term()

	def parse_term(self):
		#print("---Startin parse_term---")

		left = self.parse_factor()

		while (self.get_current_token().kind == SyntaxKind.PLUS_TOKEN or self.get_current_token().kind == SyntaxKind.MINUS_TOKEN):
			operator_token = self.get_parser_next_token()
			right = self.parse_factor()
			left = BinaryExpressionSyntax(left, operator_token, right)

		#print("---Ending parse_term---")
		return left


	def parse_factor(self):
		#print("---Startin parse_factor---")

		left = self.parse_primary_expression()

		while (self.get_current_token().kind == SyntaxKind.MULTIPLY_TOKEN or self.get_current_token().kind == SyntaxKind.DEVIDE_TOKEN):
			operator_token = self.get_parser_next_token()
			right = self.parse_primary_expression()
			left = BinaryExpressionSyntax(left, operator_token, right)
		#print("---Startin parse_factor---")

		return left

	def parse_primary_expression(self):
		#print("---Startin parse_primary_expression---")

		if self.get_current_token().kind == SyntaxKind.LEFT_PARENTHESIS:
			left = self.get_parser_next_token()
			expression = self.parse_expression()
			right = self.match(SyntaxKind.RIGHT_PARENTHESIS)
			return ParenthesizedExpressionSyntax(left, expression, right)

		number_token = self.match(SyntaxKind.NUMBER_TOKEN)

		#print("---Startin parse_primary_expression---")

		return NumberExpressionSyntax(number_token)


