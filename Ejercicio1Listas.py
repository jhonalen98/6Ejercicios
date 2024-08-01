lista = [4, 2, 9, 1, 5, 6]
print("Lista sin modificar:", lista)

lista.append(10)
print("1 Después de agregar un numero:", lista)

lista.pop(0)
print("2 Se elimina el primer elemento", lista)

lista.sort()
print("3 Después de ordenar:", lista)

lista.reverse()
print("4 Lista invertida:", lista)

print("5 Lista final:", lista)