from expression_syntax import ExpressionSyntax

class ParenthesizedExpressionSyntax(ExpressionSyntax):
	def __init__(self, left_parenthesis, expression, right_parenthesis):
		self.left_parenthesis = left_parenthesis
		self.expression = expression
		self.right_parenthesis = right_parenthesis

	def kind:
		return SyntaxKind.PARENTHESIZED_EXPRESSION_SYNTAX

	def get_children(self):
		yield left_parenthesis
		yield expression
		yield right_parenthesis
	
