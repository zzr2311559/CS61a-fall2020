def print_all(x)
  print x
  return print_all

print_all(1)(3)(5)




def print_sums(x):
  print(x)
  def next_sum(y):
    return print_sums(x + y)   # Notice that we return a function call here 
  return print next_sum        # Notice that we return a function here

print_sums(1)(3)(5)
