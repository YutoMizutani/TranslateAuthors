#!/usr/bin/python
# -*- coding: utf-8 -*-

# === About ======================================================================================================

"""
 ReadTextFile.py

Copyright © 2017 Yuto Mizutani.
This software is released under the MIT License.

Version: 1.0.0

TranslateAuthors: Yuto Mizutani
E-mail: yuto.mizutani.dev@gmail.com
Website: http://operantroom.com

Created: 2017/10/26
Device: MacBook Pro (Retina, 13-inch, Mid 2015)
OS: macOS Serria version 10.12.6
IDE: PyCharm Community Edition 2017.2.4
Python: 3.6.1
"""

# --- References ---
# --- notes ---
# --- Information ---

# === import ===========================================================================================================

# === CONSTANTS ========================================================================================================

# === User Parameters ==================================================================================================
""" 変更可能なパラメータ """

# === variables ========================================================================================================

# ======================================================================================================================

class ReadTextFileImpl:
    def get_texts(self, path):
        try:
            return self.__translate_ignore_sharp_charactor_where_the_first(
                self.__get_text_contents_array(path)
            )
        except FileNotFoundError:
            print('Error! File not found...')
            raise FileNotFoundError
        except IOError:
            print('Error! Failed to read file...')
            raise IOError
        except RuntimeError:
            print('Error! An Unknown error occurred!')
            raise RuntimeError

    def __get_text_contents_array(self, path):
        opened_file = open(path)
        text_array = opened_file.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
        opened_file.close()
        text_array = [text.replace('\r', '').replace('\n', '') for text in text_array]  # 改行文字を消す
        return text_array

    def __translate_ignore_sharp_charactor_where_the_first(self, text_array):
        for text in text_array:
            if len(text) > 0 and text[0] == '#':
                text_array.remove(text)
        return text_array

if __name__ == '__main__':
    raise RuntimeError
