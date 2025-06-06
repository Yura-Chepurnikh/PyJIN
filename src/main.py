from syntax_token import SyntaxToken
from syntax_kind import SyntaxKind
from syntax_tree import SyntaxTree
from evaluator import Evaluator
from parser import Parser
from lexer import Lexer

def main():
	while True:
		line = input('> ')

		if (is_null_or_white_space(line)):
			return

		parser = Parser(line)
		syntax_tree = parser.parse()
		print_unix_like_tree(syntax_tree.root)
		evaluator = Evaluator(syntax_tree.root)

		print(f"Result: {evaluator.evaluate()}")


def is_null_or_white_space(s):
	return s is None or s.strip() == ''

def print_unix_like_tree(node, indent = "", is_last = True):
	#print("---Starting print_unix_like_tree---")
	flag = "└──" if is_last else "├──"

	if isinstance(node, SyntaxToken) and node.content is not None:
		print(indent + flag + str(node.kind) + " " + str(node.content))

	else:
		print(indent + flag + str(node.kind))


	children = list(node.get_children())
	last_child = children[-1] if children else None

	for child in children:
		print_unix_like_tree(
			child,
			indent + ("    " if is_last else "│   "),
			child is last_child
		)

if __name__ == "__main__":
	main()