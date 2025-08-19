# Iniciando o tutorial de POO com Python...
print("Iniciando o tutorial de POO com Python... \n")

class Example:
    pass

print("Exibindo a classe Example: " + str(Example) + " \n") # Exibindo a classe Example

# criando instancia da classe
ex = Example()
print("Exibindo a instancia da classe Example: " + str(ex) + " \n") # Exibindo a instancia da classe Example

class Dog:
    # Inicializando atributos da classe Dog
    # __init__ - metodo que sempre é executado quando criamos objeto da classe. É uma funcao de inicializacao
    # self - referencia ao objeto atual. 
    # Toda funcao criada nas classes de Python precisam obrigatoriamente ter o self como primeiro atributo para que possamos acessar os nossos proprios elementos
    def __init__(self, name, age, breed):
        self.name = name # cria atributo name na classe Dog
        self.age = age # cria atributo age na classe Dog
        self.breed = breed # cria atributo breed na classe Dog
        self.is_hungry = True # cria atributo is_hungry na classe Dog, inicializando como True. Todo cachorro começa com fome.
        self.energy = 100 # cria atributo energy na classe Dog, inicializando como 100. Todo cachorro começa com energia total. 

# Metodos Especiais, __init__ , __str__, __len__, __repr__,
    # __str__ - metodo que deve retornar uma representacao em string do objeto
    def __str__(self):
        return "{} é um {} de {} anos.".format(self.name, self.breed, self.age)

    def __len__(self):
        return self.age
    
    def __repr__(self):
        return "Dog(name='{}', age={}, breed='{}')".format(self.name, self.age, self.breed)
    
    def __delattr__(self, name):
        print("Atributo '{}' foi removido.".format(name))
        super().__delattr__(name)

# Outros metodos criados por nos

    def bark(self):
        print("{} diz: Au Au!".format(self.name))

    def eat(self):
        if self.is_hungry:
            print("{} está comendo.".format(self.name))
            self.is_hungry = False
            self.energy += 10
        else:
            print("{} não está com fome.".format(self.name))

    def sleep(self):
        print("{} está dormindo.".format(self.name))
        self.energy = 100

# Herança
# A classe Bulldog herda todos os atributos e métodos da classe Dog
class Bulldog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age, "Bulldog")

dog = Dog("Rex", 5, "Labrador")
print(dog) # Exibindo a representacao em string do objeto dog, prints the __str__ method, Rex é um Labrador de 5 anos.
print("Idade do cachorro:", len(dog), "anos") # Idade do cachorro: 5 anos
print("Representação do cachorro:", repr(dog)) # Representação do cachorro: Dog(name='Rex', age=5, breed='Labrador')
print("String do cachorro:", str(dog)) # String do cachorro: Rex é um Labrador de 5 anos.

print("\n--- Exemplos do uso de 'del' ---")

# 1. Removendo um atributo de instância
dog2 = Dog("Bolt", 3, "Vira-lata")
print("Antes de deletar atributo, repr:", repr(dog2))
print("dog2 tem atributo 'age'?", hasattr(dog2, 'age'))
del dog2.age  # dispara __delattr__ customizado
print("dog2 tem atributo 'age' depois do del?", hasattr(dog2, 'age'))

# Tentando acessar algo que depende de 'age' agora gera erro (len usa age)
try:
    print(len(dog2))
except AttributeError as e:
    print("Erro esperado ao chamar len(dog2) após remover 'age':", e)