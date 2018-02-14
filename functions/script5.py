#coding: utf-8

def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    return cost - 50
  elif days >= 3:
    return cost - 20
  else:
    return cost

print rental_car_cost(10)
