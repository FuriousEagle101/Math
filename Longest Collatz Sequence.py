#inputs = range to find longest Collatz sequence
mn = int(input())
mx = int(input())+1
y = 0
for i in range(mn,mx):
   x = 0
   w = i
   while w != 4:
      if w%2 == 0:
         w = w/2
      else:
         w = w*3+1
      x += 1
   if x > y:
      y = x
      z = i
print(z)
