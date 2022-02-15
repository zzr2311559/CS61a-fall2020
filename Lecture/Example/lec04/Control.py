from math import sqrt
def real_sqrt(n):
  """Find the real part of the square root of n.
  
  >>> real_sqrt(4)
  2.0
  >>> real_sqrt(-4)
  0.0
  """
    if n >= 0:
        return sqrt(n)
    else:
        return 0.0
      
 """-----------------------------------------------------------------------------------------------------
    Using the code below, you will get an error because of the executing rule of a call expression 
 """     
 def if_(c, t, f):
  if c:
    return t
  else:
    return f
  
  def real_sqrt_(x):
    return if_(x >= 0, sqrt(x), 0.0)
