def vogal (letra):
  vogais = "aeiou"
  letraMinuscula = letra.lower()
  if vogais.find(letraMinuscula) > 0:
    return True
  return False