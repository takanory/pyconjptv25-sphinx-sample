# Read the Docs でデプロイする

## requirements.txtを追加

```{code-block} text
:caption: requirements.txt

furo==2022.12.7
myst-parser==0.18.1
Sphinx==5.3.0
```

* githubにpush

## Read the Docsのアカウント設定

* [Read the Docs](https://readthedocs.org/)
* アカウント作成
* GitHubと連携

### プロジェクトをインポート

* pyconjptv25-sphinx-sample
* https://github.com/takanory/pyconjptv25-sphinx-sample
* Git
* main

### Buildを実行

* ボタンを押してBuildを実行
* Webで確認できる <https://pyconjptv25-sphinx-sample.readthedocs.io/>

### Read the Docsで見るとリンクが増えてる

* githubとかのリンクがページの上と下に増えている

## ドキュメントを修正してPush

* 自動でbuildが走る
