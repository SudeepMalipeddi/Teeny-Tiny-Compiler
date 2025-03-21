from lex import *
from parse import *
import sys
def main():
    print("Teenytiny Compiler")
    # source = "+- */ > >= = !="
    # source = "+- # This is a comment!\n */"
    # source = "+- \"This is a string\" # This is a comment!\n */"
    # source = "+-123 9.8654*/"
    # source = "IF+-123 foo*THEN/"

    if len(sys.argv) != 2:
        sys.stderr.write("Usage: teenytiny.py <source file>\n")
        sys.exit("Error: Compiler needs source file as argument.")

    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()


    lexer = Lexer(source)
    parser = Parser(lexer)

    parser.program()
    print("Parsing complete.")

main()