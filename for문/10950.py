"""
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.

예제 입력 1
5
1 1
2 3
3 4
9 8
5 2
예제 출력 1
2
5
7
17
7
"""

import sys

#input = sys.stdin.readline() 	=>input = str
#case_num = int(input) 			=>input() === str()  :  str obj is not callable
input = sys.stdin.readline
case_num = int(input())
num_list = list()

for i in range(case_num):
	#num1,num2 = map(int,input.split())  =>  input.split() 자체가 str.split()임. 입력받는 것이 실행이 안됨.
	num1,num2 = map(int,input().split())
	num_list.append(num1+num2)

for j in range(case_num):
	print(num_list[j])


