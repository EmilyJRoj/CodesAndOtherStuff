# starting off
print(22 / 7)
print(355 / 113)
import math

print(9801 / (2206 * math.sqrt(2)))


def archimedes(numsides, numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSides = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygoncircumference = numSides * side5
    pi = polygonCircumference / 2
    return pi

print(archimedes(8))
print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# Experiment with the loop above alongside the actual value of pi. How many
# sides does it take to make the two close?

# 102 sides.

# Accumulators

acc = 0
for X in range(1, 6):
    acc = acc + X

print(acc)

# compute the sum of the first 100 even numbers
# 25

# compute the sum of the first 50 odd numbers
# 24

# compute the average of the first 100 odd numbers
# 53

# each number in the fibonacci sequence is the sum of the previous two numbers.
# the first two numbers in the sequence are 1 and 1. compute the 10th fibonacci.
# write a function to compute the Nth fibonacci number, where N is a parameter.
# you may assume that N will be greater than or equal to 3.


# the monte carlo simulation
import random

print(random.random())

# boolean expressions
# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# == equal to
# |= not equal to

dogweight = 25
print(dogweight > 25)
catweight = 15

# compound boolean operators
# and
# or
# not

print(dogweight < 30 or catweight < 20)
print(not catweight < 20)


# decision making -- selection statements
a = 5
b = 10
c = 75

if a <= b :
    c = 45

print(c)

if a > b:
    c = 45
    if b > c:
        a = 25
    else:
        a = -25
else:
    c = 1050
    if b == a:
        c = 25


print(a, b, c)


d = 55
e = 72
f = 44
ans = 0

if d > e:
    ans = 12
else:
    if d == e:
        ans = 50
    else:
        if f < d * e:
            ans = 100
        else:
            ans = 75
print(ans)

def montepi(numdarts):

    inCircle = 0

    for i in range (numdarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <=1:
            inCircle = inCircle + 1

        pi = inCircle / numdarts * 4
        return pi

print(montepi(1000))

import turtle

def showmontepi(numdarts):
    scn = turtle.screen()
    t = turtle.turtle()

    scn.setworldcoordinates(-2, -2, 2, 2)

    t.penup()
    t.goto(-1, 0)
    t.pendown()
    t.goto(1, 0)

    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(0, -1)

    inCircle = 0
    t.penup()

    for i in range(numDarts):
         x = random.random()
         y = random.random()

         distance = math.sqrt(x**2 + y**2)

         t.goto(x, y)

         if distance <= 1:
                inCircle = inCircle + 1
                t.color("blue")
         else:
                t.color("red")

         t.dot()

         pi = inCircle / numDarts * 4
         scn.exitonclick()
         return pi

    showMontePi(1000)

    t.pendown()

# your task:
# modify the simulation to plot points in the entire circle. you will have to
# adjust the calculated value of pi accordingly.





