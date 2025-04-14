from abc import ABC, abstractmethod

class SyntaxNode(ABC):
	@property
	@abstractmethod
	def kind(self):
		pass

	@abstractmethod
	def get_children(self):
		pass

	def __iter__(self):
		return iter(self.get_children())
