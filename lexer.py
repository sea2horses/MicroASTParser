from lexer_definitions import Token, TipoToken, precedencia
import lexer_definitions as lex_def

def tokenizar(source: str) -> list[Token] | None:
  tokens = []
  posicion = 0

  while posicion < len(source):
    caracter = source[posicion]

    # Ignorar espacios
    if caracter.isspace():
      posicion += 1
      continue

    # Variables (letras)
    if caracter.isalpha():
      string_identificador = ""
      
      while caracter.isalpha() or caracter == '_':
        string_identificador += caracter
        posicion += 1
        caracter = source[posicion] if posicion < len(source) else ''

      # Verificar si es una palabra clave
      if string_identificador in lex_def.keywords:
        tokens.append(Token(TipoToken.PALABRA_CLAVE, string_identificador))
      else:
        tokens.append(Token(TipoToken.VARIABLE, string_identificador))
        
      continue
  

    # Números (incluyendo decimales)
    if caracter.isdigit() or (caracter == '.' and posicion + 1 < len(source) and source[posicion + 1].isdigit()):
      string_numero = ''
      punto_encontrado = False
      while posicion < len(source) and (source[posicion].isdigit() or source[posicion] == '.'):
        if source[posicion] == '.':
          if punto_encontrado:
            break
          punto_encontrado = True
        string_numero += source[posicion]
        posicion += 1
      try:
        tokens.append(Token(TipoToken.NUMERO, float(string_numero)))
      except ValueError:
        print(f"Error, número inválido: '{string_numero}'")
        return None
      continue

    # Comillas para cadenas de texto
    if caracter == '"':
      posicion += 1
      string_cadena = ''
      while posicion < len(source) and source[posicion] != '"':
        if source[posicion] == '\\' and posicion + 1 < len(source):
          # Manejar secuencias de escape
          posicion += 1
          if source[posicion] in ['"', '\\', 'n', 't']:
            string_cadena += source[posicion]
        else:
          string_cadena += source[posicion]
        posicion += 1
      if posicion < len(source) and source[posicion] == '"':
        tokens.append(Token(TipoToken.STRING, string_cadena))
        posicion += 1  # Saltar la comilla final
      else:
        print("Error, cadena de texto no cerrada")
        return None
      
      continue

    # Paréntesis
    if caracter == '(':
      tokens.append(Token(TipoToken.ABRIR_PARENTESIS, caracter))
      posicion += 1
      continue
    elif caracter == ')':
      tokens.append(Token(TipoToken.CERRAR_PARENTESIS, caracter))
      posicion += 1
      continue
    
    # Igual
    if caracter == '=':
      tokens.append(Token(TipoToken.IGUAL, caracter))
      posicion += 1  # Saltar el siguiente caracter
      continue
    
    # Coma
    if caracter == ',':
      tokens.append(Token(TipoToken.COMA, caracter))
      posicion += 1  # Saltar el siguiente caracter
      continue

    # Operadores
    if precedencia(caracter) != -1:
      tokens.append(Token(TipoToken.OPERADOR, caracter))
      posicion += 1
      continue

    # Si llegamos aquí, es un caracter no reconocido
    print(f"Caracter no reconocido: '{caracter}'")
    return None

  return tokens