class Father:
    def father(self):
        print("This is Father class")

class Mother:
    def mother(self):
        print("This is Mother class")

class Child(Father, Mother):
    def child(self):
        print("This is Child class")

c = Child()

c.father()
c.mother()
c.child()

class Grandfather:
    def show1(self):
        print("This is Grandfather class")

class Father1(Grandfather):
    def show2(self):
        print("This is Father class")

class Son(Father1):
    def show3(self):
        print("This is Son class")

s = Son()

s.show1()
s.show2()
s.show3()