from time import sleep
from datetime import date
ano = date.today().year
anonasc = int(input('Qual o ano de nascimento? '))
idade = ano - anonasc
if idade >= 0 and idade <= 9:
    categoria = 'MIRIM'
elif idade >= 10 and idade <= 14:
    categoria = 'INFANTIL'
elif idade >= 15 and idade <= 19:
    categoria = 'JUNIOR'
elif idade >= 20 and idade <=25:
    categoria = 'SÊNIOR'
elif idade > 25:
    categoria = 'MASTER'
print('De acordo com a sua idade sua categoria é:')
sleep(2)
print('{}. Boa sorte!'.format(categoria))

