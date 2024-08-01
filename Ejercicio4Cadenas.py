Cadena = input("Ingresa la cadena de texto: ")

LetraCambiar = "o"
CambiarPor = "0"

cadena_minusculas = Cadena.lower()
print("1 Cadena en minúsculas:", cadena_minusculas)

cadena_reemplazada = cadena_minusculas.replace(LetraCambiar, CambiarPor)
print("2 Cadena con reemplazos:", cadena_reemplazada)

lista_palabras = cadena_reemplazada.split()
print("3 Lista de palabras:", lista_palabras)

