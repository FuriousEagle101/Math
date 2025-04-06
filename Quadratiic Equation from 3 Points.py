#input = 3 points in a graph
def simplify(p):
   p = p.replace(' ','')
   p = p.replace('(','')
   p = p.replace(')','')
   pcomma = p.index(',')
   x = float(p[0:pcomma])
   y = float(p[pcomma+1:len(p)])
   return [x,y]
at,bt = 1,1
p1,p2,p3 = simplify(input()),simplify(input()),simplify(input())
eq1 = [p1[1],-(p1[0])**2,-p1[0]]
eq2 = [p2[1],-(p2[0])**2,-p2[0]]
eq3 = [p3[1],-(p3[0])**2,-p3[0]]
eq4 = [(eq1[0]-eq2[0])/(eq2[2]-eq1[2]),(eq1[1]-eq2[1])/(eq2[2]-eq1[2])]
eq5 = [(eq2[0]-eq3[0])/(eq3[2]-eq2[2]),(eq2[1]-eq3[1])/(eq3[2]-eq2[2])]
a = (eq4[0]-eq5[0])/(eq5[1]-eq4[1])
b = a*eq4[1]+eq4[0]
c = a*eq1[1]+b*eq1[2]+eq1[0]
if a == int(a):
   a = int(a)
if b == int(b):
   b = int(b)
if c == int(c):
   c = int(c)
if c == 0 and not (a == 0 and b == 0):
   c = ''
elif c > 0 and not(a == 0 and b == 0):
   c = '+'+str(c)
if b > 0 and a != 0:
   b = '+'+str(b)
if a == 0:
   a = ''
   at = 0
if a == 1:
   a == ''
if b == 0:
   b = ''
   bt = 0
if b == 1:
   b = ''
print('y = ',a,'x²'*at,b,'x'*bt,c,sep='')
