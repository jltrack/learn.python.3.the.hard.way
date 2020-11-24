## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a object
class Dog(Animal):

    def __init__(self, name):
        ##self has-a name
        self.name = name

##Cat is-a Animal
class Cat(Animal):

    def __init__(self,name):
        ##self has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ##self has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## self has-a name, has-a salary
        suprt(Employee, self).__init__(name)
        ##self has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

##Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Cat is-a Satan
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet
mary.pet = Satan

## Frank is-a Employee
frank = Employee("Frank", 120000)

# Frank has-a pet
frank.pet = Rover

## Flipper is-a Fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()
