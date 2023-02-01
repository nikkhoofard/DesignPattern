from abstractfactory import Rugs

print('help')
class PriceAdapter:
    def __init__(self, rate):
        self.rate = rate

    def exchange(self, product):
        return self.rate * product._price


if __name__ == "__main__":
    r1 = Rugs('Persian rugs', 20)
    r2 = Rugs('Nain rugs', 23)
    r3 = Rugs('Morrocco rugs', 19)

    adapter = PriceAdapter(rate=28000)

    rugs = [r1, r2, r3]

    for rug in rugs:
        print(f"{rug._name}: {adapter.exchange(rug)}")
