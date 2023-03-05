#Jonathan Felix | Akhenaton 
#Código para exercício da faculdade

numero = float(input('Digite o valor: \n'))

duzento = int(numero / 200) #200,00
numero = numero - (duzento * 200)

cem = int(numero / 100) #100,00
numero = numero - (cem*100)
    
cinquenta = int(numero/50) #50,00
numero = numero - (cinquenta*50)

dez = int(numero/10) #10,00
numero = numero - (dez*10)

cinco = int(numero/5) #5,00
numero = numero - (cinco*5)

dois = int(numero / 2) #2,00
numero = numero - (dois * 2)

um = int(numero/1) #1,00
numero = numero - (um*1)

cinquentacc = int(numero/0.5) #0,50
numero = numero - (cinquentacc * 0.5)

vintecincocc = int(numero / 0.25) #0,25
numero = numero - (vintecincocc * 0.25)

dezcc = int(numero / 0.10) #0,10
numero = numero - (dezcc * 0.10)

cincocc = int(numero / 0.05) #0,05
numero = numero - (cincocc * 0.05)


print("O resultado em de cédulas é:\n ")
print(f"R$  200,00 = {duzento}.")
print(f"R$  100,00 = {cem}.")
print(f"R$  50,00 = {cinquenta}.")
print(f"R$  10,00 = {dez}.")
print(f"R$  5,00 = {cinco}.")
print(f"R$  2,00 = {dois}.")
print(f"R$  1,00 = {um}.")
print(f"R$  0,50 = {cinquentacc}.")
print(f"R$  0,25 = {vintecincocc}.")
print(f"R$  0,10 = {dezcc}.")
print(f"R$  0,05 = {cincocc}.")
