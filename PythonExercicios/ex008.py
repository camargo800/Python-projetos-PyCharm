#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n=float(input('digite um número: '))
cm=n*100
mm=n*1000
print('o valor de {} metros equivale a {:.0f}cm e {:.0f}mm'.format(n,cm,mm))

#print('{}km\n{}hm\n{}dam\n{}m\n{}dc\n{}cm\n{}mm'.format((n*0.0001),(n*0.001),(n*0.01),(n*1),(n*10),(n*100),(n*1000))
