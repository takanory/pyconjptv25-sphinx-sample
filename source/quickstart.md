# Quickstart

## githubでリポジトリ作成

* githubでリポジトリを作成する <https://github.com/takanory/>

```bash
$ git clone git@github.com:takanory/pyconjptv25-sphinx-sample.git
$ cd pyconjptv25-sphinx-sample
```

## Sphinxインストール

* 諸般の事情で最新ではなくSphinx 5.3.0をインストールする

```bash
$ python3.10 -m venv env
$ . env/bin/activate
(env) $ pip install sphinx==5.3.0
```

## Sphinx quick start

* sphinxでHTMLを生成して表示

```bash
(env) $ sphinx-quickstart
> Separate source and build directories (y/n) [n]: y
> Project name: PyCon JP TV #25 sample project
> Author name(s): takanory
> Project release []: 
> Project language [en]: ja
(env) $ make html
(env) $ ls build/html
(env) $ open build/html/index.html
```

## ファイル構成を確認

* ファイル構成を確認する

```bash
(env) $ ls -CF  # ファイルを確認
LICENSE		README.md	env		source
Makefile	build		make.bat
```

## rstを書き換える

* `source/index.rst` を書き換える
* [reStructuredText入門 — Sphinx documentation](https://www.sphinx-doc.org/ja/master/usage/restructuredtext/basics.html)

```bash
(env) $ make html
```
