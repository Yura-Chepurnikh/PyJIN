from expression_syntax import ExpressionSyntax
from syntax_kind import SyntaxKind

class BinaryExpressionSyntax(ExpressionSyntax):	
	def __init__(self, left, operator_token, right):
		self.left = left
		self.operator_token = operator_token
		self.right = right

	@property
	def kind(self):
		return SyntaxKind.BINARY_EXPRESSION_TOKEN

	def get_children(self):
		yield self.left
		yield self.operator_token
		yield self.right
