import math

# A+B:
def M_add(A,B):
   C = []
   for i in range(0,len(A)):
      C.append(A[i]+B[i])
   return C

# A-B:
def M_subtract(A,B):
   C = []
   for i in range(0,len(A)):
      C.append(A[i]-B[i])
   return C

# A*B:
def M_multiply(A,B):
   if type(B) == float or type(B) == int:
      C = []
      for i in range(0,len(A)):
         C.append(A[i]*B)
      return C
   a = A[0]*B[0]+A[1]*B[2]
   b = A[0]*B[1]+A[1]*B[3]
   c = A[2]*B[0]+A[3]*B[2]
   d = A[2]*B[1]+A[3]*B[3]
   return [a,b,c,d]

# A/B:
def M_divide(A,B):
   if type(B) == float or type(B) == int:
      C = []
      for i in range(0,len(A)):
         C.append(A[i]/B)
      return C
   C = M_multiply(M_inverse(B),A)
   return C

# A^B:
def M_exponent(A,B):
   if type(A) == list and (type(B) == float or type(B) == int):
      if B == 0:
         return [1,0,0,1]
      C = A
      for i in range(0,B-1):
         C = M_multiply(C,A)
      return C
   if A == 'e':
      C = B
      for i in range(0,60):
         C = M_add(C,M_divide(M_exponent(B,i),math.factorial(i)))
      return M_subtract(C,B)
   if type(A) == float or type(A) == int:
      return M_exponent('e',M_multiply(B,math.log(A,math.e)))
   return M_exponent('e',M_multiply(B,M_ln(A)))

# ln(A):
def M_ln(A):
   if type(A) == float or type(A) == int:
      return math.log(A,math.e)
   B = A
   for i in range(0,10):
      B = M_sqrt(B)
   B = M_multiply(B,1024)
   C = A
   for i in range(0,10):
      C = M_sqrt(C)
   C = M_inverse(C)
   C = M_multiply(C,-1024)
   return M_divide(M_add(B,C),2)

# Adjoint(A):
def M_adjoint(A):
   if len(A) == 4:
      Adj = [A[3],-A[1],-A[2],A[0]]
   if len(A) == 9:
      Adj = []
      Adj.append(M_determinant([A[4],A[7],A[5],A[8]]))
      Adj.append(-M_determinant([A[1],A[7],A[2],A[8]]))
      Adj.append(M_determinant([A[1],A[4],A[2],A[5]]))
      Adj.append(-M_determinant([A[3],A[6],A[5],A[8]]))
      Adj.append(M_determinant([A[0],A[6],A[2],A[8]]))
      Adj.append(-M_determinant([A[0],A[3],A[2],A[5]]))
      Adj.append(M_determinant([A[3],A[6],A[4],A[7]]))
      Adj.append(-M_determinant([A[0],A[6],A[1],A[7]]))
      Adj.append(M_determinant([A[0],A[3],A[1],A[4]]))
   return Adj

# Determinant(A):
def M_determinant(A):
   if len(A) == 4:
      d = A[0]*A[3]-A[1]*A[2]
   if len(A) == 9:
      d = A[0]*M_determinant([A[4],A[5],A[7],A[8]])
      d -= A[1]*M_determinant([A[3],A[5],A[6],A[8]])
      d += A[2]*M_determinant([A[3],A[4],A[6],A[7]])
   if len(A) == 16:
      d = A[0]*M_determinant([A[5],A[6],A[7],A[9],A[10],A[11],A[13],A[14],A[15]])
      d -= A[1]*M_determinant([A[4],A[6],A[7],A[8],A[10],A[11],A[12],A[14],A[15]])
      d += A[2]*M_determinant([A[4],A[5],A[7],A[8],A[9],A[11],A[12],A[13],A[15]])
      d -= A[3]*M_determinant([A[4],A[5],A[6],A[8],A[9],A[10],A[12],A[13],A[14]])
   return d

# Inverse(A):
def M_inverse(A):
   B = M_multiply(M_adjoint(A),1/M_determinant(A))
   return B

# Square root(A):
def M_sqrt(A):
   if type(A) == float or type(A) == int:
      return A**0.5
   x,y,z,w = A[0],A[1],A[2],A[3]
   a = ((x**3-w*y*z+3*x*y*z+w**2*x-2*w*x**2+2*(w*x*y**2*z**2-y**3*z**3)**0.5)/(w**2-2*w*x+x**2+4*y*z))**0.5
   c = ((z*x-z*a**2)/y)**0.5
   d = (a**2-x+w)**0.5
   b = y/(a+d)
   return [a,b,c,d]

# Hyperbolic sine(A):
def M_sinh(A):
   B = M_exponent('e',A)
   C = M_exponent('e',M_multiply(A,-1))
   D = M_divide(M_subtract(B,C),2)
   return D

#* A!:
def M_factorial(A):
   B = M_sqrt(M_multiply(A,2*math.pi))
   C = M_exponent(M_divide(A,math.e),A)
   D = M_multiply(A,M_sinh(M_inverse(A)))
   D = M_exponent(M_sqrt(D),A)
   E = M_multiply(M_exponent(A,2),35)
   E = M_multiply(M_exponent(A,3),M_add(E,[33,0,0,33]))
   E = M_exponent('e',M_multiply(M_inverse(E),7/324))
   F = M_multiply(M_multiply(M_multiply(B,C),D),E)
   return F
