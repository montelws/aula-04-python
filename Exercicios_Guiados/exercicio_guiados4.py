texto = input ("Numeros separados por espaco:")
palavras = texto.split() 
#set () elimina os repetidos
unicos = set (palavras)
print ("Digitadas:", len (palavras))
print ("Unicas:", len (unicos))
print (sorted(unicos))