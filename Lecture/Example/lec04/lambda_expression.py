"""Lambda expression is a short expression that can evaluate to a function. In Python, statements are not allowed to appear in a lambda expression, 
   which factly limits the effect of it. Lambda expression is almost the same as def statement except for one thing, that is only the def statement 
   gives the function an intrinsic name. You can see this difference when you type the function name in the python intepreter. If the function 
   is created by lambda expression, it will display something like <function <lambda> at 0x1003c1bf8>, while the funciton is created using def statement,
   it will dispaly something like <function square at 0x10293e730>(if you named your function 'square'). Try the example yourself will help you 
   get better understanding of this concept.
   
   >>> square(3)
   9
   >>> cube(5)
   125
"""
square = lambda n: n * n

cube = lambda x: x * x * x
