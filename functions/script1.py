#coding: utf-8
def square(n):
  squared = n ** 2
  print " %d squared is %d " % (n, squared)
  return square

n = int(raw_input('digite o numero: '))
square(n)
