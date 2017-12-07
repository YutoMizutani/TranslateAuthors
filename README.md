# TranslateAuthors
authors.txtに書かれたフルネームの著者名から，論文引用形式を出力します。

# Circumstances
CUI上での実行に関するpythonの資産が増えてきたため，簡単なプログラムをpythonで処理しようと考えている。
相変わらずpythonのインデントに慣れず，可読性の観点から1ファイル150行くらいが限界かなと思う。

大学での卒業論文執筆の際，以下の生物学系の論文を引用した。
doi: dx.doi.org/10.1038/nature12111

Google ScholarでのAPA Styleの引用が，[...]で省略されており使用できなかった。
本学の卒論では，文中最初の引用と引用文献の際に「全員の名前を省略せずに」記載しろとある。
例外よりも規則が優先される本学にて，全ての著者を引用形式に主導で書き換えるのはﾌﾟﾛｸﾞﾗﾑﾁｮﾄｶｹﾙﾏﾝには苦痛である。
だから作った。

Terminal(zsh)での文字数制限により，.txtファイルを読み込む形式にした。
パッケージ化？次からしよう。

# Screenshot
![ss1](https://github.com/YutoMizutani/TranslateAuthors/blob/master/Screenshots/screenshot0001.png "ss1")
 
