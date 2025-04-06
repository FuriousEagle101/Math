#input x 100 = number of tests
import random
numbers = []
times = int(input())
for t in range(0,times):
   minimum = random.randint(1,10000)
   maximum = random.randint(10001,100000)
   for i in range(0,100):
      x = str(random.randint(minimum,maximum))
      if len(x)>1:
         x = x[0:1]
      numbers.append(int(x))
for n in range(1,10):
   n_percentage = numbers.count(n)/times
   print(n,"|","="*int(n_percentage*2),n_percentage,"%",sep="")