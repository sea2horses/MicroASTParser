from lexer_definitions import Token, TipoToken
from lexer import tokenizar
from ast_parser import Parser

# Ejemplo de código fuente
codigo = """
definir x = 5 + 3

funcion suma(a, b)
    retornar a + b
fin

suma(5,x)
"""

# Analizar el código fuente
tokens = tokenizar(codigo)
print(tokens)

parser = Parser(tokens)
arbol = parser.parsear()

# Imprimir el AST resultante
for nodo in arbol:
    print(nodo.to_pretty_str())