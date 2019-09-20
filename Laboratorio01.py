# Apertura y lectura del archivo
archivo = open('insertionsort.txt', 'r')
lineas = archivo.readlines()
tam = len(lineas)
archivo.close()

# Implementación de insertionsort
for i in range(1, tam):
	num = lineas[i]
	j = i - 1
	while(j >= 0 and (lineas[j] > num or len(lineas[j]) > len(num)) and len(lineas[j]) >= len(num)):
		lineas[j+1] = lineas[j]
		j = j - 1
	lineas[j+1] = num
# Reescritura del archivo
archivo = open('insertionsort.txt', 'w')
archivo.writelines(lineas)
archivo.close()
