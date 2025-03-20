# Teeny Tiny Compiler

A simple compiler that translates a dialect of BASIC into C code.

## Overview

This project implements a compiler for a minimalist BASIC-like language. The compiler follows a standard compilation process:
- Lexical analysis (tokenization)
- Syntax analysis (parsing)
- Code generation (C output)

This implementation is based on the "Teeny Tiny Compiler" tutorial by Austin Henley:
[Teeny Tiny Compiler](https://austinhenley.com/blog/teenytinycompiler1.html)

## Current Status

The project currently implements the lexical analyzer (lexer) component, which identifies tokens like:
- Keywords (IF, THEN, WHILE, etc.)
- Operators (+, -, *, /, =, ==, etc.)
- Identifiers, numbers, and strings

## Implementation Details

The compiler is written in Python and consists of:
- `lex.py` - Tokenizer/lexical analyzer
- `teenytiny.py` - Main compiler driver




## Usage

```python
python teenytiny.py 

