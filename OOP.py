class Dog():

    #CLASS OBJECT ATRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    classe = "mamífero"
    # método init será chamado quando a classe for instanciada (construtor)
    def __init__(self, raca, nome, porte):

        self.raca = raca
        self.nome = nome
        self.porte = porte
    #MÉTODOS 
    def latir(self,num):
        print("Woof!{}{}".format(self.nome,num))

meu_pet = Dog(raca="Pastor Alemão", nome="Wendy", porte="Grande")
meu_pet.raca
meu_pet.latir(2 )

class Circle():
    pi = 3.14
    def __init__(self, radius=1) -> None:
        self.radius = radius

    def get_circumference(self):
        return self.radius * self.pi * 2
    
my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())

#HERANÇA

class Animal():
    def __init__(self):
        print("Animal criado")
    def who_am_i(self):
        print("Sou um animal")
    def eat(self):
        print("I am eating")
        
myanimal = Animal()

class Dog2(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog CREATED") 

mydog = Dog2()
mydog.eat()

#POLIMORFISMO

class Dog3():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " Says woof!"
    
class Cat():
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " Says meow!"

niko = Dog3("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

class Animal2():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog4(Animal2):
    def speak(self):
        return self.name + " Says woof!"
    
class Cat4(Animal2):
    def speak(self):
        return self.name + " Says meow!"
    
fido = Dog4("Fido")
luna = Cat("Luna")

fido.speak()
luna.speak()

#Special Methods
