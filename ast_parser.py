import ast_classes as ast
from lexer_definitions import TipoToken, Token

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def actual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def avanzar(self):
        self.pos += 1

    def consumir(self, tipo):
        token = self.actual()
        if token and token.Tipo == tipo:
            self.avanzar()
            print(f"Token Consumido: {token}")
            return token
        else:
          raise Exception(f"Se esperaba {tipo}, se encontró {token.Tipo if token else 'EOF'}")

    def parsear(self):
        nodos = []
        while self.actual() is not None:
            nodos.append(self.declaracion())
        return nodos

    def declaracion(self):
        token = self.actual()
        if token.Tipo == TipoToken.PALABRA_CLAVE and token.Valor == "definir":
            return self.declaracion_variable()
        elif token.Tipo == TipoToken.PALABRA_CLAVE and token.Valor == "funcion":
            return self.declaracion_funcion()
        elif token.Tipo == TipoToken.PALABRA_CLAVE and token.Valor == "retornar":
            return self.retorno()
        elif token.Tipo == TipoToken.PALABRA_CLAVE and token.Valor == "si":
            return self.ifexpresion()
        elif token.Tipo == TipoToken.PALABRA_CLAVE and token.Valor == "mientras":
            return self.whileexpresion()
        else:
            return self.expresion()

    def declaracion_variable(self):
        self.consumir(TipoToken.PALABRA_CLAVE)  # definir
        nombre = self.consumir(TipoToken.VARIABLE)
        self.consumir(TipoToken.IGUAL)
        valor = self.expresion()
        return ast.AsignacionAST(nombre.Valor, valor)

    def declaracion_funcion(self):
        self.consumir(TipoToken.PALABRA_CLAVE)  # funcion
        nombre = self.consumir(TipoToken.VARIABLE)
        self.consumir(TipoToken.ABRIR_PARENTESIS)
        parametros = []
        if self.actual().Tipo != TipoToken.CERRAR_PARENTESIS:
            while True:
                param = self.consumir(TipoToken.VARIABLE)
                parametros.append(param.Valor)
                if self.actual().Tipo == TipoToken.COMA:
                    self.consumir(TipoToken.COMA)
                else:
                    break
        self.consumir(TipoToken.CERRAR_PARENTESIS)
        cuerpo = []
        while self.actual() and not (self.actual().Tipo == TipoToken.PALABRA_CLAVE and self.actual().Valor == "fin"):
            cuerpo.append(self.declaracion())
        self.consumir(TipoToken.PALABRA_CLAVE)  # fin
        return ast.FuncionAST(nombre.Valor, parametros, cuerpo)
    
    def retorno(self):
        self.consumir(TipoToken.PALABRA_CLAVE)
        valor = self.expresion()
        return ast.RetornoAST(valor)
      
    def expresion(self):
        return self.expresion_binaria()

    def expresion_binaria(self, prioridad_min=1):
        izquierda = self.primario()
        while True:
            token = self.actual()
            if token and token.Tipo == TipoToken.OPERADOR and self.prioridad(token.Valor) >= prioridad_min:
                op = token.Valor
                self.avanzar()
                derecha = self.expresion_binaria(self.prioridad(op) + 1)
                izquierda = ast.ExpresionBinariaAST(izquierda, op, derecha)
            else:
                break
        return izquierda

    def prioridad(self, op):
        # Puedes usar tu función precedencia aquí
        from lexer_definitions import precedencia
        return precedencia(op)

    def primario(self):
        token = self.actual()
        if token.Tipo == TipoToken.NUMERO:
            self.avanzar()
            return ast.NumeroAST(token.Valor)
        elif token.Tipo == TipoToken.STRING:
            self.avanzar()
            return ast.StringAST(token.Valor)
        elif token.Tipo == TipoToken.VARIABLE:
            self.avanzar()
            if self.actual() and self.actual().Tipo == TipoToken.ABRIR_PARENTESIS:
                return self.llamada_funcion(token.Valor)
            return ast.VariableAST(token.Valor)
        elif token.Tipo == TipoToken.ABRIR_PARENTESIS:
            self.avanzar()
            expr = self.expresion()
            self.consumir(TipoToken.CERRAR_PARENTESIS)
            return expr
        else:
            raise Exception(f"Token inesperado: {token}")
    
    def ifexpresion(self):
        self.consumir(TipoToken.PALABRA_CLAVE)
        condicion = self.expresion()
        # Consumir 'entonces'
        self.consumir(TipoToken.PALABRA_CLAVE)
        # Cuerpo verdadero
        verdadero = []
        while self.actual() and not (self.actual().Tipo == TipoToken.PALABRA_CLAVE and self.actual().Valor == "fin"):
            verdadero.append(self.declaracion())
        # Consumir 'fin'
        self.consumir(TipoToken.PALABRA_CLAVE)
        # Crear el AST de la expresión if
        return ast.IfAST(condicion, verdadero)
    
    def whileexpresion(self):
        self.consumir(TipoToken.PALABRA_CLAVE)
        condicion = self.expresion()
        # Consumir 'entonces'
        self.consumir(TipoToken.PALABRA_CLAVE)
        # Cuerpo del bucle
        cuerpo = []
        while self.actual() and not (self.actual().Tipo == TipoToken.PALABRA_CLAVE and self.actual().Valor == "fin"):
            cuerpo.append(self.declaracion())
        # Consumir 'fin'
        self.consumir(TipoToken.PALABRA_CLAVE)
        # Crear el AST del bucle while
        return ast.WhileAST(condicion, cuerpo)

    def llamada_funcion(self, nombre):
        self.consumir(TipoToken.ABRIR_PARENTESIS)
        argumentos = []
        if self.actual().Tipo != TipoToken.CERRAR_PARENTESIS:
            while True:
                argumentos.append(self.expresion())
                if self.actual().Tipo == TipoToken.COMA:
                    self.consumir(TipoToken.COMA)
                else:
                    break
        self.consumir(TipoToken.CERRAR_PARENTESIS)
        return ast.LlamadaFuncionAST(nombre, argumentos)