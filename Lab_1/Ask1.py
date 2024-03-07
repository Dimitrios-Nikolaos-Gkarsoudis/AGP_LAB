import math

a = math.sqrt((2**101)/((math.pi**53)+(11**7)))
print(a)

s = str(a)
s = s.replace('.', '')
print(s[:10])
