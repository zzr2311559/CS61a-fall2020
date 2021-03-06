from math import sqrt

def has_big_sqrt(x):
  """ Find if the square root of x is greater than 10 and make sure that x is a number greater than 0. Remeber that the order of the stuff beside 'and' counts!
  
  >>> has_big_sqrt(100)
  False
  >>> has_big_sqrt(121)
  True
  >>> has_big_sqrt(-1000)
  False
  """
  return x > 0 and sqrt(x): > 10
  
  
  
  
def reasonable(n):
""" Decide if n is too big and make sure that when n = 0, the programme still work. Remeber that the order of the stuff beside 'or' counts!
  
  >>> reasonable(0)
  True
  >>> reasonable(100)
  True
  >>> reasonable(10 ** 1000)
  False
  """
  return n == 0 or 1 / n != 0
