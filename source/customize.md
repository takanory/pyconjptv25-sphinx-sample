# カスタマイズ

## テーマ変更

* [HTML Theming — Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/theming.html)
* テーマを `bizstyle` に変更

```bash
(env) $ vi source/conf.py
(env) $ make html
```

## ロゴ画像を追加

* <https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output>
* 画像ファイル: <https://tv.pycon.jp/_images/eyecatch.png>

```bash
(env) $ curl https://tv.pycon.jp/_images/eyecatch.png -o source/_static/logo.png 
```

* `source/conf.py` に以下を追加

```python
html_logo = "_static/logo.png"
```
