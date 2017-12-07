#!/usr/bin/python
# -*- coding: utf-8 -*-

# === About ======================================================================================================

"""
 TranslateNatureFormat.py

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

# === import ===========================================================================================================
""" Standard library """
""" Third party library """
""" Local library """
# import Other python files
from Translate import TranslateType

# === CONSTANTS ========================================================================================================

# === User Parameters ==================================================================================================
""" 変更可能なパラメータ """

# === variables ========================================================================================================

# ======================================================================================================================

class TranslateNatureFormatImpl(TranslateType):
    #### presenter
    def translate(self, text):
        inTextsAuthors = self.__get_authors_str_format_in_texts(text)
        inReferencesAuthors = self.__get_authors_str_format_in_references(text)

        print('-----------------------------------------------------------------------------')
        print('変更前')
        print(text)
        print()
        print('文中引用時記載形式 (e,g. LastName1, LastName2, and LastName3)')
        print(inTextsAuthors)
        print()
        print('文献記載形式 (e,g. LastName1, F1., LastName2, F2., and LastName3, F3.)')
        print(inReferencesAuthors)
        print('-----------------------------------------------------------------------------')

    ### usecases
    def __get_authors_str_format_in_texts(self, text):
        # e,g. Kerstin Howe, Matthew D. Clark, Carlos F. Torroja, (省略) Jane Rogers, & Derek L. Stemple
        # v
        # e,g. Howe, Clark, Torroja, (省略) Rogers, & Stemple

        # separate by ", " and delete "& " from text (add after)
        full_name_authors_array = self.__split(text.replace('& ', ''), [', '])

        result_formatted_authors = ''
        for full_name_author in full_name_authors_array:
            # get (translate) author's last name
            last_name_author = self.__translate_author_only_last_name(full_name_author)

            # add author's last name
            result_formatted_authors += last_name_author

            # add split word
            split_word = ', '
            if full_name_author != full_name_authors_array[-1]:
                result_formatted_authors += split_word

            # add last authors mark where the second from the last
            last_authors_mark = '& '
            if full_name_author == full_name_authors_array[-2]:
                result_formatted_authors += last_authors_mark

        return result_formatted_authors

    def __get_authors_str_format_in_references(self, text):
        # e,g. Kerstin Howe, Matthew D. Clark, Carlos F. Torroja, (省略) Jane Rogers, & Derek L. Stemple
        # v
        # e,g. Howe, K., Clark, M. D., Torroja, C. F., (省略) Rogers, J., & Stemple, D. L.

        # separate by ", " and delete "& " from text (add after)
        full_name_authors_array = self.__split(text.replace('& ', ''), [', '])

        result_formatted_authors = ''
        for full_name_author in full_name_authors_array:
            # get (translate) author's last name
            last_name_author = self.__translate_author_only_last_name(full_name_author)
            # get (translate) author's all initials
            initials_author = self.__get_initials(full_name_author)

            # add author's last name
            result_formatted_authors += last_name_author
            # add split word
            split_word = ', '
            result_formatted_authors += split_word
            # add author's initials
            result_formatted_authors += initials_author

            # add split word again (but not to add last authors mark where the last)
            split_word = ', '
            if full_name_author != full_name_authors_array[-1]:
                result_formatted_authors += split_word
            # add last authors mark where the second from the last
            last_authors_mark = '& '
            if full_name_author == full_name_authors_array[-2]:
                result_formatted_authors += last_authors_mark

        return result_formatted_authors

    #### translator
    def __translate_author_only_last_name(self, author_full_name):
        # e,g. Kerstin Howe
        # v
        # e,g. Howe

        # 名前をスペースで区切る。
        splitted_author_name = self.__split(author_full_name, ' ')
        # 区切られた名前の最後がlast_name
        last_name = splitted_author_name[-1]
        return last_name

    def __get_initials(self, author_full_name):
        # e,g. Matthew D. Clark
        # v
        # e,g. M. D.

        initials_array = []

        # 名前をスペースで区切る。
        splitted_author_name = self.__split(author_full_name, ' ')

        for separated_name in splitted_author_name:
            # 区切られた名前の最後がlast_nameなので，それ以外を取り出す。
            if separated_name != splitted_author_name[-1]:
                # 最後以外の名前からイニシャルだけ抽出する。
                initial = self.__get_initial(separated_name)
                # イニシャルを追加
                initials_array.append(initial)

        # イニシャルのリストを文字に直す。
        initials_str = ''
        for initial in initials_array:
            initials_str += initial
            # 最後でなければ区切り文字を追記
            split_word = ' '
            if initial != initials_array[-1]:
                initials_str += split_word

        return initials_str

    #### models
    def __get_last_name(self, text):
        text[0] = text[0].upper()
        return text

    def __get_initial(self, text):
        return text[0].upper() + '.'

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

    def __decisionIncludeKeyword(self, text, keyword):
        """[text]から[keyword] -> Bool """
        # print(keyword in text)
        return keyword in text

    def __pickOtherWords(self, text, keyword):
        """[text]から[keywordを除く文字を返す] -> String """
        return text.replace(keyword, '')