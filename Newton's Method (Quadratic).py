# x_n = x_n-1 - f(x)/f'(x)

original_eq = input('Enter a quadratic equation of the form ax^2 + bx + c:\n')
eq = original_eq
eq = eq.replace(' ','')
eq = eq.lower()
eq = eq.replace('y=','')
eq = eq.replace('=y','')
eq = eq.replace('f(x)=','')

px = eq.index('x')
a = float(eq[0:px])
eq = eq[px+3:len(eq)]
px = eq.index('x')
b = float(eq[0:px])
c = float(eq[px+1:len(eq)])

print('\na = ',a,',   b = ',b,',   c = ',c,sep='')

x = float(input('\nPick a spot to start iterating:\n'))
i = int(input('\nEnter the number of iterations you want:\n'))

print('Iteration # |     x','\n-------------+-------------\n0            |',x)
for k in range(0,i):
  y = x - (a*x*x+b*x+c)/(2*a*x+b)
  x = y
  print(k+1,' '*(11-len(str(k+1))),'|',x)
print('\nThere is a root of',original_eq,'near',x)

x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
print('\nactual roots (using quadratic formula): x =',x1,'or',x2)
