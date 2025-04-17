from expression_syntax import ExpressionSyntax
from syntax_kind import SyntaxKind

class NumberExpressionSyntax(ExpressionSyntax):
	def __init__(self, number_token):
		self.number_token = number_token

	@property
	def kind(self):
		return SyntaxKind.NUMBER_EXPRESSION_TOKEN

	def get_children(self):
		yield self.number_token