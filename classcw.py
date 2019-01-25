class Dog:

    def __init__(self, name, breed, color, gender):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender

    def printAll(self):
        print(self.name, self.breed, self.color, self.gender)

class Person:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def changeWeight(self, pounds):
        self.weight += pounds
    def changeHeight(self,inches):
        self.height += inches
    def bmI(self):
        return ({self.weight / (self.height * self.height) * 703})

class Product:
    def __init__(self, name="", price=0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return(f"The product {self.name} is {self.price} dollars and you want {self.quantity} orders")


def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()



def problem1():
    zeusDog = Dog("Zeus", "Akita", "black", "female")
    zeusDog.printAll()


    # Create a class Dog.
    # Make sure it has the attributes name, breed, color, gender.
    # Create a function that will print all attributes of the class.
    # Create an object of Dog in your problem1 function and print all of it's attributes.

def problem2():
    uI=""
    while uI != "=":
        uI=input("Enter something about yourself, or '=' to quit\n")

# Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.

def problem3():
    melaati = Person("Melaati", 170, 61)
    itayana = Person("Itayana", 180, 65)
    kareem = Person("Kareem", 200, 70)

    kareem.changeHeight(21)
    kareem.changeWeight(21)
    melaati.changeHeight(2)
    melaati.changeWeight(23)
    itayana.changeHeight(8)
    itayana.changeWeight(2)

    print(kareem.bmI())
    print(itayana.bmI())
    print(melaati.bmI())


#     In your main file create three Person objects.
#     Change the weight and height of each one.
#     Afterwards, print the BMI (body mass index) of each Person.
#     If you don’t know how to calculate BMI, look at the code I provided for you.
#
# <strong>Hint</strong>: BMI is (weight / (height * height)) x 703. Weight is in pounds and height is in inches.
#
# <strong>Extra</strong>:Put the three person objects in an array and use a loop to print out their BMIs.

def problem4():
    product1 = Product()
    product2 = Product(name ="sensodine")
    product3 = Product(name = "white strips", price=4)
    product4 = Product(name="colgate", price=3, quantity=2)
    print(product1)
    print(product2)
    print(product3)
    print(product4)




#     Create a class Product that represents a product sold online. A product has a name, price, and quantity.
#
# The class should have changeProduct:
#
# a) If changeProduct has one parameter, it can change the name of the product.
#
#     b) If changeProduct has two parameters it can change the name and price of the product.
#
#     c) If changeProduct has three parameters it can change the name, price, and quantity of the product.
#
#     Create an object of Product in your problem4 function and print all of it's attributes.
# 4():

if __name__ == '__main__':
    main()