from expression_syntax import ExpressionSyntax
from syntax_kind import SyntaxKind

class NumberExpressionSyntax(ExpressionSyntax):
	def __init__(self, number_token):
		self.number_token = number_token

	def kind:
		return SyntaxKind.NUMBER_EXSPRESSION_TOKEN

	def get_children(self):
		yield number_token