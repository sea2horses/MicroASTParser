def pretty_attr(attr, nivel, nombre=None):
    indent = "    " * nivel
    if hasattr(attr, "to_pretty_str"):
        s = attr.to_pretty_str(nivel + 1)
        if nombre:
            s = f"{indent}{nombre}:\n{s}"
        return s
    elif isinstance(attr, list):
        if not attr:
            return f"{indent}{nombre}: []" if nombre else f"{indent}[]"
        s = f"{indent}{nombre}:\n" if nombre else ""

        for a in attr:
            s += pretty_attr(a, nivel) + "\n"
        return s.rstrip()
    else:
        if attr is None:
            return ""
        if nombre:
            return f"{indent}{nombre}: {attr}"
        return f"{indent}{attr}"

class NodoAST:
    def to_pretty_str(self, nivel=0):
        indent = "    " * nivel
        return f"{indent}Nodo Desconocido"

class DeclaracionAST(NodoAST):
    def __init__(self, tipo, identificador, valor=None):
        self.Tipo = tipo
        self.Id = identificador
        self.Valor = valor

    def to_pretty_str(self, nivel=0):
        indent = "    " * nivel
        s = f"{indent}DeclaracionAST:\n"
        s += pretty_attr(self.Tipo, nivel + 1, "Tipo") + "\n"
        s += pretty_attr(self.Id, nivel + 1, "Id")
        if self.Valor is not None:
            s += "\n" + pretty_attr(self.Valor, nivel + 1, "Valor")
        return s

class NumeroAST(NodoAST):
    def __init__(self, valor):
        self.Valor = valor

    def to_pretty_str(self, nivel=0):
        indent = "    " * nivel
        return f"{indent}NumeroAST: {self.Valor}"

class StringAST(NodoAST):
    def __init__(self, valor):
        self.Valor = valor

    def to_pretty_str(self, nivel=0):
        indent = "    " * nivel
        return f"{indent}StringAST: \"{self.Valor}\""

class BooleanAST(NodoAST):
    def __init__(self, valor):
        self.Valor = valor

    def to_pretty_str(self, nivel=0):
        indent = "    " * nivel
        return f"{indent}BooleanAST: {self.Valor}"

class VariableAST(NodoAST):
    def __init__(self, identificador):
        self.Id = identificador

    def to_pretty_str(self, nivel=0):
        indent = "    " * nivel
        return f"{indent}VariableAST: {self.Id}"

class ExpresionBinariaAST(NodoAST):
    def __init__(self, izquierda, operador, derecha):
        self.Izquierda = izquierda
        self.Op = operador
        self.Derecha = derecha

    def to_pretty_str(self, nivel=0):
        indent = "    " * nivel
        s = f"{indent}ExpresionBinariaAST:\n"
        s += pretty_attr(self.Izquierda, nivel + 1, "Izquierda") + "\n"
        s += pretty_attr(self.Op, nivel + 1, "Op") + "\n"
        s += pretty_attr(self.Derecha, nivel + 1, "Derecha")
        return s

class LlamadaFuncionAST(NodoAST):
    def __init__(self, nombre, argumentos):
        self.Nombre = nombre
        self.Argumentos = argumentos

    def to_pretty_str(self, nivel=0):
        indent = "    " * nivel
        s = f"{indent}LlamadaFuncionAST:\n"
        s += pretty_attr(self.Nombre, nivel + 1, "Nombre") + "\n"
        s += pretty_attr(self.Argumentos, nivel + 1, "Argumentos")
        return s

class AsignacionAST(NodoAST):
    def __init__(self, variable, valor):
        self.Variable = variable
        self.Valor = valor

    def to_pretty_str(self, nivel=0):
        indent = "    " * nivel
        s = f"{indent}AsignacionAST:\n"
        s += pretty_attr(self.Variable, nivel + 1, "Variable") + "\n"
        s += pretty_attr(self.Valor, nivel + 1, "Valor")
        return s

class IfAST(NodoAST):
    def __init__(self, condicion, cuerpo, sino=None):
        self.Condicion = condicion
        self.Cuerpo = cuerpo
        self.Sino = sino

    def to_pretty_str(self, nivel=0):
        indent = "    " * nivel
        s = f"{indent}IfAST:\n"
        s += pretty_attr(self.Condicion, nivel + 1, "Condicion") + "\n"
        s += pretty_attr(self.Cuerpo, nivel + 1, "Cuerpo")
        if self.Sino is not None:
            s += "\n" + pretty_attr(self.Sino, nivel + 1, "Sino")
        return s

class WhileAST(NodoAST):
    def __init__(self, condicion, cuerpo):
        self.Condicion = condicion
        self.Cuerpo = cuerpo

    def to_pretty_str(self, nivel=0):
        indent = "    " * nivel
        s = f"{indent}WhileAST:\n"
        s += pretty_attr(self.Condicion, nivel + 1, "Condicion") + "\n"
        s += pretty_attr(self.Cuerpo, nivel + 1, "Cuerpo")
        return s

class RetornoAST(NodoAST):
    def __init__(self, valor):
        self.Valor = valor

    def to_pretty_str(self, nivel=0):
        indent = "    " * nivel
        return f"{indent}RetornoAST:\n" + pretty_attr(self.Valor, nivel + 1, "Valor")

class FuncionAST(NodoAST):
    def __init__(self, nombre, parametros, cuerpo):
        self.Nombre = nombre
        self.Parametros = parametros
        self.Cuerpo = cuerpo

    def to_pretty_str(self, nivel=0):
        indent = "    " * nivel
        s = f"{indent}FuncionAST:\n"
        s += pretty_attr(self.Nombre, nivel + 1, "Nombre") + "\n"
        s += pretty_attr(self.Parametros, nivel + 1, "Parametros") + "\n"
        s += pretty_attr(self.Cuerpo, nivel + 1, "Cuerpo")
        return s

class ProgramaAST(NodoAST):
    def __init__(self, declaraciones):
        self.Declaraciones = declaraciones

    def to_pretty_str(self, nivel=0):
        indent = "    " * nivel
        s = f"{indent}ProgramaAST:\n"
        s += pretty_attr(self.Declaraciones, nivel + 1, "Declaraciones")
        return s