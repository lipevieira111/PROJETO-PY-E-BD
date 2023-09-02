numero = int(input("digite um numero:"))
par=[]
impar=[]
for i in range(1,numero+1):
    if i %2 ==0:
          par.append(i)
    else:
         impar.append(i)
print(par)
print(impar)