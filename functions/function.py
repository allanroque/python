def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print "With tax: %f" % bill
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print "With tip: %f" % bill
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)


------------------

Funcao simples

def spam():
  """funcao do eggs!"""
  print "Eggs!"
  
spam()


------------------

def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared
  
# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.

square(10)

------------------

def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!


------------------

funcao chamando funcao

def fun_one(n):
  return n * 5

def fun_two(m):
  return fun_one(m) + 7

------------------------

def shout(phrase):
  if phrase == phrase.upper():
    return "YOU'RE SHOUTING!"
  else:
    return "Can you speak up?"

shout("I'M INTERESTED IN SHOUTING")

----------------------------


def cube(number):
  return number ** 3

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return false

-----------------------------

# Ask Python to print sqrt(25) on line 3.
import math
print math.sqrt(25)

----------------------

EXEMPLO
from module import function

from math import sqrt

from module import *

from math import *
-----------------------------

VER FUNCOES DE UM MODULO

import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything # Prints 'em all!


FUNCAO TYPE

print type(42)
print type(4.2)
print type('spam')

<type 'int'>
<type 'float'>
<type 'str'>

print type(11)
print type(1.1)
print type('ola')
print type(True)

<type 'int'>
<type 'float'>
<type 'str'>
<type 'bool'>

---------------------

funcao max
maximum = max(1,2,3)

print maximum

funcao min
minimum = min(1,2,3)

print minimum

funcao abs
absolute = abs(3,-3)

print absolute

---------------------

def speak(message):
  return message

if happy():
  speak("I'm happy!")
elif sad():
  speak("I'm sad.")
else:
  speak("I don't know what I'm feeling.")


---------------------


def is_numeric(num):
  return type(num) == int or type(num) == float:

max(2, 3, 4) # 4
min(2, 3, 4) # 2

abs(2) # 2
abs(-2) # 2

--------------------

def distance_from_zero(n):
  if type(n) == int or type(n) == float:
    return abs(n)
  else:
    return "Nope"

------------------

def bigger(first, second):
  print max(first, second)
  return True

----------------

def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
  	return 475






































