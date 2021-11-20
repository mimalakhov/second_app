import math

#First
print("Enter the first number")
a=float(input())
print("Enter the second number")
b=float((input()))
print("\nResults:")
print("{} + {} = {}".format(a, b, a+b))
print("{} - {} = {}".format(a, b, a-b))
print("{} * {} = {}".format(a, b, a*b))
if (b != 0): print("{} / {} = {}".format(a, b, a/b))
else: print(":((")
print("{} ** {} = {}".format(a, b, a**b))
if (b != 0): print("{} % {} = {}".format(a, b, a%b))
else: print(":((")
if (b != 0): print("{} // {} = {}".format(a, b, a//b))
else: print(":((")

#Second
print("{}{}{}".format("Hello, ", input("\nEnter your name: "), "!"))

#Third
print("{}{}".format("Reversed: ", input("\nEnter your string: ")[-1:-3:-1]))

#Fourth
r=float(input("\nEnter radius: "))
if (r <= 0): print("???")
else: print("{}{}".format("Area: ", (r**2)*math.pi))