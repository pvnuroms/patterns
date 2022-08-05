from abc import ABC
from enum import Enum, auto

class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print(f'your {self.__class__.__name__}, please')


class Coffee(HotDrink):
    def consume(self):
        print(f'your {self.__class__.__name__}, please')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea\nboil_water\nyour {amount}ml of tea')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans\nboil_water\nyour {amount}ml of coffee')
        return Coffee()


def make_drink(drink_type: str, def_amount = 200):
    if drink_type == 'tea':
        return TeaFactory().prepare(def_amount)
    if drink_type == 'coffee':
        return CoffeeFactory().prepare(def_amount)


class HotDrinkMachine:
    class AvailiableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailiableDrink:
                print(d)
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Avialable drinks:')
        print([fac[0] for fac in self.factories])
        user_drink = int(input(f'choose drink (0-{len(self.factories)-1}): '))
        amount = int(input('skolko???'))
        print(user_drink, amount, self.factories)
        return eval(self.factories[user_drink][1].prepare(amount))

if __name__ == '__main__':

    # drink_type = 'coffee'
    # drink = make_drink(drink_type)
    # drink.consume()
    # drink_type = 'tea'
    # drink = make_drink(drink_type)
    # drink.consume()


    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()

    # tea = Tea()
    # tea.consume()