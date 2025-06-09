# Primero queremos importar un enumerador para ayudarnos con los tokens
from enum import Enum

# Ahora creamos una clase TokenType o TipoToken que hereda la clase Enum
class TipoToken(Enum):
  NUMERO = 0,
  VARIABLE = 1,
  OPERADOR = 2,
  ABRIR_PARENTESIS = 3,
  CERRAR_PARENTESIS = 4,
  IGUAL = 5,
  PALABRA_CLAVE = 6,
  COMA = 7
  
# Ahora creamos la clase Token
class Token:
  # Constructor
  def __init__(self, tipo: TipoToken, valor):
    self.Tipo = tipo
    self.Valor = valor
  
  def __str__(self):
    return f"Token({self.Tipo}, {self.Valor})"
  
  def __repr__(self):
    return self.__str__()

keywords = [
  "definir",
  "funcion",
  "retornar",
  "si",
  "mientras",
  "como",
  "fin"
]

# Precedencia de los operadores, tambien usado para verificar
# que operadores existen
def precedencia(operador) -> int:
  match operador:
    case '^':
      return 5
    case '*' | '/' | '%':
      return 4
    case '+' | '-' | '–':
      return 3
    case _:
      return -1