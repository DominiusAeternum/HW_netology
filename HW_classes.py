class Animal:
    is_fed = 'not fed'

    def feed(self):
        self.is_fed = 'fed'
        self.weight *= 1.2

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Goose(Animal):     #склоняюсь к тому, что гуси все-таки не несут яиц, поэтмоу у них мы их собирать не будем
    def sound(self):
        print('krya')

class Cow(Animal):
    is_milked = 'not milked'
    def sound(self):
        print('mooo')

    def milk(self):
        self.is_milked = 'milked'
        self.weight -= 5

class Sheep(Animal):
    is_sheared = "not sheared"
    def sound(self):
        print('bee')

    def shear(self):
        self.is_sheared = 'sheared'
        self.weight *= 0.8

class Hen(Animal):
    has_eggs = 'has eggs'
    def sound(self):
        print('kokoko')

    def give_me_eggs(self):
        self.has_eggs = 'has no eggs'
        self.weight -= 0.5

class Goat(Cow):
    def sound(self):
        print('mee')

class Duck(Goose, Hen):
    pass

goose0 = Goose('Seriy', 5.5)
goose1 = Goose('Beliy', 6)
goose0.feed()
goose1.feed()

cow0 = Cow('Manka', 100)
cow0.feed()
cow0.milk()

sheep0 = Sheep('Barashek', 80)
sheep1 = Sheep('Kudryaviy', 75)
sheep0.feed()
sheep1.feed()
sheep0.shear()
sheep1.shear()

hen0 = Hen('Ko-ko', 4)
hen1 = Hen('Kukareku', 4.5)
hen0.feed()
hen1.feed()
hen0.give_me_eggs()
hen1.give_me_eggs()

goat0 = Goat('Roga', 25)
goat1 = Goat('Kopita', 27)
goat0.feed()
goat1.feed()
goat0.milk()
goat1.milk()

duck0 = Duck('Kryakva', 10)
duck0.feed()
duck0.give_me_eggs()

animal_dict = {goose0.name: goose0.weight,
               goose1.name: goose1.weight,
               cow0.name: cow0.weight,
               sheep0.name: sheep0.weight,
               sheep1.name: sheep1.weight,
               hen0.name: hen0.weight,
               hen1.name: hen0.weight,
               goat0.name: goat0.weight,
               goat1.name: goat1.weight,
               duck0.name: duck0.weight
               }
weight_ex = 0
name_ex = 0
weight_sum = 0
for name, weight in animal_dict.items():
    weight_sum += weight
    if weight > weight_ex:
        weight_ex = weight
        name_ex = name
print(f'Самое больше животное это {name_ex}. Оно весит {animal_dict.get(name_ex)} кг!')
print(f'А общий вес животных - {weight_sum}кг!')