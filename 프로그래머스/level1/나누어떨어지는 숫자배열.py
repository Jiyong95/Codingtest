def solution(arr, divisor):
    answer = []
    for e in arr:
        if e % divisor == 0:
            answer.append(e)
    answer.sort()
    # answer = [x for x in arr if x % divisor == 0]
    # answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer

def solution2(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]