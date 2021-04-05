def solution(strings, n):
    answer = strings.sort()
    answer = sorted(strings, key = lambda x: x[n])
    print(answer)
    return answer

def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])

strings = ["abce", "abcd", "cdx"] 
print(strange_sort(strings, 2))

# solution(['abce','abcd','cdx'],2)
