archivo=open("prueba.txt","w")
archivo.write("Hola.\nBienvenido al curso de Python.\nEsperamos que sea una agradable experiencia.")

print(archivo.tell())
print(type(archivo))
archivo.close()
