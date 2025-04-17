from syntax_token import SyntaxToken
from syntax_kind import SyntaxKind
from syntax_tree import SyntaxTree
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

def is_null_or_white_space(s):
	return s is None or s.strip() == ''

def print_unix_like_tree(node, indent = "", is_last = True):
	flag = "└──" if is_last else "├──"
	print(indent + flag + node.kind)

	if (isinstance(node, SyntaxToken) and node.value is not None):
	    print(indent + "\t" + str(node.value))

    children = node.get_children()
	last_child = children[-1] if children else None

	for child in children:
		print_unix_like_tree(
            child,
            indent + ("    " if is_last else "│   "),
            child is last_child
        )

if __name__ == "__main__":
	main()