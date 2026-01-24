from random import choice, randint
from .listas import personagens, erros_tupla, erros_complex, erros_none

def shrekizar(valor):
    if isinstance(valor, (int, str, bool, float)) == True:
        valor = choice(personagens)
        return valor
    elif isinstance(valor, list) == True:
        for i in range(len(valor)):
            valor[i] = choice(personagens)
        return valor
    elif valor == None:
        print(f'\033[32m {erros_none[randint(0, len(erros_none) - 1)]}\033[0m' )
        return ''
    elif isinstance(valor, complex) == True:
        print(f'\033[32m {erros_complex[randint(0, len(erros_complex) - 1)]}\033[0m' )
        return ''
    elif isinstance(valor, dict) == True:
        for chave in valor.keys():
            valor[chave] = choice(personagens)
        return valor
    elif isinstance(valor, tuple) == True:
        print(f'\033[32m {erros_tupla[randint(0, len(erros_tupla) - 1)]} \033[0m')
        return ''

