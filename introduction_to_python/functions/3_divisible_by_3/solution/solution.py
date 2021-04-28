def divisible_by_3(*args):
   lst= []
   for num in args:
      if num%3==0:
         lst.append(num)
         #print(num)
      else:
         pass
   return lst