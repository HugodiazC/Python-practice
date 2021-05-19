archivo=open("C:/Users/Vallarta/Documents/Ejemplo_escribir_archivo/prueba1.txt","w")
archivo.write("Hola.\nBienvenido al curso de Python.\nEsperamos que sea una agradable experiencia.")

print(archivo.tell())
print(type(archivo))
archivo.close()
