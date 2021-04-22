## heap(= 우선순위 큐)
- 넣는 순서에 상관없이 최대부터 빠지는 걸 Max Heap,  
최소부터 빠지는 걸 Min Heap이라고 한다.
 
 
## 사용법
``` python
import heapq
 
1. 선언
heap = []
 
2. heap에 원소 추가
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
 
print(heap)
#[1, 3, 4] 오름차순 정렬 아님.
 
 
3. heap 원소 삭제
heaqp.heappop(heap)
#가장 작은 원소가 삭제 된다.
 
4. heap 변환
list = [3, 4, 1]
heapq.heapify(list)
 
5. Max-heap만들기
 
Max_heap = []
nums = [4,1,7,3,8,5]
 
for num in nums:
    heapq.heappush(Max_heap, (-num, num))
#[(-8, 8), (-7, 7), (-5, 5), (-1, 1), (-3, 3), (-4, 4)]
#오름차순 정렬 안되있음.
 
while heap:
    print(heapq.heappop(heap)[1])
#뺄때마다 최소값을 앞으로 만들어주면서 빠짐.
#결국 오름차순을 빠진다.
```
 

