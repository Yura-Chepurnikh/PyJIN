class SyntaxToken:
	def __init__(self, pos, content, kind):
		self.pos = pos
		self.content = content
		self.kind = kind

	def __str__(self):
		return f"{self.pos} \t {self.content} \t {self.kind}"

