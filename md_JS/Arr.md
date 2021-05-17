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