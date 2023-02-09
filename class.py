class planet:

    def __init__(self):
        self.name = 'hoth'
        self.radius = 200000
        self.gravity = 5.5
        self.system = 'hoth system'

    def orbit(self):
        return f'{self.name} is orbiting the {self.system}'

hoth = planet()
print(f'name is :{hoth.name}')
print(f'radius is:{hoth.radius}')
print(f'the gravity is:{hoth.gravity}')
print(hoth.orbit())