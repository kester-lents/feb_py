class Notebook:
    def __init__(self, name, screen, price, resolution='1920/1080'):
        self.name = name
        self.screen = screen
        self.resolution = resolution
        self.price = price

    def sell(self):
        print('!'*70)
        print(self)
        print('!'*70)
        print('sell {}'.format(self.price))


n = Notebook(name='Dell', screen='IPS', price=100)
n1 = Notebook(name='HP', screen='TN-Film', price=200)
print(n)
print(n.name)
print(n.sell())
print(n1)
print(n1.name)
n1.sell()
