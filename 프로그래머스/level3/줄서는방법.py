def solution(n):
    answer = ''
    for i in range(0,n):
        if i % 2 == 0:
            answer = answer.join('수')
        else:
            answer = answer.join('박')
    return answer


ans = 'k'
print(ans.join('수'))
print(ans.join('수'))
print(ans)