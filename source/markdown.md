# markdown対応

## myst-parserを追加

* <https://myst-parser.readthedocs.io/en/latest>/

```bash
(env) $ pip install myst-parser
```

* `extensions` に追加

```python
extensions = [
    "myst_parser"
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

```md
# テストドキュメント

* 箇条書き
* 箇条書き
* [tv.pycon.jp](https://tv.pycon.jp/)
```

