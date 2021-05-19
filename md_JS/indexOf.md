## indexOf()

``` javascript
const beasts = ['ant', 'bison', 'camel', 'duck', 'bison'];

console.log(beasts.indexOf('bison'));
// 1

// 인덱스 2부터 시작해서 bison 찾음.
console.log(beasts.indexOf('bison', 2));
// 4

console.log(beasts.indexOf('giraffe'));
// 못찾으면 -1
```