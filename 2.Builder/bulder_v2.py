import json


class Person:

    __slots__ = ('name', 'position', 'birthday')

    def __init__(self):
        for attr in self.__slots__:
            self.__setattr__(attr, None)

    def __str__(self):
        return json.dumps({atr: self.__getattribute__(atr) for atr in self.__slots__})

    @staticmethod
    def new(self):
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def set_name(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def set_job(self, position):
        self.person.position = position
        return self


class PersonBirthBuilder(PersonJobBuilder):
    def set_birth(self, birthday):
        self.person.birthday = birthday
        return self


pb = PersonBirthBuilder()
me = pb.set_name('Hrun').set_job('eng').set_birth('11.11.11').build()
print(me)
