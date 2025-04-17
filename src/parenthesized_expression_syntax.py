from expression_syntax import ExpressionSyntax
from syntax_kind import SyntaxKind

class ParenthesizedExpressionSyntax(ExpressionSyntax):
	def __init__(self, left_parenthesis, expression, right_parenthesis):
		self.left_parenthesis = left_parenthesis
		self.expression = expression
		self.right_parenthesis = right_parenthesis

	@property
	def kind(self):
		return SyntaxKind.PARENTHESIZED_EXPRESSION_SYNTAX

	def get_children(self):
		yield self.left_parenthesis
		yield self.expression
		yield self.right_parenthesis
	
