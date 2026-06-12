# Definimos el rol inicial
rol = "201012341"

# 1. Asegurarnos de que el rol sea texto para poder leer letra por letra
rol_texto = str(rol)

# 2. Invertir el número
rol_invertido = ""
for numero in rol_texto:
    # Agregamos cada número al principio para que quede al revés
    rol_invertido = numero + rol_invertido 

# 3. Multiplicar los dígitos por la secuencia 2, 3, 4, 5, 6, 7
suma = 0
multiplicador = 2

for numero in rol_invertido:
    # Multiplicamos el número actual y lo sumamos al total
    suma = suma + (int(numero) * multiplicador)
    
    # Aumentamos el multiplicador para el siguiente número
    multiplicador = multiplicador + 1
    
    # Si el multiplicador llega a 8, lo regresamos a 2
    if multiplicador == 8:
        multiplicador = 2

# 4. Al resultado obtenido debemos sacarle el módulo 11
modulo = suma % 11

# 5. Con el resultado obtenido, debemos restarlo de 11
resultado_resta = 11 - modulo

# Revisar los casos especiales de la resta
if resultado_resta == 11:
    digito_verificador = "0"
elif resultado_resta == 10:
    digito_verificador = "K"
else:
    digito_verificador = str(resultado_resta)
    
# 6. Finalmente, el dígito verificador será el obtenido unido al rol
rol_completo = rol_texto + "-" + digito_verificador

print("El rol con dígito verificador es:")
print(rol_completo)

