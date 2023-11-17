from ninjaclass import Ninja

#class pet
class pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=health
        self.energy=energy

#implement the following methods of class pet
    def sleep(self):
        self.energy+=25
        print(self.energy)
    def eat(self):
        self.energy+=25
        self.health+=10
        print(self.energy, self.health)

    def play(self):
        self.health+=5
        print(self.health)

    def stats(self):
        print(self.energy, self.health)


    def noise(self):
        print(f'the sound of {self.name}')
    


cat=pet('kahla','cat','scratch',100,10)
houssem=Ninja('houssem','bahri','kroket','salami',cat)

cat.stats()

houssem.walk()
houssem.bathe()
houssem.feed()

cat.stats()
