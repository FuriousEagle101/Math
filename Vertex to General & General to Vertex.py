#input = quadratic equation in either vertex or general form
eq = input()
eq = eq.replace(' ','')
eq = eq.replace('y=','')
px = eq.index('x')
if ')^2' in eq:
   pbracket = eq.index(')')
   a = float(eq[0:px-1])
   h = float(eq[px+1:pbracket])
   k = float(eq[pbracket+3:])
   b = str(round(h*2*a,11))
   if float(b) > 0:
      b = '+'+b
   c = str(round(h**2*a+k,11))
   if float(c) > 0:
      c = '+'+c
   if float(c) == 0:
      c = ''
   eq2 = 'y = '+str(a)+'x^2'+b+'x'+c
   print(eq2)
else:
   a = float(eq[:px])
   eq2 = eq[:px]+eq[px+1:]
   px2 = eq2.index('x')+1
   b = float(eq[px+3:px2])
   c = float(eq[px2+1:])
   h = str(b/(2*a))
   if float(h) >= 0:
      h = '+'+h
   k = str(-(float(h)**2*a)+c)
   if float(k) >= 0:
      k = '+'+k
   eq2 = 'y = '+str(a)+'(x'+h+')^2'+k
   print(eq2)
