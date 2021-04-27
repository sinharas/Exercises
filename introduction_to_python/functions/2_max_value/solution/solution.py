# Write your solution here
def max_val(a, b, c):
    if (a >= b) and (a >= c):
        maximum = a
    elif (b >= a) and (b >= c):
        maximum = b
    else:
        maximum = c
    return maximum 