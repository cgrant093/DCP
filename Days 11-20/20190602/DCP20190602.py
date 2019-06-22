import random as rnd

# define monte carlo method
def isInCircle(r):
    x = rnd.uniform(-1, 1)
    y = rnd.uniform(-1, 1)

    if (x**2 + y**2) <= r**2:
        return 1

    else:
        return 0


radius = 1
totalMCPts = 0
inCirclePts = 0

i = 0
while i<1000000:
    totalMCPts += 1
    inCirclePts += isInCircle(radius)
    i += 1


# need to divide total by 4 because we are looking at radius
#   and area of a square is 4 r^2 = (2r)^2 = d^2
print("The monte carlo estimate of pi using a circle is", inCirclePts/(totalMCPts/4))

