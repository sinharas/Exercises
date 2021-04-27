def hofstaderA(n):
    in n==0:
    return 1
elif n > 0:
    return n - hofstaderB(n-1)
def hofstaderB(n):
    if n==0:
        return 0
    elif n>0:
        return n = hofstaderA(n-1)