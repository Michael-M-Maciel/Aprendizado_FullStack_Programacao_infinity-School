'''DESAFIO PRÁTICO

Suponha que você está gerenciando uma competição esportiva e tem
uma lista de tuplas representando os resultados das equipes em
diferentes modalidades. Cada tupla contém o nome da equipe, seguido
por uma lista de pontuações obtidas em cada rodada da competição.

1.Calcule a média das pontuações de cada equipe e armazene esses
valores em uma nova lista chamada medias.
2.Ordene a lista medias em ordem decrescente.
3.Crie uma nova lista chamada classificacao que contém tuplas, onde
cada tupla contém o nome da equipe e sua média de pontuações.
4.Exiba na tela a classificação final das equipes, mostrando o nome da
equipe e sua média, da equipe com a pontuação mais alta para a
mais baixa.'''

#criando uma lista de tuplals
resultados = [
    ('flamengo', [3, 2, 6, 10]),
    ('sport', [2, 1, 1, 0]),
    ('vasco,', [0, 0, 1, 1]),
    ('palmeiras', [2, 3, 5, 8])]



#1-lista que vai receber resultado da média
media = []

for  time, pontuacao in resultados:
    media_calculo = sum(pontuacao)/ len(pontuacao)
    media.append(media_calculo)    
    

#2-método "sort()" ordena por base do menor para o maior, (reverse = True) , para mudar a order do maior para o menor
media.sort(reverse=True)
print(f'Média de pontuação das equipes: {media}') # media do maior par o menor



#3-nova lista para receber a tupla com nome do time e média.
classificacao = []
for nome, notas in resultados:
    media_calculada2 = sum(notas) / len(notas) 

    #nova tupla para receber nome, e média
    nova_tupla = (media_calculada2, nome)
    # adicionando nova_tupla em nossa lista classificação
    classificacao.append(nova_tupla)

print(classificacao)

#4-mostrar classificação do maior para o menor usando método sort(reverse = True) para ordenar do maior para o menor
classificacao.sort(reverse=True)
print(classificacao)