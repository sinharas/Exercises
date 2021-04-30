def reverse(string):
   a=""
   last_index=len(string)-1
   for i in range(last_index,-1,-1):
      a=a+string[i]
   return a
print(reverse("string"))
