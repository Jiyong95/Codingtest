import sys
input = sys.stdin.readline().split()
a,b = map(int, input)

if a>b:
	print(">")
elif a==b:
	print("==")
else :
	print("<")
