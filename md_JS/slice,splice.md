## slice
- slice한 복사본을 반환한다.
- 원본을 수정하지 않는다.
``` js

const animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];
console.log(animals.slice(2));
//2,3,4
//["camel", "duck", "elephant"]

console.log(animals.slice(2, 4));
//2,3
//["camel", "duck"]
```

## splice
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
