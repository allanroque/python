#coding: utf-8
def cube(number):
  number = number ** 3
  print number

def by_three():
  if number % 3 == 0:
    cube(number)
  else:
    return false

number = int(raw_input('digite o numero: '))

cube(number)
