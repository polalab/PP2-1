# exercise 1 - create two variables a, b of type int and add them together
a=7
b=16
print(a+b)
# exercise 2 - take an input "c" from the user and print multiplication of a times c
c = input("give a number")
multiplication = int(a)* int(c)
print(multiplication)
#i had to google this cause what the actual fuck is an input

# excersise 3 - types - print type of every variable (type checking)

a_int = 5
b_bool = True
c_string = "Hello,Katrina"
d_float = 0.001

print(type(a_int))
print(type(b_bool))
print(type(c_string))
print(type(d_float))

# excercise 4 - make an algorithm that will print c_string a_int times
repetition= c_string * a_int
print(repetition)

# excercise 5 - make a function that will take a parameter 'num' of type int and return a string consisting of num times
# 'hello' e.g. for num = 3 it will return 'hello hello hello'

def thisishard(int_num):
    return "pola " * int_num
print(thisishard(8))

# excercise 6 - amend commit so that the function in excercise 5 takes two parameters - num and name and returns a string
# consisting of num times 'hello' followed by a ', name'

p = 5 

def thisishard(int_num, name):
    return ("hello " + name) * int_num
print(thisishard(5, "katrina, "))


# *** If times allows: random library
