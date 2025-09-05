# %%

members = ['工藤','木村','佐藤']
print(members[0])
print(members[1])

# %%
#試験の点数
scores = [90,85,70,100]
total = sum(scores)
print(f'合計{total}点')


# %%
scores = [90,85,70,100]
total =sum(scores)
avg = total / len(scores)
print(f'合計{total}点、平均{avg}点')

# %%
members = ['小山','増田','加藤']
members.append('森')
members.append('草野')
print(members)

# %%
members = ['小山','増田','加藤','森']
members.remove('森')
print(members)

# %%
members = ['森','増田','加藤']
members[0] = '小山'
print(members)

# %%
a = [1,4,6,2,7,9,3,8]
print(a[1:3]) #1から3の手前まで
print(a[3:])  #3から最後まで
print(a[:4])  #最初から4の手前まで
print(a[-3:]) #後ろから3つ

# %%
#ディクショナリの作成
scores = {'国語':90,'数学':85,'英語':70}
print(scores)
print(scores['数学'])

# %%
scores = {'国語':90,'数学':85,'英語':70}
scores['理科'] = 100 #新しい要素の追加
scores['国語'] = 95 #国語の点数を変更
del scores['英語'] #英語の要素を削除
print(scores)

# %%
#ディクショナリの合計
scores = {'国語':90,'数学':85,'英語':70}
total = sum(scores.values())
print(f'合計{total}点')

# %%
#タプル(変更不可のリスト)
point = (90,85,70)
print(point[1])

# %%
#セット(重複不可、順序なし)
a = {1,2,3,4,5}
a .add(3) #重複する3は追加されない
a .add(6) #6は追加される
print(a)

# %%
mamber_hobby = {
    '増田':{'ファッション','音楽'},
    '加藤':{'音楽','映画','カメラ'}
}
print(mamber_hobby)
print(mamber_hobby['加藤'])

# %%
#&(積集合)、|(和集合)、-(差集合)、^(排他的論理和)
mamber_hobby = {
    '増田':{'ファッション','音楽'},
    '加藤':{'音楽','映画','カメラ'}
}
print(mamber_hobby['増田'] & mamber_hobby['加藤']) #共通の趣味

# %%
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A & B) #積集合
print(A | B) #和集合
print(A - B) #差集合
print(A ^ B) #排他的論理和

# %%
""""
練習問題2
2-1
(1)ディクショナリ
(2)リスト
(3)セット
(4)ディクショナリ ❌セット
(5)リスト ❌ディクショナリ

"""
#2-2
tennsuu = [
    int(input('国語の点数を入力してください')),
    int(input('算数の点数を入力してください')),
    int(input('理科の点数を入力してください')),
    int(input('社会の点数を入力してください')),
    int(input('英語の点数を入力してください'))
]
total = sum(tennsuu)
avg = total / len(tennsuu)
print(f'合計{total}点、平均{avg}点')


# %%
#2-3
player1 = {'サッカー','カメラ','音楽','映画','旅行'}
player2 = {'野球','音楽','映画','ゲーム','ドライブ'}
input('心の準備ができたらEnterキーを押してください')
seki = player1 & player2
wa = player1 | player2
aisyou = (len(seki) / len(wa)) * 100
print(f'相性度は{aisyou}%です')
# %%
