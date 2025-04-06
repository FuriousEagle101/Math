#input = linear equation
line=input()
px=line.index("x")
m=float(line[2:px])
b1=float(line[px+1:len(line)])
dot="-"
b=b1/-m
m=1/m
for i in range(10,0,-1):
   if int(m*i+b)<0:
      print(" "*int(3*(m*i+b+7)),dot," "*(19-int(3*(m*i+b+7))),"|",sep="")
   elif int(m*i+b)>0:
      print(" "*20,"|"," "*int(3*(m*i+b)-3),dot,sep="")
   else:
      print(" "*20,"|",sep="")
print("="*45)
for i in range(-1,-11,-1):
   if int(m*i+b)<0:
      print(" "*int(3*(m*i+b+7)),dot," "*(19-int(3*(m*i+b+7))),"|",sep="")
   elif int(m*i+b)>0:
      print(" "*20,"|"," "*int(3*(m*i+b)-3),dot,sep="")
   else:
      print(" "*20,"|",sep="")
print("x intercept =",b)
print("y intercept =",b1)
