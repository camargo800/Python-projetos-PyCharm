#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians,sin,cos,tan
ang=float(input('digite um ângulo qualquer: '))
print('o seno de {} é igual a {:.2f}'.format(ang,sin(radians(ang))))
print('o cosseno de {} é igual a {:.2f}'.format(ang,cos(radians(ang))))
print('e a tangente de {} é igual a {:.2f}'.format(ang,tan(radians(ang))))


