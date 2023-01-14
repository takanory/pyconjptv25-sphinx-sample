# おすすめ拡張機能

* 拡張機能がある
* [Extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
* [yoloseem/awesome-sphinxdoc: A curated list of awesome tools for Sphinx Python Documentation Generator](https://github.com/yoloseem/awesome-sphinxdoc)

## sphinxext-opengraph

* [sphinxext-opengraph 1.0 documentation](https://sphinxext-opengraph.readthedocs.io/en/latest/)

* 追加する前に確認 <https://www.opengraph.xyz/>
* ogタグを入れてくれる

```bash
(env) $ pip install sphinxext-opengraph
```

* `requirements.txt` に追加

```text
...
sphinxext-opengraph=0.7.5
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
