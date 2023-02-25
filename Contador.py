#Jonathan Felix | Akhenaton 
#Código para exercício da faculdade

numero = int(input('Digite o valor: '))

cem = int(numero / 100)
numero = numero - (cem*100)
    
cinquenta = int(numero/50)
numero = numero - (cinquenta*50)

dez = int(numero/10)
numero = numero - (dez*10)

cinco = int(numero/5)
numero = numero - (cinco*5)

um = numero
    
print(f"R$  100,00 = {cem}.")
print(f"R$  50,00 = {cinquenta}.")
print(f"R$  10,00 = {dez}.")
print(f"R$  5,00 = {cinco}.")
print(f"R$  1,00 = {um}.")