#ordena aléatoriamente e não aceita repetição.
set1 = {'michael','michael', 1, 1, 2.0}

# mostrando o tipo com método type().
print(type(set1))
print(set1)


#convertendo em conjunto.
set2 = set(['inifity', 'school', '202'])
print(set2)

#adicionando (add), no conjunto. 
set2.add('computador')
print(set2)

#adicionando outro conjunto, método - update().
set2.update(set1)
print(set2) 


#verificnado se o dado se encontra dentro do conjunto, retorna um boolean.
set3 = {'carro', 'moto', 'gato'}
print('moto' in set3)
print('aviao' in set3)

#percorrendo um conjunto usando laço de repetição (for).
for i in set3:
    print(i)

#apagando um dado do conjunto, metodos = .discar() ou .remove().
set4 = {'joão', 'marcos', 'daniel'}
print(set4)
set4.discard('joão')
set4.remove('marcos')
print(set4)

#mostrando a intercesão entre conjuntos, metodo = .intersection()
pessoas1 = {'ana', 'bia', 'carlo'}
pessoas2 = {'joana', 'bia', 'max'}

print(pessoas1.intersection(pessoas2))

#union(). para retornar um conjunto de elementos de outro conjuntos.
pessoas1 = {'ana', 'bia', 'carlo'}
pessoas2 = {'joana', 'bia', 'max'}

print(pessoas1.union(pessoas2))

