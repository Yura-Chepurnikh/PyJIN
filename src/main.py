from syntax_token import SyntaxToken
from syntax_kind import SyntaxKind
from lexer import Lexer

def main():
	text = "(143 + 903) *       123"
	lexer = Lexer(text)

	while True:
		token = lexer.get_next_token()

		if token is None:
			break

		if token.kind == SyntaxKind.EOF_TOKEN:
			break

		print(token)


if __name__ == "__main__":
	main()