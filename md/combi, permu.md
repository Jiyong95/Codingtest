## permutation(순열), Combination(조합)

``` python
from itertools import permutations
a = [1, 2, 3]

#a에서 2개 원소로 순열 만든다.
#return : permutations obj
permu = permutations(a, 2)
print(list(permu))
#[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]



form itertools import combinations
a = [1, 2, 3]

#a에서 2개 원소로 조합 만든다.
#return : combinations obj
combi = combinations(a, 2)
print(list(combi))
#[(1,2),(1,3),(2,3)]

```