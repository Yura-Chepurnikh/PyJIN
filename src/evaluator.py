from number_expression_syntax import NumberExpressionSyntax
from binary_expression_syntax import BinaryExpressionSyntax
from parenthesized_expression_syntax import ParenthesizedExpressionSyntax

from syntax_kind import SyntaxKind

class Evaluator:
	def __init__(self, root):
		self.root = root

	def evaluate(self):
		return self.evaluate_expression(self.root)

	def evaluate_expression(self, node):
		if isinstance(node, NumberExpressionSyntax):
			return int(node.number_token.content)

		elif isinstance(node, BinaryExpressionSyntax):
			left = self.evaluate_expression(node.left)
			right = self.evaluate_expression(node.right)

			if (node.operator_token.kind == SyntaxKind.PLUS_TOKEN):
				return left + right

			elif (node.operator_token.kind == SyntaxKind.MINUS_TOKEN):
				return left - right

			elif (node.operator_token.kind == SyntaxKind.MULTIPLY_TOKEN):
				return left * right

			elif (node.operator_token.kind == SyntaxKind.DEVIDE_TOKEN):
				return left / right

		elif isinstance(node, ParenthesizedExpressionSyntax):
			return self.evaluate_expression(node.expression)
	
		else:
			raise Exception(f"Unexpected node type: {type(node)}")

