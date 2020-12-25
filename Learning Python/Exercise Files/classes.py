class myClass():
    def method1(self):
        print('My class method')

    def method2(self, someString):
        print("My favorite clas "+ someString)


class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print('anotherclass method')

    def method2(self, someString):
        print("Another class Metnod2")

    
def main():
    c = myClass()
    c.method1()
    c.method2("Math ")

    c2= anotherClass()
    c2.method1()
    c2.method2("This is a string")


if __name__ == "__main__":
    main()