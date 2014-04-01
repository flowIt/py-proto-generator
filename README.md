py-proto-generator
==================

This project is meant to generate a setup method in a template file called setup.py
in order to transform a simple text file with a specific format into a code that generates
a setup of nodes.

The format of the simple text file is very basic,

The first line is composed of two elements:
- A number of blocks
- The type of blocks

The following lines describes the links between the blocks:
(A,B) -> (C,D)
Where
- A is the block index from which to connect from
- B is the output index of the block to be connected with
- C is the block index from which to connect to
- D is the input index of the block to connect to

To install the dependencies, you can use pip

pip install -r requierements.txt

Then to generate the output file:

cog -D input_file=example.txt setup.py
