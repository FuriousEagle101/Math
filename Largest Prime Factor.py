#input = natural number
x = int(input())
y = 2
not_done = True
while not_done:
   while x%y == 0 and x != y:
      x = x/y
   y += 1
   if y**2 > x:
      not_done = False
print(int(x))
