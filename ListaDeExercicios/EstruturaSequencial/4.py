#coding: utf-8
#Faça um Programa que peça as 4 notas bimestrais e mostre a média. 

n1 = int(raw_input("Digite a nota N1: "))
n2 = int(raw_input("Digite a nota N2: "))
n3 = int(raw_input("Digite a nota N3: "))
n4 = int(raw_input("Digite a nota N4: "))

media = (n1 + n2 + n3 + n4) / 4

print "média das notas é: %d" % (media)
