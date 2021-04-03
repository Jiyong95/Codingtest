"""
문제
N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

예제 입력
2

예제 출력 1
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
"""

import sys
input = sys.stdin.readline()
num = int(input)

for i in range(1,10):
	print("{} * {} = {}".format(num,i,num*i))
