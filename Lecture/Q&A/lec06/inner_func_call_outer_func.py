"""Notice that since f is defined in the global frame, it will be define only once and used many times, while g is defined within the f function, 
   so every time g is returned, it will create a new g which will used only once.
"""
def f(x):
  def g(y):
    return f
return g

result = f(2)(3)(4)(5)
