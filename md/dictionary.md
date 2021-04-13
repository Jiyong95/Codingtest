## dictionary

```python
1.선언
dic = {}
type(dic) # class : dict

dic = {'a' : 1, 'b' : 2}

dic[0] #error
dic['a']

dic['c'] = 3 # dic = {'a' : 1, 'b' : 2, 'c' : 3}




2.dictionary 변환

newdict = dict( alice = 5, bob = 20, tony= 15, suzy = 30)
# {'alice' : 5, 'bob' : 20, 'tony' : 15 ...}

name_and_ages = [['alice', 5], ['Bob', 13]]
dict(name_and_ages)  #{'alice': 5, 'Bob': 13}

***주의***
key로 set, list, dict 사용 불가



3.for 문

a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}

for key in a:
	print(key)

alice
bob
tony
suzy


for val in a.values():
	print(val)

[1, 2, 3]
20
15
30


for key, val in a.items():
	print(key, val)


4.삭제
# dictionary

a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}

del a['alice']
```
