class Person:

    num_of_adults_in_America = 0
    num_of_adults_in_Ukraine = 0

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return f'{self.name}, {self.age}, {self.country}'

    @classmethod
    def adult(cls, name, age, country):
        if country == "USA" and age >= 18:
            cls.num_of_adults_in_America += 1

        if country == "Ukraine" and age >= 18:
            cls.num_of_adults_in_Ukraine += 1

        return cls(name, age, country)


person1 = Person.adult("Marie", 15, "Ukraine")
person2 = Person.adult("Alex", 20, "USA")
person3 = Person.adult("Ann", 18, "USA")
person4 = Person.adult("John", 23, "Ukraine")
person5 = Person.adult("Max", 50, "Ukraine")
person6 = Person.adult("Oleh", 21, "France")

print(Person.num_of_adults_in_Ukraine)
print(Person.num_of_adults_in_America)
