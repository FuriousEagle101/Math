#input = number of primes to find
end = int(input())
for n in range(1,end+1):
   prime = True
   for d in range(2,int(end**0.5)+1):
      if n != d:
         if n%d == 0:
            prime = False
   if prime == True:
      print(n)
