def sum_naturals(n):
  """Sum the first N natural numbers
  
  >>> sum_naturals(5)
  15
  """
  total = 0
  k = 1
  while k <= n:
    total += k
    k += 1
  return total

def sum_cubes(n):
  """Sum the first N cubes of natural numbers
  
  >>> sum_cubes(5)
  225
  """
  total = 0
  k = 1
  while k <= n:
    total += pow(k, 3)
    k += 1
  return total

"""------------------------------------------------------------------------
   generaliazed version
"""
def identity(k):
  return k

def cube(k):
  return pow(k, 3)

def summation(n, term):
  """Sum the first N terms of a sequence.
  
  >>> summation(5, cube)
  225
  """
  total = 0
  k = 1
  while k <= n:
    total += term(k)
    k += 1
  return total

def sum_naturals(n):
  """Sum the first N natural numbers
  
  >>> sum_naturals(5)
  15
  """
  return summation(n, identity)
  
def sum_cubes(n):
  """Sum the first N cubes of natural numbers
  
  >>> sum_cubes(5)
  225
  """
  return summation(n, cube)
