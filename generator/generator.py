from parsing.parsing import parse_file

class Generator:
	def __init__(self, input_file):
		self.input_file = input_file
		self.header, self.lines = parse_file(input_file)

	def header(self):
		return self.header
