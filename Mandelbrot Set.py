from getkey import getkey

def Mandelbrot(n,w,h,z,px,py):
  print('\n'*(40-int(h/2)))
  print('Screen dimensions =',w,'x',h)
  print('Itterations = ',n,'     Zoom = x',round(1/z,5),sep='')
  print('Position = (',round(px/z,5),',',round(py/z,5),')',sep='')
  print('+'+'='*w+'+')
  for y in range(-int(h/4),int(h/2)-int(h/4)):
    M = '|'
    for x in range(-int(w/2),w-int(w/2)):
      a = 0
      c = 4*(z*x+px)/w+8j*(z*y+py)/w
      i = 0
      while abs(a) < 2 and i < n+1:
        a = a**2 + c
        i += 1
      if i == n+1:
        M += '#'
      else:
        M += ' '
    M += '|'
    print(M)
  print('+'+'='*w+'+')

w = int(input('How wide would you like the screen to be?\n'))
h = int(input('How tall would you like the screento be?\n'))
n = 1
z = 1
px = 0
py = 0
i = ''
while i != ' ':
  Mandelbrot(n,w,h,z,px,py)
  i = getkey()
  if i == ' ':
    break
  if i == 'q':
    z *= 1.2
  if i == 'e':
    z /= 1.2
  if i == 'w':
    py -= w/30*z
  if i == 'a':
    px -= w/15*z
  if i == 's':
    py += w/30*z
  if i == 'd':
    px += w/15*z
  if i == 'z':
    n -= 1
  if i == 'x':
    n += 1
