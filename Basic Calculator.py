#input = equation using only +, -, * or / (You may use as many numbers and symbols as you wish)
eq = input('Enter an equation using only +, -, * or /.\nYou may use as many numbers and symbols as you wish.\n')
eq = eq.replace(' ','')
eq = eq.lower()
eq2 = eq.replace('-','+')
eq2 = eq2.replace('*','+')
eq2 = eq2.replace('/','+')
SymbolPositions = [-1]
n = eq.count('+') + eq.count('-') + eq.count('*') + eq.count('/')
for i in range(0,n):
  SymbolPositions.append(eq2.index('+'))
  eq2 = eq2[:SymbolPositions[i+1]] + ' ' + eq2[SymbolPositions[i+1]+1:]
SymbolPositions.append(len(eq))
Numbers = []
for i in range(0,n+1):
  Numbers.append(float(eq[SymbolPositions[i]+1:SymbolPositions[i+1]]))
for i in range(0,n):
  if eq[SymbolPositions[i+1]] == '+':
    Numbers[i+1] = Numbers[i] + Numbers[i+1]
  if eq[SymbolPositions[i+1]] == '-':
    Numbers[i+1] = Numbers[i] - Numbers[i+1]
  if eq[SymbolPositions[i+1]] == '*':
    Numbers[i+1] = Numbers[i] * Numbers[i+1]
  if eq[SymbolPositions[i+1]] == '/':
    Numbers[i+1] = Numbers[i] / Numbers[i+1]
print(Numbers[len(Numbers)-1])
