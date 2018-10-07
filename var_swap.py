# How do you swap two numbers without using the third variable?

x, y = 5, 10
y += x
x = y - x
y -= x
print(x,y)
