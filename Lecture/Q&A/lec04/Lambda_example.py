def f(x):
  return x + 1

g = lambda x: f                 # This just creates a lambda function that returns an f function. Notice that the formal parameter of lambda function is ignored.


z = lambda x: lambda y: y + 1   # This does the same thing as above using only lambda. 
