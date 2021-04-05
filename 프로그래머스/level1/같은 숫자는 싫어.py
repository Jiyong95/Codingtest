def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return answer

def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
    
def sol2(arr):
    answer = []
    answer = [e for e in arr if e not in answer] 
    print(answer)
    return answer
print(solution([1,2,3,4]))
# 연산이 다 끝난 후 대입되서 [1,1,2,2,3,3]으로 나온다.