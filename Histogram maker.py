#1st input = number of list items
#2nd input = number of bars in histogram
#other inputs = list items
#putting a * beside a value marks it as your score
n = int(input())
b = int(input())
l = []
a = 0
e = ''
for i in range(0,n):
   h = input()
   if '*' in h:
      h = h.replace('*','')
      e = float(h)
   h = float(h)
   a += h
   l.append(h)
a /= n
print('mean =',a)
l.sort()
if n%2 == 0:
   print('median =',(l[int(n/2)]+l[int((n-2)/2)])/2)
else:
   print('median =',l[int((n-1)/2)])
z = [0]
for g in range(0,n):
   m = l[g]
   if m not in z:
      if l.count(m) == z[0]:
         z.append(m)
   if l.count(m) > z[0]:
      z = [l.count(m),m]
w = str(z[1:len(z)])
w = w.replace('[','')
w = w.replace(']','')
print('mode =',w,'(appears',z[0],'times)')
print('minimum =',l[0])
print('maximum =',l[n-1])
print('range =',l[n-1]-l[0])
y = 0
for t in range(0,n):
   x = l[t]
   y += (x-a)**2
print('Standard deviation =',(y/n)**0.5)
if e != '':
   print('Your score =',e)
   print('Z score =',(e-a)/(y/n)**0.5)
print('')
k = len(str(int((l[n-1]-l[0])/b*(b-1)+l[0]+1))+str(int((l[n-1]-l[0])+l[0]+1)))
for d in range(0,b):
   q1 = int((l[n-1]-l[0])/b*d+l[0]+d/b)
   q2 = int((l[n-1]-l[0])/b*(d+1)+l[0]+(d+1)/b)
   r = 0
   for s in range(0,len(l)):
      if l[s] >= q1 and l[s] < q2:
         r += 1
   r2 = r/n*100
   print(' '*(k-len(str(q1))-len(str(q2))),q1,' to ',q2,'|','='*int(r2),r,sep='')
