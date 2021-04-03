### 알게 된 것

``` python
import sys

input = sys.stdin.readline
case_num = int(input())
num_list = list()

for i in range(case_num):
	num1,num2 = map(int,input().split())
	num_list.append(num1+num2)

for j in range(case_num):
	print(num_list[j])
```

``` python
import sys

input = sys.stdin.readline() 	=>input = str
case_num = int(input) 			=>input() === str()  :  str obj is not callable
num_list = list()

for i in range(case_num):
	num1,num2 = map(int,input.split())  =>  input.split() 자체가 str.split() 값임 ['case_num']. (readline() 함수가 실행안됨)
											그래서 not enough values오류 발생. num1,num2 2개 필요한데 ['5']니까.
	num_list.append(num1+num2)

for j in range(case_num):
	print(num_list[j])

for k in num_list:  => 이 방법이 더 쉬움.
	print(k)
```
