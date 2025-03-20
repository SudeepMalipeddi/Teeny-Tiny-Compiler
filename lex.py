import sys
import enum

class Lexer:
    def __init__(self,source):
        self.source = source + '\n'
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    # Process the next character in the source code
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0'
        else:
            self.curChar = self.source[self.curPos]

    # Return the lookahead character
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos + 1]

    # Invalid Token found, print error message and exit
    def error(self, message):
        pass

    # Skip whitespace characters except newlines
    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()

    # Skip comments
    def skipComments(self):
        if self.curChar == '#':
            while self.curChar != '\n':
                self.nextChar()


    # abort function
    def abort(self,message):
        sys.exit("Lexing error. " + message)

    # Skip comments in the code
    def getToken(self):
        # check the first character to this token to see if we can decide what it is
        #
        self.skipWhitespace()
        self.skipComments()
        token = None
        
        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)
        
        elif self.curChar == '\n':
            token = Token(self.curChar, TokenType.NEWLINE)
        
        elif self.curChar == '\0':
            token = Token(self.curChar, TokenType.EOF)
        
        elif self.curChar == '=':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.EQEQ)
            else:
                token = Token(self.curChar, TokenType.EQ)
        
        elif self.curChar == '>':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.GTEQ)
            else:
                token = Token(self.curChar, TokenType.GT)
        
        elif self.curChar == '<':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.LTEQ)
            else:
                token = Token(self.curChar, TokenType.LT)
        
        elif self.curChar == '!':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.NOTEQ)
            else:
                self.abort("Expected != but got !" + self.peek())

        elif self.curChar == '\"':
            self.nextChar()
            startPos = self.curPos
            
            while self.curChar != '\"':
                if self.curChar == '\r' or self.curChar == '\n' or self.curChar == '\t' or self.curChar == '\\' or self.curChar == '%':
                    self.abort("Illegal character in string.")
                self.nextChar()
            
            tokText = self.source[startPos : self.curPos] # getting the substring
            token = Token(tokText,TokenType.STRING)

        
        elif self.curChar.isdigit():
            
            startPos = self.curPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek() == '.':
                self.nextChar()
                if not self.peek().isdigit():
                    self.abort("Illegal character in number.")
                while self.peek().isdigit():
                    self.nextChar()

            tokText = self.source[startPos: self.curPos + 1]
            token = Token(tokText, TokenType.NUMBER)

        elif self.curChar.isalpha():
            startPos = self.curPos
            while self.peek().isalnum():
                self.nextChar()
            
            tokText = self.source[startPos: self.curPos + 1]
            keyword = Token.checkIfKeyword(tokText)
            if keyword == None:
                token = Token(tokText, TokenType.IDENT)
            else:
                token = Token(tokText, keyword)

        else:
            self.abort("Unknown token: " + self.curChar)

        self.nextChar()
        return token


class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind

    @staticmethod
    def checkIfKeyword(tokenText):
        for kind in TokenType:
            # Relies on all keyword enum values being 1XX.
            if kind.name == tokenText and kind.value >= 100 and kind.value < 200:
                return kind
        return None

class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3

    # Keywords
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111

    # Operators
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211

