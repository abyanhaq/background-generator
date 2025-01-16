# List comprehensions

my_list = [char for char in 'hello']
my_list2 = [num**2 for num in range(0,100)]
my_list3 = [num for num in my_list2 if num%2 == 0]
print(my_list)
#print(my_list2)
print(my_list3)

# Dict comprehensions

my_dict = {num:num*2 for num in [1,2,3,4,5]}
print(my_dict)