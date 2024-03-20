class SuperClass1:
    def info(self):
        print("I am a SuperClass1")


class SuperClass2:
    def info(self):
        print("I am a SuperClass2")


class Descendant(SuperClass1, SuperClass2):
    pass


d1 = SuperClass1()
d1.info()

d2 = SuperClass2()
d2.info()

d3 = Descendant()
d3.info()
print(Descendant.mro())
