### 알게 된 것

> ### 출력
``` python
print(int(a/b))
print(a//b)
```
``` python
print(a * b3)
print(a * b2)
print(a * b1)
print(a * b)
print(a * b3, a*b2, a*b1, a*b, sep='\n') 위 4가지 출력과 같음
H = 1, M = 2
print("{} {}".format(H,M))
print(H,M,sep = ' ')
```
둘 다 출력 값이 같다.

> ### 입력
	input vs sys.stdin.readline
>> #### input
``` python
a = int(input())
b = int(input())
```
>>#### sys.stdin.readline
``` python
import sys
input= sys.stdin.readline().split()
a,b = map(int, input)
```
sys.stdin.readline이 input보다 훨씬 더 빠르다.

