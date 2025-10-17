# Defensa contra ataques modelo
# Ejemplo de numero de combinaciones con clave de solo 4 digitos numericos. 10 x 10 x 10 x 10
# Osea que un atacante tendria que utilizar como maximo 10.000 ataques de fuerza bruta para poder dar con la clave numerica.

from string import digits

for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:
                print(i, j, k, l)


