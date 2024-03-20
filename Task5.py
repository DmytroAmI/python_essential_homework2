class MyClass:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    @staticmethod
    def is_adult(age):
        return age >= 18


print(MyClass.is_adult(15))
print(MyClass.is_adult(20))

my_class1 = MyClass("Alex", 19, "USA")
my_class2 = MyClass("Marie", 11, "Ukraine")

print(MyClass.is_adult(my_class1.age))
print(MyClass.is_adult(my_class2.age))
