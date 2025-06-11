from lexer_definitions import Token, TipoToken
from lexer import tokenizar
from ast_parser import Parser

if __name__ == "__main__":
    # Ejemplo de código fuente
    codigo = """
    definir x = 5 + 3

    funcion suma(a, b)
        retornar a + b
    fin

    definir y = suma(5,x)

    si y > 5 entonces
        imprimir("Hola")
    fin
    """

    # Analizar el código fuente
    tokens = tokenizar(codigo)
    print(tokens)

    parser = Parser(tokens)
    # Esto devuelve un nodo 'programa'
    programa = parser.parsear()

    # Imprimir el AST
    print(programa.to_pretty_str())