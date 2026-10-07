class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        if self.health > 0:
            print(f"{self.name} attacks -> {self.damage} damage")
            zombie.take_damage(self.damage)
        else:
            print(f"{self.name} is unable to attack.")

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)


class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
        if self.distance > 0:
            self.distance -= 1
            print(f"zombie moves closer, distance: {self.distance}")

    def attack(self, plant):
        print(f"Zombie attack, dealt {self.damage} damage")
        plant.take_damage(self.damage)

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)


def show(p1, p2, z):
    print("-" * 45)
    print(f"{p1.name}: {p1.health} HP  |  {p2.name}: {p2.health} HP")
    print(f"Zombie: {z.health} HP  |  Distance: {z.distance}")
    print("-" * 45)


def game_over(p1, p2, z):
    if z.health <= 0:
        print("plant win")
        return True
    if p1.health <= 0 and p2.health <= 0:
        print("zombie win")
        return True
    return False


PeaShooter = Plant("peashooter", 90, 10)
Repeater = Plant("repeater", 80, 15)
zombie = Zombie("zombie", 150, 30, 0)

print("Plants VS Zombies")

while True:
    if PeaShooter.health > 0:
        PeaShooter.attack(zombie)
        show(PeaShooter, Repeater, zombie)
        if game_over(PeaShooter, Repeater, zombie):
            break

    if Repeater.health > 0:
        Repeater.attack(zombie)
        show(PeaShooter, Repeater, zombie)
        if game_over(PeaShooter, Repeater, zombie):
            break

    if zombie.distance > 0:
        zombie.move()
    else:
        if PeaShooter.health > 0:
            zombie.attack(PeaShooter)
        elif Repeater.health > 0:
            zombie.attack(Repeater)

    show(PeaShooter, Repeater, zombie)
    if game_over(PeaShooter, Repeater, zombie):
        break
