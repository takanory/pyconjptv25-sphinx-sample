# おすすめ拡張機能

* 拡張機能がある
* [Extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
* [yoloseem/awesome-sphinxdoc: A curated list of awesome tools for Sphinx Python Documentation Generator](https://github.com/yoloseem/awesome-sphinxdoc)

## sphinxext-opengraph

* [sphinxext-opengraph 1.0 documentation](https://sphinxext-opengraph.readthedocs.io/en/latest/)
* ogタグを入れてくれる
* 現在の状態を確認 <https://www.opengraph.xyz/>
* `pip install`

```bash
(env) $ pip install sphinxext-opengraph
```

* `requirements.txt` に追加

```text
...
sphinxext-opengraph==0.7.5
```

* `source/conf.py` に設定を追加

```python
extensions = [
    ...
    "sphinxext.opengraph",
]

# sphinxext-opengraph
ogp_site_url = "https://pyconjptv25-sphinx-sample.readthedocs.io/"
ogp_image = "https://pyconjptv25-sphinx-sample.readthedocs.io/en/latest/_static/logo.png"
```

## sphinx-copybutton

* [Sphinx-copybutton](https://sphinx-copybutton.readthedocs.io/en/latest/)
* テキストにコードをコピーするボタンを追加
* `pip install`

```bash
(env) $ pip install sphinx-copybutton
```

* `requirements.txt` に追加

```text
...
sphinx-copybutton==0.5.1
```

* `source/conf.py` に設定を追加

```python
extensions = [
    ...
    "sphinx_copybutton",
]
```

* `test.md` にコードを追加

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

* make htmlしてコードがコピーできることを確認

## sphinx-design

* [sphinx-design](https://sphinx-design.readthedocs.io/en/latest/index.html)
* Grid、Tab、アイコンとかが追加できる

* `pip install`

```bash
(env) $ pip install sphinx-design
```

* `requirements.txt` に追加

```text
...
sphinx-design==0.3.0
```

* `source/conf.py` に設定を追加

```python
extensions = [
    ...
    "sphinx_design",
]

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css",
]
```

* Font Awesomeのフォントを追加
  * [Font Awesome](https://fontawesome.com/search)
  
```md
* {fab}`twitter` @takanory
* {fab}`python` Python
* {fas}`cable-car` ケーブルカー
```

## sphinx-pyscript

* [Sphinx PyScript documentation](https://sphinx-pyscript.readthedocs.io/en/latest/)
* [PyScript](https://pyscript.net/) を埋め込める
* `pip install`

```bash
(env) $ pip install sphinx-pyscript
```

* `requirements.txt` に追加

```text
...
sphinx-pyscript==0.1.0
```

* `source/conf.py` に設定を追加

```python
extensions = [
    ...
    "sphinx_pyscript",
]
```

* markdownに設定を追加

```
---
py-config:
  splashscreen:
    autoclose: true
  packages:
  - matplotlib
---
```

````
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
````