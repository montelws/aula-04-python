#arquivo : principal.py
from Conteudo_Silde.adicionar import adicionar
from Conteudo_Silde.remover import remover
from Conteudo_Silde.atualizar import atualizar
from Conteudo_Silde.iterar import iterar 
from Conteudo_Silde.pertencimento import existe 
estoque = ["mouse", "mose", "hd"]
adicionar (estoque, "teclado")
atualizar (estoque, "mose", "mouse2")
remover (estoque, "hd")
if existe (estoque, "teclado"):
    iterar (estoque)    #relatorio final
