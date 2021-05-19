## Filter
> arr.filter(callback(element, (index), (array), thisArg))
- filter()는 호출되는 배열을 변화시키지(mutate) 않습니다.
``` javascript

const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];

const result = words.filter((word, i) => i > 3);
// i(index)가 3보다 큰것만 filter
console.log(result);
// destruction, present

```

## Map
> arr.map(callback(currentValue[, index[, array]])[, thisArg])
- 배열의 각 요소에 대해 실행한 callback의 결과를 모은 새로은 배열 반환.
``` javascript

var numbers = [1, 4, 9];
var doubles = numbers.map(num => num * 2);
console.log(dobules)
// [2, 8, 18]
```

## Reduce
>arr.reduce(callback[, initialValue])
- reduce() 메서드는 배열의 각 요소에 대해 주어진 리듀서(reducer) 함수를 실행하고, 하나의 결과값을 반환합니다.
- 리듀서 함수의 반환 값은 누산기에 할당되고, 누산기는 순회 중 유지되므로 결국 최종 결과는 하나의 값이 됩니다.
``` javascript

const array1 = [1, 2, 3, 4];
const reducer = (accumulator, currentValue) => accumulator + currentValue;

// 1 + 2 + 3 + 4
console.log(array1.reduce(reducer));
// 10

// 5 + 1 + 2 + 3 + 4
console.log(array1.reduce(reducer, 5));
// 15


[0, 1, 2, 3, 4].reduce(function(accumulator, currentValue, currentIndex, array) {
  return accumulator + currentValue;
});
```
- 콜백은 4번 호출됩니다. 각 호출의 인수와 반환값은 다음과 같습니다.  
1. 처음에 0,1 이 들어오고 반환값 acc에 저장
2. 그다음부터는 2 들어오고 반환값 acc에 저장
3. 3들어오고 ...
4. 4들어오고 ...

|callback|accumulator|currentValue|currentIndex|array|반환 값|
|---|---|---|---|---|---|
|1번째 호출|	0|	1|	1|	[0, 1, 2, 3, 4] |1 |
|2번째 호출|	1|	2|	2|	[0, 1, 2, 3, 4]	|3 |
|3번째 호출|	3|	3|	3|	[0, 1, 2, 3, 4]	|6 |
|4번째 호출|	6|	4|	4|	[0, 1, 2, 3, 4]	|10|

