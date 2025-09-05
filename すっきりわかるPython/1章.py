# %%
"""

参考書：すっきりわかるPython/377ページ
作成者：さくや
作成日：2025/08
作りたいもの：自動家計簿
            バーコードを読み込むと商品名が自動入力され、家財管理ができるアプリ
            (フードロス削減、片付けの補助、商品の重複購入防止)

目的：基本的な文法のおさらい
    Pythonへの理解を深めるため
    Pythonを使用してゲームや便利ツールを作るため
    初心者を脱却するため
    Pythonに慣れるため
苦手：関数

目標達成期間:2025/09/30まで

"""

# %%
print('Hellow World')

print('Python 頑張る')

# %%
#氏名、年齢、自己紹介を表示

print('さくや')
print('20代')
print('好奇心旺盛&動物大好き')

# %%
#第1部 Pythonの基礎を学ぼう
#第1章 変数とデータ型

print(1)
print(10)

print(1+1) #+
print(10-2) #-
print(13*4) #×
print(28000/23) #÷
print(148//9) #割り算の商
print(98%9) #割り算の余り
print(2**8) #累乗

print('1'+'1')

print('オラ'*7)

print('Python' + 'の世界へようこそ')
print('とっても'*2 + '楽しいよ!')

print('はじめまして\nサクヤです\nギターが趣味です')
print('引用符に\'と\"があります')

# %%
name = 'さくや'
age = '20代'
print(name)
print(age)

print('半径が3cmの円の直径は')
直径 = (3 * 2)
print(直径)
print('その円の演習の長さは、直径×円周率で求まるため、')
print(直径 * 3.14)

age = 20
print('木村の年齢は')
print(age)
age =26
print('うそ。本当は')
print(age)

name,age = '木村',24

print(name)
print(age)

age = 24
print('今年の年齢は')
print(age)
age = age + 1
print('来年は')
print(age)
age = age + 1
print('再来年は')
print(age)

age += 1
print(age)

# %%
name = input('あなたの名前を入力してください')
print('おお' + name + 'よ、其方が来るのを待っていたぞ！')

X = 10
print(type(X))

#type(変数名)で変数に代入されているデータ型を調べることができる


# %%
name = 'さくや'
age = 20
height = 165

print('私の名前は{}で、年齢は{}代で、身長は{}cmです'.format(name,age,height))

#'{}を含む文字列'.format(埋め込む値１,埋め込む値2,....)　のように記載すると見やすいコードになる。
#「.」を忘れないように注意。
#formatの後ろの()内は自動的に文字列に変換される。

from string import hexdigits
name = 'さくや'
age = 20
height = 165

print('私の名前は{}で、年齢は{}代で、身長は{}cmです'.format(name,age,height))
#or
print(f'私の名前は{name}で、年齢は{age}代で、身長は{height}cmです')

#どちらの書き方でも同じ意味となる。

'''
練習問題

1-1

(1)2+10*5 → 2+ 50 → 52
(2)'7'*(3+4) → '7'* 7 → 7777777
(3)'version{}'.format(3+2*0.1+9*0.01) → 'version{}'.format(3+0.2+0.09) → version3.29
(4)4*'num'+'回目のTypeError' → 'numnumnumnum' + '回目のTypeError' → numnumnumnum回目のTypeError

1-2

(1)int型
(2)str型  ❌エラーになる
(3)str型
(4)float型

1-3
BMI計算

h,w = int(input('身長は？(cm)'))/100,int(input('体重は？(kg)'))
print(f'BMIは{w/(h**2)}です')

↑本での正答
'''

# %%
weight = input('体重を入力してください(kg)')
height = input('身長を入力してください(m)')
weight = int(weight)
height = float(height)
BMI = int(weight / height**2)
print(f'BMIは{BMI}')