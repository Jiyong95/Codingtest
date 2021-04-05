def sol2(s,n):
    answer = []
    lower_list = [x for x in range(ord('a'),ord('z')+1)] #26글자
    upper_list = [x for x in range(ord('A'),ord('Z')+1)]
    for e in list(s):
        if ord(e) in lower_list:
            alpha = lower_list[(ord(e) - lower_list[0] + n)%26]
            answer.append(chr(alpha))
        elif ord(e) in upper_list:
            alpha = upper_list[(ord(e) - upper_list[0] + n)%26]
            answer.append(chr(alpha))
        else:
            answer.append(' ')
    return "".join(answer)



# lower_list = [x for x in range(ord('a'),ord('z')+1)] #26글자
# print(lower_list)

print(sol2("AB", 1))
print(sol2("z", 1))
print(sol2("Z", 10))
print(sol2("a B z", 4))
print(sol2(" aBZ", 20))
print(sol2("y X Z", 4))
print(sol2(" . h z", 20))

