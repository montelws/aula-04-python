# declaração do conjunto ( chaves )
frutas = {"maca", "uva", "maca"}
#duplicadas são eliminadas
print (frutas) # {'maca', 'uva'}
# percorrendo o conjunto 
for f in frutas :
    print (f) 


#Exemplo pratico: professor quer saber quais alunos entregaram o trabalho (sem duplicatas)

#lista de entregas com nomes repetidos
entregas = ["Ana", "João", "Ana", "Pedro"]
# set () elimina as duplicatas
conjunto = set (entregas)
# imprime apenas os alunos unicos 
print (conjunto)

