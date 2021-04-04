> ### 출력
``` python
print(a * b3)
print(a * b2)
print(a * b1)
print(a * b)
print(a * b3, a*b2, a*b1, a*b, sep='\n') 위 4가지 출력과 같음

name = 'Jiyong'
print(f"Hello {name}")
```

> ### 입력
	input vs sys.stdin.readline
#### input
``` python
a = int(input())
b = int(input())
```
#### sys.stdin.readline
``` python
import sys
input= sys.stdin.readline().split()
a,b = map(int, input)
```
sys.stdin.readline이 input보다 훨씬 더 빠르다.

