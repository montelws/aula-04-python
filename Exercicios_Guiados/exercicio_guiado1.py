numeros = [] # lista vazia 
qtd = int (input("Quantos numeros?"))
for i in range (qtd) :
    n = int (input("Digite um numero :"))
    numeros.append(n)   #insere no fim 
print ("Lista:", numeros)
print ("Tamanho:", len (numeros))