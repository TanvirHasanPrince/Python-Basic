# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)



# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)

# Exercise
# You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."

print(format_string % data)

# data = ("John", "Doe", 53.44): This line creates a tuple named data containing three elements: "John", "Doe", and 53.44. This tuple represents information about a person, including their first name, last name, and current balance.

# format_string = "Hello %s %s. Your current balance is $%.2f.": Here, format_string is assigned a string value. This string contains placeholders marked by %s and %f for string and float formatting, respectively. Let's break down the placeholders:

# %s: This is a placeholder for a string value. It will be replaced by the first and second elements of the data tuple, which are the first name and last name, respectively.

# %f: This is a placeholder for a floating-point number. It will be replaced by the third element of the data tuple, which is the balance. The .2 in %.2f specifies that the floating-point number should be formatted to two decimal places.

# The whole format string is "Hello %s %s. Your current balance is $%.2f." It combines static text with placeholders for dynamic values.

# print(format_string % data): This line uses the % operator for string formatting. It takes the format_string and applies the formatting specified by the placeholders to the data tuple. The % data part injects the values from the data tuple into the placeholders in the format_string. Then, it prints the formatted string.