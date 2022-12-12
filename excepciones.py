

from logging import exception


edad=17

#if edad < 18:
#    raise Exception('eres menor para usar el programa')

print('continuacion')

class AgeException(Exception):
    pass

try:
    'texto' +5
    if edad < 18:
        raise AgeException('eres menor para usar el programa')

except Exception:
    print('se lanzo el error')
