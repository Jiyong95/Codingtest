import sys
input = sys.stdin.readline().split()
h,m = map(int, input)

if m >= 45 :
	print(h, m - 45)
elif m < 45 and h >= 1 :
	print(h-1, m + 15)
else :
	print(h + 23, m + 15)
