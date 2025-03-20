from lex import *

def main():
    source = "+- */ > >= = !="
    source = "+- # This is a comment!\n */"
    source = "+- \"This is a string\" # This is a comment!\n */"
    source = "+-123 9.8654*/"
    source = "IF+-123 foo*THEN/"
    lexer = Lexer(source)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

main()