#ax+bx2+cx+d=0
import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())

p = b - a**2 / 3
q = ((2 * a**3) / 27) - ((a * b) / 3) + c

delta = (q**2 / 4) + (p**3 / 27)
w = delta
print("delta =", w)


if d >= 0:
  print("EQUATION HAS 3 ROOTS")
  x = (-q / 2 + math.sqrt(w))**(1 / 3) + ((-q / 2 - math.sqrt(w))**(1 / 3)) - (a / 3)
  print(x)
elif d == 0:
  print("EQUATION HAS 3 ROOTS, BUT TWO OF THEM ARE EQUAL!")
  x1 = -2 ((q / 2)**(1 / 3))
  x2 = x3 = ((q / 2)**(1 / 3) - (a / 3))
  print('x1=', x1, 'x2 & x3=', x2)
elif d <= 0:
  print("EQUATION HAS 3 DIFFERENT ROOT")
  x10=((2/math.sqrt(3))*math.sqrt(-1*p))*math.sin((1/3)*(1/math.sin((3*math.sqrt(3*q))/(2*(math.sqrt(-1*p)))**3))-(a/3))
  x20=((-1)*(2/math.sqrt(3))*math.sqrt(-1*p))*math.sin((1/3)*(1/math.sin((3*math.sqrt(3*q))/(2*(math.sqrt(-1*p)))**3)+(math.pi/3))-(a/3))
  x3=((2/math.sqrt(3))*math.sqrt(-1*p))*math.cos((1/3)*(1/math.sin((3*math.sqrt(3*q))/(2*(math.sqrt(-1*p)))**3)+(math.pi/6))-(a/3))
  print("x10=", x10, "x20=", x20, "x3=", x3)
                       
  