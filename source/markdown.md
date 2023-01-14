# markdown対応

## myst-parserを追加

* <https://myst-parser.readthedocs.io/en/latest>/

```bash
(env) $ pip install myst-parser
```

* `extensions` に追加

```python
extensions = [
    "myst_parser",
]
```

## markdownのファイルを追加

* `source/index.rst` を修正

```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   test
```

* `source/test.md` を追加

```bash
(env) $ cd source
(env) $ mkdir images
(env) $ curl https://pbs.twimg.com/profile_images/192722095/kurokuri_400x400.jpg -o images/takanory.jpg
```

```md
# テストドキュメント

* 箇条書き
* 箇条書き
* [tv.pycon.jp](https://tv.pycon.jp/)

![takanory](images/takanory.jpg)
```

