def fib(n):
  """Compute the nth Fibonacci number"""
  pred, curr = 0, 1
  k = 1
  while k < 0:
    pred, curr = curr, curr + pred
    k += 1
  return curr
