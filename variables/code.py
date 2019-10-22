myint = 7

midecimal = 7.0
midecimal = float(7)

#Las cadenas est�n definidas con comillas sencillas o compuestas.

micadena = 'Hola'
micadena = "Hola"
#La diferencia ente las dos es que usando doble comillas lo hace mas facil de incluir los apostofres (de lo contrario concluirira la cadena si se usa doble comillas)

micadena = "No te preocupes de los 'apostofres' usando comillas dobles"
#There are additional variations on defining strings that make it easier to include things such as carriage returns, backslashes and Unicode characters. These are beyond the scope of this tutorial, but are covered in the Python documentation.

#Operadores sencillos pueden ser ejecutados en n�meros o cadenas:

uno = 1
dos = 2
tres = uno + dos

hola = "hola"
mundo = "mundo"
holamundo = hola + " " + mundo
#Se puede asignar a mas de una variable simultaneamente en la misma linea, como se muestra aqu�

a, b = 3, 4
#Mezclando operadores entre los numeros y cadenas que no son soportadas:

# Esto no funcionar�!
print uno + dos + hola
