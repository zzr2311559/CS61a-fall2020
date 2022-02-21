def make_adder(n):
  return lambda k: n + k

"""
   >>> make_adder(2)(3)  notice that 'make_adder' is a function that returns a function while 'add' takes 2 value and return the eventual value
   5
   >>> add(2, 3)
   5
"""


def curry2(f):
  """Transform the two-argument functions such as 'add' to higher-order funcitons such as 'make_adder'
     >>> from operator import add
     >>> add(2, 3)
     5
     >>> m = curry2(add)
     >>> add_three = m(3)
     >>> add_three(2)
     5
  """
  def g(x):
    def h(y):
      return f(x, y)
    return  h
  return g

