def add(*args):
    #we can also access its indexes as it is in form of a tuple
    print(args[1])
    sum=0
    for i in args:
        sum+=i
    print(sum)

add(1,90,8,9,7,5)

#unlimited keyword arguments

def calculate(n,**kwargs):
    #kwargs will be in the form of a dictionary
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)

calculate(2,add=3,multiply=5)

#we can create a class of our own
# class Car:
#     def __init__(self,**kwargs):
#         self.make = kwargs["make"]
#         self.model = kwargs["model"]
#
# car = Car(make="nissan",model="gtr")
# print(car.model)

#if we dont provide a parameter then it will throw an error
class Car:
    def __init__(self,**kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")

car = Car(make="nissan")
print(car.model)

#so here we can also use get method to access values from dictionary but the benefir is instead of error it will give none if there is no parameter