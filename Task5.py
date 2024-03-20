class MyClass:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    @staticmethod
    def adult(age):
        return age >= 18


print(MyClass.adult(15))
print(MyClass.adult(20))

my_class1 = MyClass("Alex", 19, "USA")
my_class2 = MyClass("Marie", 11, "Ukraine")

print(MyClass.adult(my_class1.age))
print(MyClass.adult(my_class2.age))
