#a = int(input())
#b = int(input())
#b1 = int(b/100)
#b2 = int(b%100/10)
#b3 = b%10
#print(a * b3)
#print(a * b2)
#print(a * b1)
#print(a * b)
#print(a * b3, a*b2, a*b1, a*b, sep='\n') 위 4가지 출력과 같음
#print("%d"%(10))


import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = b
while (b):
	print(a * (b%10))
	b = b//10
print(a*c)
