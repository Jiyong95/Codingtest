## forEach, for..Of
- forEach 리턴 값 : undefined
- map 은 배열 반환
``` js
const array1 = ['a', 'b', 'c'];

array1.forEach(element => console.log(element));
//"a"
//"b"
//"c"

array1.forEach((element,index) => console.log(element, index));
//"a" 0
//"b" 1
//"c" 2


for (let i of array1){
    console.log(i);
}
// 'a'
// 'b'
// 'c'
```