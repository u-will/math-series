def fibonacci (num):
  if num == 0 or num == 1:
    return 0 if num == 0 else 1
  return fibonacci(num -1) + fibonacci(num -2)

def lucas (num):
  if num == 0 or num == 1:
    return 2 if num == 0 else 1
  return lucas (num - 1) + lucas(num -2)


# that's how you create a argument with optional value
def sum_series(num, opArga=0, opArgb=1): 
  if num == 0 or num == 1:
    return opArga if num == 0 else opArgb
  return sum_series(num - 1, opArga, opArgb) + sum_series(num -2, opArga, opArgb)