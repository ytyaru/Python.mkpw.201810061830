# このソフトウェアについて

　パスワード作成CUIツール。

# 使い方

```bash
$ python3 mkpw.py
```
```bash
$ python2 ./src/py2.7/mkpw.py
```

## 引数

### デフォルト引数

位置|項目|値
----|----|--
1|figure|`8`
2|number|`10`
3|character|```ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"#$%&'()*+,-./:;<=>?@[\]^_\`{|}~```

### 構文パターン

```bash
$ python3 mkpw.py 桁数 個数 字種
```
```bash
$ python3 mkpw.py 桁数 個数
```
```bash
$ python3 mkpw.py 桁数
```
```bash
$ python3 mkpw.py
```

　省略された引数はデフォルト値を用いる。

### 例

```bash
$ python3 mkpw.py 8 3 "ABCDE"
```

　8桁のパスワードを3個作る。パスワードに用いる文字は`A`,`B`,`C`,`D`,`E`の5つ。

```bash
BCDDCEBA
EBDADDEB
CAAEACCB
```

# 課題

* ヘルプを整備する
* 1行に複数のパスワードを表示する切替を用意する
* 字種をファイルから読み取れるようにする
* パスワード強度設定フラグを用意する
    * 字種グループごとに使うか否かのフラグを用意する
    * 必ず複数の文字種を併用するフラグを用意する
    * 字種ごとにパターンを指定できるようにする (`[小英字]{2}[記号]{1}[大英字]{3}[数字]{2}`, `l2p1u3d2`, `llpuuudd`)
    * 紛らわしい文字を省く（`0O`, `1lI`, `8B`, `9qQ`, `ij`）
    * メタ文字を省く（プログラミング言語(文字列)、スクリプト言語、正規表現）
    * 字種を設定できるフレームワークを作る

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)
