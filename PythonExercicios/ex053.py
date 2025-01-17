# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo
# (palavras ou frases lidas de trás para a frente que o resultado é igual, desconsiderando os espaços).
# Ex: arara, kaiak, amor a roma...)
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')

#OUTRA FORMA MAIS SIMPLES SUGERIDA PELO PROFESSOR SEM O 'FOR' E COM FATIAMENTO DE STRING
frase = str(input('Digite uma frase qualquer: ')).strip().upper() #strip tira todos os espaços da frase e upper transforma todas as letras em maiúsculas
palavras = frase.split() #split faz uma 'lista' das palavras, um vetor.
junto = ''.join(palavras) #.join junta o que for colocado entre parênteses, no caso as palavras
inverso = junto[::-1] #[::-1] faz a leitura do começo ao fim porém o -1 faz de tras para frente
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')




