#!/usr/bin/python
# -*- coding: utf-8 -*-

# === About ======================================================================================================

"""
 __main__.py

Copyright © 2017 Yuto Mizutani.
This software is released under the MIT License.

Version: 1.0.0

TranslateAuthors: Yuto Mizutani
E-mail: yuto.mizutani.dev@gmail.com
Website: http://operantroom.com

Created: 2017/12/06
Device: MacBook Pro (Retina, 13-inch, Mid 2015)
OS: macOS Serria version 10.12.6
IDE: PyCharm Community Edition 2017.2.4
Python: 3.6.1
"""

# --- References ---
# --- notes ---
# --- Information ---
"""
authors.txtに書かれたフルネームの著者名から，論文引用形式を出力します。
"""
# --- Circumstances ---
"""
CUI上での実行に関するpythonの資産が増えてきたため，簡単なプログラムをpythonで処理しようと考えている。
相変わらずpythonのインデントに慣れず，可読性の観点から1ファイル150行くらいが限界かなと思う。

大学での卒業論文執筆の際，以下の生物学系の論文を引用した。
http://dx.doi.org/10.1038/nature12111

Google ScholarでのAPA Styleの引用が，[...]で省略されており使用できなかった。
本学の卒論では，文中最初の引用と引用文献の際に「全員の名前を省略せずに」記載しろとある。
例外よりも規則が優先される本学にて，全ての著者を引用形式に主導で書き換えるのはﾌﾟﾛｸﾞﾗﾑﾁｮﾄｶｹﾙﾏﾝには苦痛である。
だから作った。

Terminal(zsh)での文字数制限により，.txtファイルを読み込む形式にした。
パッケージ化？次からしよう。
"""

# === import ========================================================================================================

""" Standard library """
import os
""" Third party library """
""" Local library """
# import Other python files
from ReadConfigFile import ReadConfigFileImpl
from ReadTextFile import ReadTextFileImpl
from Translate import TranslateType
from TranslateNatureFormat import TranslateNatureFormatImpl

# === CONSTANTS ========================================================================================================
SELF_PATH = os.path.dirname(os.path.abspath(__file__))

# === User Parameters ==================================================================================================

# === variables ========================================================================================================


# =============================================================================================================

class Main:
    # constants
    FILEPATH_KEY = 'FilePath'
    TRANSLATE_TYPE_KEY = 'TranslateType'
    # variables
    config_reader = ReadConfigFileImpl
    authors_reader = ReadTextFileImpl
    translateType = TranslateType
    translator = TranslateType
    path = ''

    # init
    def __init__(self):
        self.config_reader = ReadConfigFileImpl()
        self.authors_reader = ReadTextFileImpl()
        self.__set_translate_type()
        self.translator = self.translateType()
        self.__set_path()
        self.__copyright()
        self.__translate()

    # models
    def __copyright(self):
        print("[TranslateAuthors-python3]")
        print('Copyright © 2017 Yuto Mizutani.')
        print('This software is released under the MIT License.')
        print('参照元に書かれたフルネームの著者名から，論文引用形式を出力します。')
        print('参照元: {0}'.format(self.path))

    def __set_translate_type(self):
        # read config - type
        translate_type_str = self.config_reader.read(self.TRANSLATE_TYPE_KEY)
        # set type
        if translate_type_str == 'Nature':
            self.translateType = TranslateNatureFormatImpl

    def __set_path(self):
        # read config - path
        path_str = self.config_reader.read(self.FILEPATH_KEY)
        # complemention path
        translated_path = path_str.replace('(SELF_PATH)', os.path.dirname(os.path.abspath(__file__)))
        # set path
        self.path = os.path.expanduser(translated_path)

    def __translate(self):
        # translate and print formatted authors
        authors = self.authors_reader.get_texts(self.path)
        for author in authors:
            self.translator.translate(author)


if __name__ == '__main__':
    main = Main()

# =============================================================================================================
