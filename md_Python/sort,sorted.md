``` python
answer = strings.sort() #answer = None
answer = sorted(strings, key = lambda x: x[n])
```

### sort()
> - return 값 : None
> - sort(reversed=True)

### sorted(list,key)
> - return 값 : list
> - key를 기준으로 정렬


## 2key order
``` python
a_list = ["aaa", "cc", "bb"]
new_list = sorted(a_list, key=lambda x: (len(x), x))
#['bb','cc','aaa']
#len(x)로 정렬한 후 x(알파벳순서)로 정렬
```
## functools.cmp_to_key
- 매개변수 2개를 비교하기 위해 사용
``` python
from functools import cmp_to_key

def cmp_sort(a,b):
    return a-b

sorted([5,2,1,4,3], key=cmp_to_key(cmp_sort))
#1,2,3,4,5
```

