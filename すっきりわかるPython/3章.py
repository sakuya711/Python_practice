# %%
#if文
name = input("名前を入力してください:")
print(f"こんにちは、{name}さん")
food = input('好きな食べ物は何ですか？:')
if food =='寿司':
    print('私も寿司が好きです')
else:
    print(f'私も{food}好きですよ!')

# %%
name = input('あなたの名前を教えてください')
print(f'こんにちは、{name}さん')
food = input(f'{name}さんの好きな食べ物を教えてください')
if 'カレー' in food:
    print('私もカレーが好きです')
else:
    print(f'私も{food}が好きですよ')

# %%
scores = {'数学': 80, '英語': 75, '国語': 90}
key = input('追加する科目名を入力してください')
if key in scores:
    print(f'{key}はすでに登録されています')
else:
    date = int(input(f'{key}の点数を入力してください'))
    scores[key] = date
print(scores)

# %%
score = int(input('試験の点数を入力してください'))
if score < 0 or score > 100:
    print('点数は0から100の間で入力してください')
elif score >= 60:
    print('合格です')
else:
    print('不合格です')

# %%
""""
練習問題
3-1
(1)変数priceに1.1をかけ、その数字が30万以下か
(2)❌
(3)変数kansaiに'gihu'が含まれているか
(4)a+bが60以下かつ、deyの値が3であるか
(5)Flseかどうか


3-2
(1)initial == 'K'
(2)point >= 80 and point < 256
(3)bmi < 20 or bmi >=25
(4)year / 4 == 0 ❌year % 4 == 0
(5)day != 28 and day != 30 and day != 31 ❌not(day in [28,30,31])

3-4
(1)1,3,5,7,8,10,12
(2)4,6,9,11
(3)2

"""
#3-3
#1
isError = False
n = 50

if isError == False and n <100:
    print('OK')

#2
score = int(input('数字を入力してください'))
if score % 2 == 0:
    print('偶数')
else:
    print('奇数')

#3
aisatu = input ('挨拶を入力してください')

if aisatu == 'こんにちは':
    print('ようこそ！')
elif aisatu =='景気は？':
    print('ぼちぼちです')
elif aisatu == 'さようなら':
    print('お元気で！')
else:
    print('どうしました？')

