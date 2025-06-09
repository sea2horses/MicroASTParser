def pretty_attr(attr, nivel, nombre=None):
    prefix = "-" * nivel
    if hasattr(attr, "to_pretty_str"):
        s = attr.to_pretty_str(nivel)
        if nombre:
            s = f"{prefix}{nombre}: \n" + s
        return s
    elif isinstance(attr, list):
        s = ""
        if nombre:
            s += f"{prefix}{nombre}:"
        for a in attr:
            s += "\n" + pretty_attr(a, nivel + 1)
        return s
    else:
        if nombre:
            return f"{prefix}{nombre}: {attr}"
        return f"{prefix}{attr}"

class NodoAST:
    def to_pretty_str(self, nivel=0):
        return "-" * nivel + str(self)

class DeclaracionAST(NodoAST):
    def __init__(self, tipo, identificador, valor=None):
        self.Tipo = tipo
        self.Id = identificador
        self.Valor = valor

    def to_pretty_str(self, nivel=0):
        s = "-" * nivel + f"DeclaracionAST"
        s += "\n" + pretty_attr(self.Tipo, nivel + 1, "Tipo")
        s += "\n" + pretty_attr(self.Id, nivel + 1, "Id")
        if self.Valor:
            s += "\n" + pretty_attr(self.Valor, nivel + 1, "Valor")
        return s

class NumeroAST(NodoAST):
    def __init__(self, valor):
        self.Valor = valor

    def to_pretty_str(self, nivel=0):
        return "-" * nivel + f"NumeroAST\n" + pretty_attr(self.Valor, nivel + 1, "Valor")

class StringAST(NodoAST):
    def __init__(self, valor):
        self.Valor = valor

    def to_pretty_str(self, nivel=0):
        return "-" * nivel + f"StringAST\n" + pretty_attr(self.Valor, nivel + 1, "Valor")

class BooleanAST(NodoAST):
    def __init__(self, valor):
        self.Valor = valor

    def to_pretty_str(self, nivel=0):
        return "-" * nivel + f"BooleanAST\n" + pretty_attr(self.Valor, nivel + 1, "Valor")

class VariableAST(NodoAST):
    def __init__(self, identificador):
        self.Id = identificador

    def to_pretty_str(self, nivel=0):
        return "-" * nivel + f"VariableAST\n" + pretty_attr(self.Id, nivel + 1, "Id")

class ExpresionBinariaAST(NodoAST):
    def __init__(self, izquierda, operador, derecha):
        self.Izquierda = izquierda
        self.Op = operador
        self.Derecha = derecha

    def to_pretty_str(self, nivel=0):
        s = "-" * nivel + f"ExpresionBinariaAST"
        s += "\n" + pretty_attr(self.Izquierda, nivel + 1, "Izquierda")
        s += "\n" + pretty_attr(self.Op, nivel + 1, "Op")
        s += "\n" + pretty_attr(self.Derecha, nivel + 1, "Derecha")
        return s

class LlamadaFuncionAST(NodoAST):
    def __init__(self, nombre, argumentos):
        self.Nombre = nombre
        self.Argumentos = argumentos

    def to_pretty_str(self, nivel=0):
        s = "-" * nivel + f"LlamadaFuncionAST"
        s += "\n" + pretty_attr(self.Nombre, nivel + 1, "Nombre")
        s += "\n" + pretty_attr(self.Argumentos, nivel + 1, "Argumentos")
        return s

class AsignacionAST(NodoAST):
    def __init__(self, variable, valor):
        self.Variable = variable
        self.Valor = valor

    def to_pretty_str(self, nivel=0):
        s = "-" * nivel + "AsignacionAST"
        s += "\n" + pretty_attr(self.Variable, nivel + 1, "Variable")
        s += "\n" + pretty_attr(self.Valor, nivel + 1, "Valor")
        return s

class IfAST(NodoAST):
    def __init__(self, condicion, cuerpo, sino=None):
        self.Condicion = condicion
        self.Cuerpo = cuerpo
        self.Sino = sino

    def to_pretty_str(self, nivel=0):
        s = "-" * nivel + "IfAST"
        s += "\n" + pretty_attr(self.Condicion, nivel + 1, "Condicion")
        s += "\n" + pretty_attr(self.Cuerpo, nivel + 1, "Cuerpo")
        if self.Sino:
            s += "\n" + pretty_attr(self.Sino, nivel + 1, "Sino")
        return s

class WhileAST(NodoAST):
    def __init__(self, condicion, cuerpo):
        self.Condicion = condicion
        self.Cuerpo = cuerpo

    def to_pretty_str(self, nivel=0):
        s = "-" * nivel + "WhileAST"
        s += "\n" + pretty_attr(self.Condicion, nivel + 1, "Condicion")
        s += "\n" + pretty_attr(self.Cuerpo, nivel + 1, "Cuerpo")
        return s

class RetornoAST(NodoAST):
    def __init__(self, valor):
        self.Valor = valor

    def to_pretty_str(self, nivel=0):
        return "-" * nivel + f"RetornoAST\n" + pretty_attr(self.Valor, nivel + 1, "Valor")

class FuncionAST(NodoAST):
    def __init__(self, nombre, parametros, cuerpo):
        self.Nombre = nombre
        self.Parametros = parametros
        self.Cuerpo = cuerpo

    def to_pretty_str(self, nivel=0):
        s = "-" * nivel + f"FuncionAST"
        s += "\n" + pretty_attr(self.Nombre, nivel + 1, "Nombre")
        s += "\n" + pretty_attr(self.Parametros, nivel + 1, "Parametros")
        s += "\n" + pretty_attr(self.Cuerpo, nivel + 1, "Cuerpo")
        return s

class ProgramaAST(NodoAST):
    def __init__(self, declaraciones):
        self.Declaraciones = declaraciones

    def to_pretty_str(self, nivel=0):
        s = "ProgramaAST"
        s += "\n" + pretty_attr(self.Declaraciones, nivel + 1, "Declaraciones")
        return s