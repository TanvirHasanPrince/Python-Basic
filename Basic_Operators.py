number = 1 + 2 * 3 / 4.0
print(number)


remainder = 11 % 3
print(remainder)


squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)


helloworld = "hello" + " " + "world"
print(helloworld)



# Python also supports multiplying strings to form a string with a repeating sequence:
lotsofhellos = "hello" * 10
print(lotsofhellos)


# Lists can be joined with the addition operators:
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)


# Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:
print([1,2,3] * 3)


# The target of this exercise is to create two lists called x_list and y_list,
# which contain 10 instances of the variables x and y, respectively.
# You are also required to create a list called big_list,
# which contains the variables x and y, 10 times each,
# by concatenating the two lists you have created.

# TODO: change this code
x = 'x'  # Define x and y variables
y = 'y'

x_list = [x] * 10  # Create x_list with 10 instances of x
y_list = [y] * 10  # Create y_list with 10 instances of y
big_list = x_list + y_list  # Concatenate x_list and y_list to create big_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# Testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:  # Fix missing condition
    print("Great! All lists contain the correct number of items.")

