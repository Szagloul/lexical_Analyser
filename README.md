# Mini grammer Lexer & Parser

A top-down recursive descent parser and lexical analyzer built with Python.

## Features

- **Maximum Munch Lexing**:
  - The scanner uses a greedy approach to correctly distinguish between similar operators like `:`, `:=`, `=`, and `=<`.
- **Recursive Descent Parsing**:
  - A predictive parser that validates code structure through a clean hierarchy of methods (Program → Body → Statements → Expressions).
- **Comprehensive Operator Support**:
  - Full implementation of mathematical operators (`+`, `-`, `*`, `/`, `mod`) and logical operators (`and`, `or`, `not`).
- **Dynamic Error Reporting**:
  - Precise error tracking that provides the exact line and column number when a syntax or lexical error is encountered.
- **Robust Comment Handling**:
  - Built-in logic to identify and skip single-line comments (`//`), allowing for documented source code.
- **Stateful Tokenization**:
  - Objects that preserve the token's exact position, type, and value for downstream debugging or interpretation.

## Usage

1. Ensure you have **Python 3.14.2** installed.
2. Prepare a text file (e.g., `source.txt`) containing your code.
3. Run the script via your terminal:
   ```bash
   python main.py

## Technologies Used

- **Python 3.14.2**
- **Standard I/O & File Handling** (Standard Library)
- **Object-Oriented Design**

## Skills Demonstrated

- **Lexical Analysis**: Crafting a state-based scanner to convert raw character streams into a stream of meaningful tokens.
- **Syntactic Analysis**: Implementing EBNF (Extended Backus-Naur Form) grammar rules via recursive function calls.
- **Error Handling: Implementing**: "fail-fast" logic that halts execution with descriptive feedback upon encountering invalid syntax.
- **Lookahead Logic**: Using a one-token lookahead (csym) to determine the correct execution path without backtracking.
- **Formal Grammar Implementation**: Translating high-level language specifications into programmatic validation logic.


## License

This project is licensed under the MIT License. See the [LICENSE] file for details.

---

*Created by Saif Zagloul*
