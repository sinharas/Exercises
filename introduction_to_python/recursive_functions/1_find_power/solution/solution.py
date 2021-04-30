def power(a, b):
  
    # if power is 0 or 1 then number is returned
    if(b == 0 or b == 1):
        return a
    else:
        return (a*power(a, b-1))
