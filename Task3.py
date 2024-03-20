class SuperClass1:
    """Parent class 1"""
    def info(self):
        """Print some info about the class"""
        print("I am a SuperClass1")


class SuperClass2:
    """Parent class 2"""
    def info(self):
        """Print some info about the class, override method"""
        print("I am a SuperClass2")


class Descendant(SuperClass1, SuperClass2):
    """Example of multiple inheritance"""
    pass


d1 = SuperClass1()
d1.info()

d2 = SuperClass2()
d2.info()

d3 = Descendant()
d3.info()
print(Descendant.mro())
