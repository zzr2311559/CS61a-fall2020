"""Q1.1----------------------------------------------------
"""
def wears_jacket_with_if(temp, raining):
  """
  
  >>> wears_jacket_with_if(90, False)
  False
  >>> wears_jacket_with_if(40, False)
  True
  >>> wears_jacket_with_if(100, True)
  True
  """
  if temp < 60 or raining == True:
    return True
  else:
    return False


def wears_jacket(temp, raining):
    return temp < 60 or raining == True
  
"""Q1.2-----------------------------------------------------
   The result of the code below will be an infinite loop because x will never be less than or equal to 0
"""
def square(x):
  print("hello!")
  return x * x

def so_slow(num):
  x = num
  while x > 0:
    x += 1
  return x / 0

square(so_slow(5))

"""Q1.3--------------------------------------------------------
"""
def is_prime(n):
  """
  
  >>> is_prime(10)
  False
  >>> is_prime(7)
  True
  """
  factor = n - 1
  while factor > 1:
    if n % factor == 0:
      return False
    factor -= 1
  return True

