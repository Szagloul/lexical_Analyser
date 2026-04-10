**Name:** Saif Zagloul
**Language:** Python 3.14.2
**Interpreter:** CPython 3.14.2
**IDE:** VS Code

## Files
- `lexer.py` — Lexical analyzer that tokenizes the input source file
- `parser.py` — Syntax analyzer that parses the token stream against the grammar

## How to Execute
1. Place your input file (e.g., `text.txt`) in the same directory as the scripts.
2. Run the program using the command: `py parser.py`
3. When prompted, enter the filename: `text.txt`

## End-User Documentation
The program reads a source file and determines if it is syntactically valid according to the grammar.
- If the input is syntactically correct, the program prints `true` and terminates.
- If a syntax error is encountered, the program prints an error message with the line and column of the error and terminates.
- Whitespace and comments `//` are ignored.