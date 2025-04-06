n = int(input('Find the lucky numbers up to:\n'))
L = []
for i in range(1,n+1,2):
  L.append(i)
D = True
i = 1
while D:
  x = L[i]
  for t in range(1,len(L)//x+2):
    L = L[:t*x-1-(t-1)]+L[t*x-(t-1):]
  i += 1
  if i > len(L)-1:
    D = False
print(L)
