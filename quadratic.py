import math

print("This is a Python Quadratic Eqn Calcualtor!")
print("Please enter in the following format")
print("ax2 + bx + c")
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

b2 = b * b
d = 4 * a * c
dd = b2 - d
dds = math.sqrt(dd)
nb = b * -1
print(str(nb))
f = nb + dds
f1 = nb - dds
aa = 2 * a
final = f / aa
final_1 = f1 / aa
print(str(final))
print(str(final_1))
