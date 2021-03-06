def end(n, d):
  """Print the final digits of N in reverse order until D is found.
  
  >>> end(34567, 5)
  7
  6
  5
  """
  while n > 0:
    digit = n % 10
    print (digit)
    if digit == d:
      return None
    n  = n // 10
    
    
"""----------------------------------------------------------------
   
   >>> search(is_three)
   3
   >>> search(positive)
   11
   >>> sqrt = inverse(square)
   >>> sqrt(16)
   4
   >>> sqrt(256)
   16
"""
def search(f):
  x = 0
  while True:      # alternative: while not f(x):
    if f(x):       #                  x += 1
      return x     #              return x
    x += 1
    
def is_three(x):
  return x == 3

def square(x):
  return x * x

def positive(x):
  return man(o, square(x) - 100)

def inverse(f):                                   # This function basically says evaluate a function which is going through [0, infinite integer) 
  """Return g(y) such that g(f(x)) -> x."""       # to find a value that corresponds to the number that the given 'y' specified
  return lambda y : search(lambda x: f(x) == y)

def inverse_(f):                                                      # An alternative way of doing inverse. 
                                                                      # Notice that everytime a nested def statement has been created, a generalization is completed. 
                                                                      # So you can say that it is because I have to do a generalizaion, I created
                                                                      # a nested def statement like this.
  """ Return a function g(y) that returns x such that f(x) == y.
  >>> sqrt = inverse_(square)
  >>> sqrt(16)
  4
  >>> sqrt = inverse_(square)(25)
  >>> sqrt
  5
  """
  def inverse_of_f(y):
    def is_inverse_of_y(x):
      return f(x) == y
    return search(is_inverse_of_y)
  return inverse_of_f

