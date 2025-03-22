class Emitter:
    def __init__(self, fullPath):
        self.fullPath = fullPath
        self.header = ""
        self.code = ""
        self.indent_level = 0

    def emit(self, code):
        self.code += code

    def emitLine(self, code):
        self.code += ("    " * self.indent_level) + code + "\n"
    
    def headerLine(self, code):
        self.header += code + '\n'  

    def writeFile(self):
        with open(self.fullPath, 'w') as outputFile:
            outputFile.write(self.header + self.code)