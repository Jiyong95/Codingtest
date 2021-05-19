## Array.from()
``` javascript
Array.from({length: 5}, (v, i) => i);
// v : undefined
// i : index
// [0, 1, 2, 3, 4, 5]

Array.from([1, 2, 3], x => x + x);
// [2, 4, 6]

Array.from([1, 2, 3], (v, i) => v + v);
// v = 1, 2, 3
// i = 0, 1, 2
// [2, 4, 6]

Array.from({length: 100}, e => 1);
//[1, 1, 1, 1, ....... 1]  100개
```

## 원소 추가
### 1. Array.push()
- 원소 추가

### 2. splice
- splice로 제거한 요소를 담은 배열 반환.
- 제거 0이면 빈 배열 반환.
- 원본을 수정함.
``` js
const months = ['Jan', 'March', 'April', 'June'];
console.log(months.splice(1, 0, 'Feb')); //[]
//index 1에 0개를 제거하고 'Feb'추가 == Index1에 'Feb'추가

console.log(months);
//["Jan", "Feb", "March", "April", "June"]

months.splice(4, 1, 'May');
// index 4에서 1개 지우고 'May'추가
console.log(months);
// ["Jan", "Feb", "March", "April", "May"]
```

## 원소 제거
### 1. Array.pop()
- 마지막 원소 제거

### 2. Array.shift()
- 첫번째 원소 제거

### 3. splice
``` javascript
let arr = [1,2,3,4];

arr.splice(2,1);
//arr = [1,2,4];
```