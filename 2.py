class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)


class Human:

    def __init__(self, money):
        self.money = money
        self.house = None

    def make_deal(self, house_, price):
        self.money -= price
        self.house = house_

    def buy_house(self, house_, discount):
        if self.money >= house_.final_price(discount):
            self.make_deal(house_, house_.final_price(discount))
        else:
            print("Not enough money")


human = Human(50000)
house = SmallHouse(55000)
human.buy_house(house, 10)
