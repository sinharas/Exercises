def multiply(a, b):
   if a == 0:
      return 0
   elif a == 1:
      return b
   else:
      return b + multiply(a-1, b)