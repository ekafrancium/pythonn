#pythagoras theoram using python
#ΔABC is perpandicular
#side AB = perpandicular
#     BC = base
#	  AC = hypotenuse
#AC**2 = AB**2 + BC**2

import math

print("Enter side AB & BC for find hypotenuse lenth")

a = int(input("Enter side AB :- "))
b = int(input("Enter side BC :- "))	 
c = math.sqrt(a ** 2 + b ** 2)

print(f"Hypotenuse of triangle is {c}")
