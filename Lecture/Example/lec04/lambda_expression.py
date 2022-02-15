"""Lambda expression is a short expression that can evaluate to a function. In Python, statements are not allowed to appear in a lambda expression, 
   which factly limits the effect of it
   
   >>> square(3)
   9
   >>> cube(5)
   125
"""
square = lambda n: n * n

cube = lambda x: x * x * x
