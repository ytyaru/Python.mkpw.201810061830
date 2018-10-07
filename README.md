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

```
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"#$%&'()*+,-./:;<=>?@[\]^_\`{|}~
```

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

#### 字種を指定する

　shellから字種を指定するには工夫がいる。ここでは全字種を指定する2つの方法を紹介する。

A. シングルクォート
B. ダブルクォート

##### A. シングルクォート

　shell構文のシングルクォート(`'`)はリテラル文字列を指定する。従って、シングルクォート内ではエスケープができず、シングルクォート自身を含めることができない。

　そこで、文字列結合によって解決する。`'ABC'` + `\'` + `'DEF'`となる。shell構文では文字結合に`+`や`&`は不要なので、省く。また、スペースを入れてしまうと次の起動引数になってしまうためスペースを含めずに書く。すると以下のようになる。

```bash
$ python3 mkpw.py 8 10 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"#$%&'\''()*+,-./:;<=>?@[\]^_`{|}~'
8 10 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
R[KOnyPo
alp\K(9$
tPy{o$?o
PY*S0$]M
\L^ZRvX)
;.~3^.R@
/62}|W6(
~{yEWI8s
"e9S^Ppk
&(ZR.tGC
```

##### B. ダブルクォート

　shell構文のダブルクォートはエスケープや変数展開ができる。従って、shell構文におけるメタ文字をエスケープすることで解決を試みる。

```bash
$ python3 mkpw.py 8 10 "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\!\"#$%&'()*+,-./:;<=>?@[\\]^_\`{|}~"
```

　よく見ると、引数値の出力が間違っている。`9`と`!`の前に`\`がある。これはエスケープ文字のつもりだった。本来の`\`は`[`と`]`の間にある。

```
8 10 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\!"#$%&'()*+,-./:;<=>?@[\\]^_\`{|}~
```

　だが、`!`の前の`\`を取ると、bashコマンドになってしまう。bashのヒストリ展開機能である。([情報源](https://qiita.com/anqooqie/items/785f46a8cc5f10ba7abb))

```
$ python3 mkpw.py 8 10 "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_\`{|}~"
bash: !\: event not found
```

　ヒストリ展開の機能を無効化することで正しく実行できる。

```
$ set +H
$ python3 mkpw.py 8 10 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\!"#$%&'\''()*+,-./:;<=>?@[\\]^_\`{|}~'
8 10 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\!"#$%&'()*+,-./:;<=>?@[\\]^_\`{|}~
G(~b+24-
htDTjfC'
+dSbbNel
U{&@R<I!
T9y*e.$<
R>akWiF\
8aq^>I!b
e?=B@S@\
.}A\E}z|
Q\&JKahM
```

# 既知のバグ

* 字の出現率が不均等になることがある
    * 字種指定したとき同じ文字が重複するとその文字の出現率が上がる
        * 対策: 重複文字を削除する

# 課題

* ヘルプを整備する
* 1行に複数のパスワードを表示する切替を用意する
* 字種をファイルから読み取れるようにする（shell構文のせいで記号の字種指定が難しすぎる）
* 使用する字種を選べるようにする
    * サービス側で使える字種のみを指定したい（自由設定＆記録＆選択）
    * 見間違い、書き間違い、言い間違い、聞き間違いを防ぎたい（紛らわしい文字を省く（`0O`, `1lI`, `8B`, `9qQ`, `ij`））
    * プログラミングで使いたい（メタ文字を省きたい（プログラミング言語(文字列)、スクリプト言語、正規表現））※それ以前にハッシュ化して使うべきか
* パスワード強度設定フラグを用意する
    * 必ず複数の文字種を併用する
    * 字種が連続しないようにする（`1234`, `ABCD`, `111`, `CCC`）
    * 一定時間より早く解析されるパスワードは除外する
        * パスワード解析予測時間を算出する
            * （最新コンピュータの性能情報をどこからどうやって入手するか）
* 要らないかもしれない
    * 字種グループごとに使うか否かのフラグを用意する
    * 字種ごとにパターンを指定できるようにする (`[小英字]{2}[記号]{1}[大英字]{3}[数字]{2}`, `l2p1u3d2`, `llpuuudd`)
    * 字種を設定できるフレームワークを作る

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)
