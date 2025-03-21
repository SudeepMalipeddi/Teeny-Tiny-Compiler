from lex import *
from emit import *
from parse import *
import sys
def main():
    print("Teeny Tiny Compiler")

    if len(sys.argv) != 2:
        sys.stderr.write("Usage: teenytiny.py <source file>\n")
        sys.exit("Error: Compiler needs source file as argument.")

    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()


    lexer = Lexer(source)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program()
    emitter.writeFile()
    print("Compiling complete.")

main()