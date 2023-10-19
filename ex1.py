def myfunc(a,b,c=0,d=0,e=0):
    return sum((a,b,c,d,e))*0.05

result = myfunc(40,60,50,10,200) 
print(result)

def myfuncArgs(*args):
    return sum(args)*0.05

result_args = myfuncArgs(10,20,30)
print(result_args)

def myfuncArgs2(*args):
    for item in args:
        print(item)

myfuncArgs2(10,20,30,40,210)

def myfunc3(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc3(fruit = 'Apple')

#EXERCICIO 1 - Números pares
print("EXERCÍCIO 1")
def ex1(a,b):
    if a%2==0 and b%2==0:
       return min(a,b)
    else:
        return max(a,b)

resultado = ex1(1,2)
print(resultado)

#EXERCICIO 2 
print("---------------------------------------------------------------------------------------")
print("EXERCÍCIO 2")
def animal(text):
    lista = text.split()
    return lista[0][0] == lista[1][0]

test = animal('Levelheaded Lhama')
print(test)

#EXERCICIO 3 - Total 20 ou se há 20
print("---------------------------------------------------------------------------------------")
print("EXERCÍCIO 3")
def check_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20
    
res1 = check_twenty(20,10)
res2 = check_twenty(10,20)
res3 = check_twenty(18,2)
res4 = check_twenty(40,10)
print(res1)
print(res2)
print(res3)
print(res4)

print("EXERCÍCIO 3 - Segunda Solução")
def check_twenty(n1,n2):
    if n1==20 or n2==20 or (n1+n2)==20:
        return True
    else:
        return False
    
res5 = check_twenty(20,10)
res6 = check_twenty(10,20)
res7 = check_twenty(18,2)
res8 = check_twenty(40,10)
print(res5)
print(res6)
print(res7)
print(res8)

#EXERCICIO 4 - Total 20 ou se há 20
print("---------------------------------------------------------------------------------------")
print("EXERCÍCIO 4 - Retorna a primeira e quarta letra em maiúscula")
def old_macdonald(frase1):
    if len(frase1)>3:
        return frase1[:3].capitalize() + frase1[3:].capitalize()
    else:
        return "Name is too short!"
    

foi = old_macdonald("macdonald")
print(foi)

#EXERCICIO 5
print("---------------------------------------------------------------------------------------")
print("EXERCÍCIO 5 - Retorna a frase invertida")
teste1 = "A frase deve vir inversa"

def inversa(teste):
    return teste[::-1]

foi1 = inversa(teste1)
print(foi1)

#EXERCICIO 6
print("---------------------------------------------------------------------------------------")
print("EXERCÍCIO 6 - Dado um número, retorna True se faltam até 10 números para alcançar o 100 ou 200")

def cem_duzentos_check(num):
    if (abs(100 - num) <= 10)  or  (abs(200 - num) <= 10):
        return True
    else:
        return False

a1 = cem_duzentos_check(90)
a2 = cem_duzentos_check(104)
a3 = cem_duzentos_check(150)
a4 = cem_duzentos_check(209)
print(a1)
print(a2)
print(a3)
print(a4)

#EXERCICIO 7
print("---------------------------------------------------------------------------------------")
print("EXERCÍCIO 7 - Encontre o 33 dado uma lista na qual cada valor deve ser um número inteiro entre 1 a 3")

def achar_tres(lista):
    for num in range(0, len(lista)-1):
        if lista[num] == 3 and lista[num+1] == 3:
            return True
    else:
        return False

listaTeste = [1,3,3]
resultado = achar_tres(listaTeste)
listaTeste1 = [1,3,1,3]
resultado1 = achar_tres(listaTeste1)
listaTeste2 = [3,1,3]
resultado2 = achar_tres(listaTeste2)
print("Resultado da função achar 3")
print(resultado)
print(resultado1)
print(resultado2)

#EXERCICIO 8
print("---------------------------------------------------------------------------------------")
print("EXERCÍCIO 8 - Repete cada letra 3 vezes")
def paper_doll(frase):
    final = ""
    for char in frase:
        final += char*3
    return final
ah = paper_doll("Hello")
print(ah)