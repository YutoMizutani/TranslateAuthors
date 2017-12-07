#!/usr/bin/python
# -*- coding: utf-8 -*-

# === About ======================================================================================================

"""
 ReadConfigFile.py

Copyright © 2017 Yuto Mizutani.
This software is released under the MIT License.

Version: 1.0.0

TranslateAuthors: Yuto Mizutani
E-mail: yuto.mizutani.dev@gmail.com
Website: http://operantroom.com

Created: 2017/12/07
Device: MacBook Pro (Retina, 13-inch, Mid 2015)
OS: macOS Serria version 10.12.6
IDE: PyCharm Community Edition 2017.2.4
Python: 3.6.1
"""

# --- References ---
# --- notes ---
"""
"""
# --- Information ---

# === import ===========================================================================================================
""" Standard library """
import os
""" Third party library """
""" Local library """

# === CONSTANTS ========================================================================================================

# === User Parameters ==================================================================================================
""" 変更可能なパラメータ """

# === variables ========================================================================================================

# ======================================================================================================================


class ReadConfigFileImpl:
    # Settings file path
    SETTING_FILE_PATH = os.path.expanduser(os.path.dirname(os.path.abspath(__file__)) + '/config.ini')

    def read(self, keyword, default=''):
        try:
            # try to get contents text
            text_array = self.__translate_ignore_sharp_charactor_where_the_first(
                self.__openFile(self.SETTING_FILE_PATH)
            )
            return self.__read_settings(text_array, keyword, default)
        except:
            self.__display_import_error(self.SETTING_FILE_PATH)
            raise RuntimeError

    def __read_settings(self, text_array, keyword, default=''):
        result = default
        for line in text_array:
            if self.__decision_include_keyword(line, keyword):
                result = self.__translate_ignore_before_blanks(
                    self.__split(line, ': ')[-1]
                )
        return result

    def __display_import_error(self, path):
        # If cannot read files, print error massages and work default values.
        print('Can not read \"{0}\"! '.format(path))

    # -- Translator ----------------------------------------
    def __translate_ignore_sharp_charactor_where_the_first(self, text_array):
        for text in text_array:
            if len(text) > 0 and text[0] == '#':
                text_array.remove(text)
        return text_array

    def __translate_ignore_before_blanks(self, text):
        # e.g. '   a bc' -> 'a bc'
        is_not_blank_find_yet = True
        result = ''
        for char in text:
            if is_not_blank_find_yet:
                if char != ' ':
                    is_not_blank_find_yet = False
            if not is_not_blank_find_yet:
                result += char
        return result

    # -- Model ---------------------------------------------
    def __openFile(self, path):
        opened_file = open(path)
        text_array = opened_file.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
        opened_file.close()
        text_array = [text.replace('\r', '').replace('\n', '') for text in text_array]  # 改行文字を消す
        return text_array

    def __decision_include_keyword(self, text, keyword):
        # return bool
        return keyword in text

    def __split(self, text, split_words):
        if isinstance(split_words, list):
            if len(split_words) > 0:
                rawText = text
                for split_word in split_words:
                    if split_word == split_words[0]:
                        continue
                    else:
                        rawText = rawText.replace(split_word, split_words[0])

                return rawText.split(split_words[0])
            else:
                print('Error: split_words length under 1 in __split()')
                raise RuntimeError
        else:
            return text.split(split_words)
