#coding: UTF-8
'''
mecab-python3
https://github.com/SamuraiT/mecab-python3
mecab
https://github.com/taku910/meca b
'''
import MeCab

'''
Taggerメソッドの引数
mecabrc: (デフォルト)
-Ochasen: (ChaSen 互換形式)
-Owakati: (分かち書きのみを出力)
-Oyomi: (読みのみを出力)
'''

TEXT = input().strip()
print('# 「元文章」出力結果') 
print(TEXT)

# 分ち書き
tagger = MeCab.Tagger("-Owakati")
result = tagger.parse(TEXT)
print('\n# 「分ち書き」出力結果')
print(result)

# 読みのみ出力
tagger = MeCab.Tagger("-Oyomi")
result = tagger.parse(TEXT)
print('\n# 「読みのみ」出力結果')
print(result)

# 形態素解析
tagger = MeCab.Tagger('-Ochasen')
result = tagger.parse(TEXT)
print('\n# 「形態素解析」出力結果')
print(result)
