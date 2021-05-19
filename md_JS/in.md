## in 연산자
- 사용법
> 속성 in 객체명

### 1.인덱스 in 배열
``` javascript
var trees = new Array("redwood", "bay", "cedar", "oak", "maple");
0 in trees         // 0 인덱스가 있냐? => true
3 in trees         // 3 인덱스가 있냐? => true
5 in trees         // false
```
### 2.메소드 in 객체
``` javascript
var color1 = new String("green");
"length" in color1 // String 객체는 length(길이를 반환하는 메소드)를 가지고 있기 때문에 true

var color2 = "coral";
"length" in color2 // color2는 String 객체가 아님(length 메소드 x) false
```
### 3. key in dictionary
``` javascript
var myCar = {company: "Lamborghini", model:"Lamborghini Veneno Roadster", year: 2014};

"company" in myCar; // true를 반환합니다.

```

## includes()
``` javascript
"abcd".includes('a') //true
```