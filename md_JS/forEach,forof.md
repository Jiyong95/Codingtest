## forEach
- forEach 리턴 값 : undefined
- map 은 배열 반환

## for of VS for in
- for of : iterator 속성을 가지는 컬렉션 전용
- for in : 객체의 열거 가능한 속성에 대해 반복

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

for (let i in array1){
    console.log(i);
}
// 0
// 1
// 2

let dic = {'a' : 1, 'b' : 2, 'c' : 3};

for (let e of dic){
    console.log (e);
} 
//error  

for (let e in dic){
    console.log(e);
}
// 'a'
// 'b'
// 'c'
```
