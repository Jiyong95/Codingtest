import collections
li = ['a','a','b','c','d','d']

dic = collections.Counter(li)
print(dic)
print(dic['a'])