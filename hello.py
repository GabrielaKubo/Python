#Funções Python
def greet_world(name):
    print("Hello "+ name)

greet_world("Maria")

def greet_world_2(name = 'Default'):
    print(f"Hello {name}")

greet_world_2()
print("---------------------------------------------------------------------------------")

#O return permite adicionar o valor a uma variável
print("O return permite adicionar o valor a uma variável")

def add_num(num1,num2):
    return num1+num2

result = add_num(10,20)

print(result)

def return_result(a,b):
    return a+b

result2 = return_result(10,40)
print(result2)

print("---------------------------------------------------------------------------------")
def sum_numbers(num1,num2):
    return num1+num2

ex1 = sum_numbers(10,20)
ex2 = sum_numbers('10','20')

print(ex1)
print(ex2 + " Tal função concatenou o valor das variáveis strings")
print("---------------------------------------------------------------------------------")
def par(number):
    return number % 2 == 0

a = par(5)
a2 = par(10)
print(a)
print(a2)

def par_lista(lista):
    for number in lista:
        if number % 2 == 0:
            print(f'{number} é Positivo ')
        else:
            print(f'{number} é Negativo ')
            pass
 
par_lista([1,2,3,4,5,6,7,8,9,10])
print("---------------------------------------------------------------------------------")
print("retornando apenas números positivos")
even_numbers = []
def return_postivos(lista):
    for number in lista:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass

return_postivos([1,2,3,4,5,6,7,8,9,10])

print(even_numbers)
