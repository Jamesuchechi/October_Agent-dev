from app import Character, goblin

class Warrior(Character):
    def attack(self, target):
        print(f"⚔️ {self.name} slams a heavy greatsword into {target.name}!")

class Archer(Character):
    def attack(self, target):
        print(f"🏹 {self.name} snipes {target.name} from across the map!")

# Look how clean this is: we loop through different classes and call the SAME method
party = [Warrior("Thor", 150, 40), Archer("Legolas", 90, 35)]

for member in party:
    member.attack(goblin)  # Same command, totally different outputs!