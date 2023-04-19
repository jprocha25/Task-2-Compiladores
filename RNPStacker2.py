class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class Token:
    def __init__(self, type, lexeme):
        self.type = type
        self.lexeme = lexeme

    def __repr__(self):
        return f"Token [type={self.type}, lexeme={self.lexeme}]"


def scan(input_str):
    tokens = []
    for token_str in input_str.split():
        if token_str.isdigit():
            tokens.append(Token("NUM", token_str))
        elif token_str in {"+", "-", "*", "/"}:
            tokens.append(Token(token_str, token_str))
        else:
            raise ValueError(f"Token Invalido: {token_str}")
    return tokens


entrada = input("Digite a sua entrada em RPN: ")

try:
    tokens = scan(entrada)
except ValueError as e:
    print(e)
    exit()

pilha = Stack()
resultado = None

for token in tokens:
    if token.type == "NUM":
        pilha.push(int(token.lexeme))
    elif token.type in {"+", "-", "*", "/"}:
        b = pilha.pop()
        a = pilha.pop()

        if token.type == '+':
            resultado = a + b
        elif token.type == '-':
            resultado = a - b
        elif token.type == '*':
            resultado = a * b
        elif token.type == '/':
            resultado = a / b

        pilha.push(resultado)

    else:
        raise ValueError(f"Token Invalido: {token.type}")

saida = pilha.pop()

print("\nTokens:")
for token in tokens:
    print(token)

print("\nSaida: ", saida)
