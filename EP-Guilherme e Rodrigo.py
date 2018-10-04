# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 09:09:46 2018

@author: guilherme
"""


#abrindo o arquivo
import json
with open ('Arquivo.txt','r') as arquivo:
    a = arquivo.read()
    cardapio = json.loads(a)

with open ('Comanda.txt','r') as arquivo:
    b = arquivo.read()
    listacomandas = json.loads(b)


Progama_Rodando = 1

while Progama_Rodando == 1 :
    
    #HUB do editor do cardápio
    print("\nEscolha:\n")
    print(" 0 - Cardápio\n",
          "1 - Comanda\n",
          "2 - Sair\n",)
    
    decisaoinicial = int(input("Faça sua escolha: "))

    while decisaoinicial != 2:
        
        
        if decisaoinicial == 0 :
            
            #HUB do editor do cardápio
            print("\nMenu do cardápio:\n")
            print(" 0 - Imprimir o cardápio\n",
                  "1 - Adicionar produto ao cardápio\n",
                  "2 - Remover produto do cardápio\n",
                  "3 - Sair do menu do cardápio\n",)
            
            decisaocardapio = int(input("Faça sua escolha: ")) 
            
            if decisaocardapio == 0 :
    
                print('O cardápio possui os seguintes itens:\n')
                for produto in cardapio:
                    print('{0}:'.format(produto), '{0} R$'.format(cardapio[produto]))
                    
                    
                    
            if decisaocardapio == 1 :
                
                produto = input('Digite o nome do produto que deseja adicionar: ')
                produto = produto.lower()
                if produto in cardapio:
                    print('O produto já está no cardápio')
                    break
                else:
                    preco= float(input('Digite o preço do produto:'))
                    cardapio[produto] = preco
                    if preco < 0: 
                        print('O preço não pode ser negativo')
                break
            
            if decisaocardapio == 2 :
                
                produto = input('Digite o nome do produto que deseja remover: ')
                produto = produto.lower()
                if produto not in cardapio:
                    print('O produto não está no cardápio')
                    break
                else:
                    del cardapio[produto]
                break
            
            if decisaocardapio == 3 :
                break
            
        
        if decisaoinicial == 1 :
            
            #HUB da Comanda eletrônica
            nomecomanda = input("Qual o numero da sua comanda?")
            if nomecomanda not in listacomandas:
                diccomanda = nomecomanda
                diccomanda = {}
                listacomandas.append(diccomanda)
                
            numerodacomanda = listacomandas.index(diccomanda)
                
                

            print("\nMenu da comanda\n")
            print(" 0 - Adicionar item à comanda\n",
                  "1 - Remover item da comada\n",
                  "2 - Imprimir comanda\n",
                  "3 - Sair do menu da comanda\n")
                  
            decisaocomanda = int(input("Faça sua escolha: "))   
            
            if decisaocomanda == 0 :
                
                    produto= input("Escreva o nome do produto desejado:")
                    produto = produto.lower()
                    
                    if produto not in cardapio:
                        print('O produto não está no cardápio')
                        break
                    
                    quantidade = int(input('Digite a quantidade do produto: '))
                    if quantidade < 0:
                        print('A quantidade tem de ser positiva e inteira')
                        break
                    
                    
                    listacomandas[numerodacomanda][produto] = quantidade
                    break
                    

            if decisaocomanda == 1 :
                
                    produto= input("Escreva o nome do produto que deseja tirar da comanda:")
                    produto = produto.lower()
                    if produto not in listacomandas[numerodacomanda]:
                        print('O produto não está na comanda')
                        break
                    if produto in listacomandas[numerodacomanda]:
                        quantidade = int(input('Digite quanto do produto deseja remover:'))
                        if quantidade > 0:
                            listacomandas[numerodacomanda][produto] -= quantidade
                            if listacomandas[numerodacomanda][produto] <= 0:
                                del listacomandas[numerodacomanda][produto]
                                print('Produto removido da comanda')
                        if quantidade < 0 :
                            print('Não se pode remover uma quantidade negativa')
                            break

            
            if decisaocomanda == 2:
                
                    total_final= 0
                    total_final10 = 0                    
                    lista_preco_tot=[]
                    for produto in listacomandas[numerodacomanda]:
                        preco_unitario = float(cardapio[produto])
                        quantidade_produto = int(listacomandas[numerodacomanda][produto])
                        preco_tot =  preco_unitario * quantidade_produto
                        lista_preco_tot.append(preco_tot)
                        
                        print('{0}:'.format(produto),"{0}".format(listacomandas[0][produto]))
                        print('Preço Unitário {0} R$'.format(preco_unitario))
                        print('Preço Total {0} R$'.format(preco_tot))
                        total_final += sum(lista_preco_tot,0)
                        total_final10 += 1.1 * total_final
                        continue
                    
                    print('Preço final sem 10%: {0:.2f} R$'.format(total_final))
                    print('Preço final com 10%: {0:.2f} R$'.format(total_final10))
                    break            
            
            if decisaocomanda == 3 :
                break
              
    if decisaoinicial == 2 :
        
        print("até mais!")
        Progama_Rodando = 0   

with open ('Comanda.txt','w') as arquivo:
    Conteudo = json.dumps(listacomandas , sort_keys=True, indent=4)
    arquivo.write(Conteudo)

with open ('Arquivo.txt','w') as arquivo:
    conteudo = json.dumps(cardapio, sort_keys=True, indent=4)
    arquivo.write(conteudo)