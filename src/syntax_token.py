from syntax_node import SyntaxNode

class SyntaxToken(SyntaxNode):
	def __init__(self, pos, content, kind):
		self.pos = pos
		self.content = content
		self.kind = kind

	def __str__(self):
		return f"{self.pos} \t {self.content} \t {self.kind}"

	def kind(self):
		return self.kind

	def get_children(self):
		return []

