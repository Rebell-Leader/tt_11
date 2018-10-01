class Planet(object):
    count = 0
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
planet = Planet('Earth')
planet = Planet('Mars')
print(planet.count)
