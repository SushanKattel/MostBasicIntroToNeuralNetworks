
def cost(b):
    return (b-4)**2

x=cost(0)
print(x)

def num_slope(b):
    h= 0.0001
    return (cost(b+h)-cost(b))/h  #  numerical approximation of slope

print(num_slope(3))
print(num_slope(5))

def slope(b):
    return 2* (b-4)  # Derivative of function to find slope.

print(slope(3))  # ans is closer to numerical approximation
print(slope(5))
print("--------------------------------------------------------------")

#  This can be taken as training loop

b = 8
jpt = 0
for jpt in range(7):      # on each loop, b is minimized and is closer to 4. Change range to see...

    b = b-.1* slope(b)   # we are minimizing b by a fraction of 1/10
    print(b)
    jpt = jpt+1
print("--------------------------------------------------------------")

