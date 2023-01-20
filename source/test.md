---
py-config:
  splashscreen:
    autoclose: true
  packages:
  - matplotlib
---

# テストドキュメント

* 箇条書き
* 箇条書き
* [tv.pycon.jp](https://tv.pycon.jp/)

![takanory](images/takanory.jpg)

```python
for i in range(1, 101):
    match i % 3, i % 5:
        case (0, 0):
            print("FizzBuzz")
        case (0, _):
            print("Fizz")
        case (_, 0):
            print("Buzz")
        case _:
            print(i)
```

## Font Awesome

* {fab}`twitter` @takanory
* {fab}`python` Python
* {fas}`cable-car` ケーブルカー

## PyScript

```{py-repl}
def fizzbuzz(num):
    match i % 3, i % 5:
        case (0, 0):
            return "FizzBuzz"
        case (0, _):
            return "Fizz"
        case (_, 0):
            return "Buzz"
        case _:
            return i

for i in range(1, 101):
    print(fizzbuzz(i), end=", ")
    if i % 10 == 0:
        print()
print()
```

```{py-terminal}
```