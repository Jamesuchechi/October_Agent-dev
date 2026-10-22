class Character:
    def __init__(self, name, health, attack_power):
        self.name = name                  
        self.health = health              
        self.attack_power = attack_power  

    def attack(self, target):
        print(f"{self.name} swings at {target.name} for {self.attack_power} damage!")
        target.health -= self.attack_power
        print(f"{target.name} has {target.health} HP left.\n")

hero = Character("Jin", 100, 25)
goblin = Character("Goblin", 60, 10)

hero.attack(goblin)   
goblin.attack(hero)   