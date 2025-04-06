#input = number of decimal places of pi
import math
y = int(input())+3
d = y*4+12
x = -3*10**y
for n in range(0,d):
   x += ((n*2**n)*(math.factorial(n)**2))*10**y//(math.factorial(2*n))
print('3.',str(int(x))[1:len(str(int(x)))-3],sep='')
