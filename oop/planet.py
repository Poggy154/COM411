from human import Human
from robot import Robot

class Planet:

    def __init__(self):
        self.inhabitants = {
            'humans':[],
            'robots':[]
        }
    def __repr__(self):
        return f"planet(humans={self.inhabitants['humans']}, robots={self.inhabitants['robots']})"

    def __str__(self):
        return f"This planet has {len(self.inhabitants['humans'])} humans and {len(self.inhabitants['robots'])}"

    def add_human(self, human):
        self.inhabitants['humans'].append(human)

    def add_robot(self, robot):
        self.inhabitants['robots'].append(robot)

    def remove_human(self, human):
        self.inhabitants['humans'].remove(robot)

if (__name__ =="__main__"):
    planet = Planet()
    print(repr(planet))
    liam = Human("Liam")
    planet.add_human(liam)
    print(repr(planet))
    print(planet)