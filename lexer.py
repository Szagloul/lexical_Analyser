# Set to hold keywords in the grammar
keywords = {
    'program', 'if', 'then', 'else', 'end', 
    'while', 'do', 'print', 'bool', 'int', 
    'true', 'false', 'and', 'or', 'not', 'mod'
}
# Valid symbols 
symbols = {'.', ',', ';', '(', ')', '+', '-', '*', '/','<'}

# Represents a single token with its (position,type,value)
class Token:
    def __init__(self, position, type, value=None):
        self.position = position
        self.type = type
        self.value = value

# Scanner that walks through the input text character by character
class Scanner:
    def __init__(self, text):
        self.text = text
        self.count = 0
        self.line = 1
        self.col = 1
        self.current_token = None
    # Reads the next lexeme and creates the corresponding token
    def next(self):

        # Skip whitespace and update line and column position
        while self.count < len(self.text) and self.text[self.count].isspace():
            if self.text[self.count] == '\n':
                self.line += 1
                self.col = 1
            else:
                self.col += 1
            self.count += 1

        # Create token once scanner has reached the end of text file 
        if self.count >= len(self.text):
            self.current_token = Token((self.line, self.col), "end-of-text", None)
            return
        
        # Save the starting position and current character before scanning
        start_pos = (self.line, self.col)
        current_char = self.text[self.count]
        
        # Check for comments and skip the line
        if current_char == '/' and self.count + 1 < len(self.text) and self.text[self.count + 1] == '/':
            self.count += 2
            while self.count < len(self.text) and self.text[self.count] != '\n':
                self.count += 1
            return self.next()
        
        # Read full word using maximum munch
        if current_char.isalpha():
            word = ""
            while self.count < len(self.text) and (self.text[self.count].isalnum() or self.text[self.count] == '_'):
                word += self.text[self.count]
                self.count += 1
                self.col += 1

            # Determine if word is a keyword or identifier
            if word in keywords:
                self.current_token = Token(start_pos, word, None)
            else:
                self.current_token = Token(start_pos, "ID", word)
            return
        
        # Read full number using maximum munch
        if current_char.isdigit():
            number_str = ""
            while self.count < len(self.text) and self.text[self.count].isdigit():
                number_str += self.text[self.count]
                self.count += 1
                self.col += 1
            self.current_token = Token(start_pos, "NUM", int(number_str))
            return

        # Check for invalid ! and print error
        if current_char == '!':
            if self.count + 1 < len(self.text) and self.text[self.count + 1] == '=':
                self.count += 2
                self.col += 2
                self.current_token = Token(start_pos, "!=", None)
                return
            else:
                print(f"Error at Line: {self.line} Column: {self.col} '!' must be followed by '='")
                exit()

        # Determine if symbol is >= or >
        if current_char == '>':
            if self.count + 1 < len(self.text) and self.text[self.count + 1] == '=':
                self.count += 2
                self.col += 2
                self.current_token = Token(start_pos, ">=", None)
            else:
                self.count += 1
                self.col += 1
                self.current_token = Token(start_pos, ">", None)
            return

        # Determine if symbol is =< or =
        if current_char == '=':
            if self.count + 1 < len(self.text) and self.text[self.count + 1] == '<':
                self.count += 2
                self.col += 2
                self.current_token = Token(start_pos, "=<", None)
            else:
                self.count += 1
                self.col += 1
                self.current_token = Token(start_pos, "=", None)
            return
        
        # Determine if symbol is := or :
        if current_char == ':':
            if self.count + 1 < len(self.text) and self.text[self.count + 1] == '=':
                self.count += 2
                self.col += 2
                self.current_token = Token(start_pos, ":=", None)
            else:
                self.count += 1
                self.col += 1
                self.current_token = Token(start_pos, ":", None)
            return
        
        # Check if character is in the valid symbols set 
        if current_char in symbols:
            self.current_token = Token(start_pos, current_char, None)
            self.count += 1
            self.col += 1
            return
        print(f"Error at Line: {self.line} Column: {self.col} '{current_char}' is not allowed")
        exit()

    # Returns the kind of the current token
    def kind(self):
        return self.current_token.type

    # Returns the value of the current token
    def value(self):
        return self.current_token.value

    # Returns the position of the current token
    def position(self):
        return self.current_token.position

# Get text input
if __name__ == "__main__":
    file_name = input("Enter the name of the text file (e.g., text.txt): ")
    with open(file_name, 'r') as file:
        content = file.read()

    # Create the first token and loop till end of text 
    scanner = Scanner(content)
    scanner.next()
    print(f"{scanner.position()} {scanner.kind()} {scanner.value() if scanner.value() is not None else ''}")
    while scanner.kind() != "end-of-text":
        scanner.next()
        print(f"{scanner.position()} {scanner.kind()} {scanner.value() if scanner.value() is not None else ''}")