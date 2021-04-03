"""
입력
첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

출력
각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

예제 입력 1
5
1 1
12 34
5 500
40 60
1000 1000
예제 출력 1
2
46
505
100
2000
"""

import sys
input = sys.stdin.readline
test_num = int(input())
num_list = list()
#num_list = list()


for i in range(test_num):
	num1,num2 = map(int,input().split())
	num_list.append(num1+num2)

for j in range(test_num):
	print(num_list[j])

""" 시간초과
test_num = int(input())
num_list = list()

for i in range(test_num):
	num1,num2 = map(int,input().split())
	num_list.append(num1+num2)

for j in range(test_num):
	print(num_list[j])
"""
