def compose1(f, g):
  return lambda x: f(g(x))

f = compose1(lambda x: x * x, lambda y: y + 1)
result1 = f(12)

"""------------------------------------------------------------
   The code above is almost the same as below.
"""
def compose2(f, g):           # When you want to return a functionB in a functionA, You have to define a functionB within the functionA,
  def composition(x):         # and that is the time that nested def statement happens.
    return f(g(x))
  return composition

def f1(x):
  return x * x

def f2(y):
  return y + 1

function = compose2(f1, f2)
result2 = f(12)
