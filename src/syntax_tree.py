class SyntaxTree:
	def __init__(self, diagnostics, root, end_of_file_token):
		self.diagnostics = diagnostics
		self.root = root
		self.end_of_file_token = end_of_file_token
