# 탐색 알고리즘 DFS, BFS

## 선행지식
- 스택
- 큐
- 재귀함수

## 재귀함수
- 재귀함수는 스택자료구조를 이용
- 마지막에 호출한 함수가 끝나야 그 앞의 함수 호출이 종료
- 점화식 이용

## 스택 + 큐 => Deque
``` python
#스택구현
from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)        #deque([1, 2, 3])
stack.pop()  
print(stack)        #deque([1, 2])
arr = list(stack)   #[1,2]


#큐구현
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)        #deque([1,2,3])
queue.popleft()     
print(queue)        #deque([2,3])


#While

queue = deque()
queue.append(1)
queue.append(2)
while queue:
    print(queue.popleft())  #1, 2

```


## DFS(깊이 우선 탐색)
- 깊은 부분을 우선적으로 탐색
- 스택 이용 -> 재귀
``` python
dfs(){
    if 범위

    if 처리
    
    dfs() 재귀
}
```

## BFS(너비 우선 탐색)
- 가까운 부분부터 탐색
- 큐 이용