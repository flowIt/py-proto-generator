import argparse
from lepl import * 

class NodeTemplateFromFile:
    def __init__(self): 
        spaces = ~Whitespace()[:]
        with Separator(spaces):
            self.header = Integer() & Word()
            self.kvcouple = ~Literal('(') & Integer() & ~Literal(',') & Integer() & ~Literal(')')
            self.input_line = self.kvcouple & ~Literal('->') & self.kvcouple

    def parse_header(self, header_line):
        return self.header.parse(header_line)

    def parse_line(self, input_line):
        return self.input_line.parse(input_line)

def parse_file(filename):
    node_parser = NodeTemplateFromFile()
    with open(filename, 'r') as f:
        header = node_parser.parse_header(f.readline().strip())
	lines = []
        for line in f:
            lines.append(node_parser.parse_line(line.strip()))
    return header, lines
