from random import choice, randint
from .listas import personagens, erros_tupla, erros_complex, erros_none, erros_byte, erros_frozenset

def shrekizar(valor):
    if isinstance(valor, (int, str, bool, float)) == True:
        valor = choice(personagens)
        return valor
    elif isinstance(valor, list) == True:
        for i in range(len(valor)):
            valor[i] = choice(personagens)
        return valor
    elif isinstance(valor, (bytes, bytearray)) == True:
        print(f'\033[32m {choice(erros_byte)}\033[0m' )
        return ''
    elif isinstance(valor, frozenset) == True:
        print(f'\033[32m {choice(erros_frozenset)}\033[0m' )
        return ''
    elif isinstance(valor, set) == True:
        total = len(valor)
        valor.clear()
        while len(valor) < total:
            valor.add(choice(personagens))
        return valor
    elif valor == None:
        print(f'\033[32m {choice(erros_none)}\033[0m' )
        return ''
    elif isinstance(valor, complex) == True:
        print(f'\033[32m {choice(erros_complex)}\033[0m' )
        return ''
    elif isinstance(valor, dict) == True:
        for chave in valor.keys():
            valor[chave] = choice(personagens)
        return valor
    elif isinstance(valor, tuple) == True:
        print(f'\033[32m {choice(erros_tupla)} \033[0m')
        return ''
