"""
예제 입력 1
5
예제 출력 1
    *
   **
  ***
 ****
*****
"""
import sys
input = sys.stdin.readline
num = int(input())

for i in range(1,num+1):
	print(" "*(num-i)+"*"*i)
