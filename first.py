#!/bin/python3


#STRINGS
# Print String
print("Hello World!")
print('Hello World!')
print("""This string runs
multiple lines!""") # Triple quote for multi line
print("This string is "+"awesome!") # We can also concatenate
print("\n") # A new line
print("Test that new line out")


print("\n")
#MATHS

print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multply
print(50 / 50) #devide
print(50 + 50 - 50 * 50 / 50) #BODMAS
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes what is left over
print(50 / 6) #division with remainder (or a float)
print(50 // 6) #no remainder


print("\n")
#VARIABLES AND METHODS

quote = "All is fair in love and war."
print(quote)
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #counts characters

name = "Nishant" #string
age = 15 #int
score = 97.5 #float - has a decimal

print(int(age))
print(int(30.1))
print(int(30.9)) #Will it round? NO.

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1
age += birthday
print(age)


print("\n")
#FUNCTIONS

def who_am_i(): #this is a function without perameters
    name = "Nishant" #loal variable
    age = 30
    print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

def add(x,y):
    print(x + y)

add(7,7)

def multiply(x,y):
    return x * y

multiply(7,7)
print(multiply(7,7))

def square_root(x):
    print(x ** .5)

square_root(64)

def nl(): #new line
    return("\n")


print(nl())
#BOOLEAN EXPRESSIONS (TRUE OR FALSE)

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))


print(nl())
#RELATIONAL AND BOOLEAN OPERATORS
greater_than = 7 > 5
less_than = 5 < 7
greater_than_or_equal_to = 7>=7
less_than_or_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False


#print(nl())
#CONDITIONAL STATEMENTS - if/else

def drink(money):
    if money >= 2:
        return "You've got yourself a drink!"
    else:
        return "No drink for you!"
    
print(drink(3))
print(drink(1))

print(nl())

def alcohol(age,money):
    if (age >= 18) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 18) and (money < 5):
        return "Come back with more money."
    elif (age < 18) and (money >= 5):
        return "Nice try, kid!"
    else:
        return "You're too young and too poor."

print(alcohol(18,5))
print(alcohol(18,4))
print(alcohol(17,5))
print(alcohol(17,4))


print(nl())
#LISTS -Have brackets []
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1]) #returns the second item in the list
print(movies[0]) #returns the first item in the list
print(movies[1:3]) #return the first index number given right until the last number, but not include the last number
print(movies[1:])
print(movies[:1]) #colon works as "up until, number"
print(movies[-1]) #return last iten in list

print(len(movies)) #count items in the list
movies.append("JAWS")
print(movies)

movies.insert(2, "HUSTLE")
print(movies)

movies.pop() #removes the last item
print(movies)

movies.pop(0) #removes the first item
print(movies)

amber_movies = ["Just Go With It", "50 First Dates"]
our_favourite_movies = movies + amber_movies
print(our_favourite_movies)

grades = [["Bob", 82], ["Allice", 90], ["Jeff", 73]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1] = 83
print(grades)


print(nl())
#TUPLES - Do not change, uses ()
grades = ("a", "b", "c", "d", "e", "f")

print(grades[1])