from app import Character, goblin

# Wizard inherits from Character by putting (Character) in parentheses
class Wizard(Character):
    def __init__(self, name, health, attack_power, mana):
        # super() calls the Parent class's __init__ to handle name, health, and attack_power!
        super().__init__(name, health, attack_power)
        self.mana = mana  # Wizard's unique stat

    def cast_fireball(self, target):
        if self.mana >= 20:
            self.mana -= 20
            damage = self.attack_power * 2
            target.health -= damage
            print(f"🔥 {self.name} casts Fireball on {target.name} for {damage} damage!")
        else:
            print(f"{self.name} is out of mana!")

gandalf = Wizard("Gandalf", 80, 30, mana=50)
gandalf.attack(goblin)         # Inherited directly from Character!
gandalf.cast_fireball(goblin)  # Wizard's special move!