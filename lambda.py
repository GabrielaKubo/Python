# Métodos com map 
def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print(item)

lista = list(map(square, my_nums))
print(lista)

def splicer(mystring):
    if len(mystring)%2 == 0:
        return "EVEN"
    else:
        return mystring[0]
    
names = ["Andy", "Eve", 'Sally']
lista_igual = list(map(splicer, names))
print(lista_igual)

def check_even(num):
    return num % 2 == 0
my_nums = [1,2,3,4,5,6]

# Métodos com filter 
filtro = list(filter(check_even, my_nums))
print(filtro)

for n in filter(check_even, my_nums):
    print(n)

# Métodos com lambda
def square(num):
    result = num**2
    return result

square = lambda num: num ** 2

quadrado = square(5)
print(quadrado)

a1 = list(map(lambda num: num**2, my_nums))
print (a1)

a2 = list(filter(lambda num: num%2 == 0, my_nums))
print(a2)