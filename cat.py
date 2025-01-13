#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
tiger = Cat('Tiger', 2)
lion = Cat('Lion', 1)
lynx = Cat('Lynx', 3)

# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    max_age = 0
    for i in args:
        if i.age > max_age:
            max_age = i.age
    return max_age


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest_cat=oldest_cat(tiger, lion, lynx)
print(f'The oldest cat is {oldest_cat} years old.')