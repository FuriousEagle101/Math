#input = number of rows of Pascal’s triangle
x = int(input())
y = [[1]]
for i in range(1,x):
   y.append([])
   for t in range(0,i+1):
      if t == 0 or t == i:
         y[i].append(1)
      else:
         y[i].append(y[i-1][t-1]+y[i-1][t])
for z in range(0,x):
   print(y[z])
