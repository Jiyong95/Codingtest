import time

start = time.time()
def solution(n):
    num_arr = [0] + [1] * n
    m = int(n ** 0.5)
    for i in range(2,m+1):
        for j in range(i*i,n+1,i):
            num_arr[j] = 0
    print(num_arr.count(1))
    return 0
print(solution(5))
print(time.time() - start)