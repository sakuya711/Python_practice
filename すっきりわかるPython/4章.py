# %%
print('さあ、寝ようかしら')
i = 0

while i <10:
    print(f'羊が{i}匹')
    i += 1

print('おやすみなさい')

# %%
#試験の平均点を求める
count = 0
student_num = int(input('学生の数を入力'))
score_list = list()
while count < student_num:
    count += 1
    score = int(input(f'{count}人目の試験の得点を入力'))
    score_list.append(score)
print(score_list)
total = sum(score_list)
print(f'平均点は{total/student_num}点です')


# %%
for num in range(2):
    print('こんにちは!')

# %%
"""
練習問題
4-1
(1)5
(2)5
(3)5
(4)5
(5)5
(6)5
(7)4
(8)5

"""

#4-2
count = 0
print('カレーを召し上がれ')
while count < 10:
    count += 1
    print(f'{count}皿のカレーを食べました')
    print('おかわりはいかがですか？(y/n)')
    okawari = input()
    if okawari == 'n':
        print('ごちそうさまでした')
        break
    if okawari == 'y':
        count += 1

# %% 
#4-2正解
count =1
ans = True
print('カレーを召し上がれ')
while ans == True:
    print(f'{count}皿のカレーを食べました')
    key = input('おかわりはいかがですか？(y/n)')
    if key == 'y':
        count += 1
    else:
        ans = False
print('ごちそうさまでした')

# %%
#4-3
i = 0
for i in range(10):
    print(i,end='')
print('Lite off!')

# %%
#4-3正解
for n in range(10):
    print(f'{10-n}',end='')
print('Lift off!')

# %%
#4-4
#1九九
for i in range(1,10):
    for j in range(1,10):
        print(f'{i}x{j}={i*j}')

# %%
#2
for i in range(1,10):
    if i % 2 == 0:
        continue
    for j in range(1,10):
        print(f'{i}x{j}={i*j}')

# %%
#3
for i in range(1,10):
    if i % 2 == 0:
        continue
    for j in range(1,10):
        if i*j > 50:
            break
        print(f'{i}x{j}={i*j}')

# %%
#4-5
temp = list()
for i in range(10):
    num = float(input(f'{i+1}個目の数値を入力'))
    temp.append(num)
    print(temp[i])

temp_new = list()
for j in range(10):
    num = float(input(f'{i+1}個目の数値を入力'))
print(f'平均気温は{sum(temp_new)/len(temp_neew)}度です')

# %%
#4-5正解
temp = list()
for n in range(10):
    date = float(input(f'{n+1}個目の数値を入力'))
    temp.append(date)
for count in range(10):
    print(f'{count+8}時の気温は{temp[count]}度です')

temp_new = list()
for count in range(len(temp):
    if count == 5:
        temp_new.append('N/A')
    else:
        temp_new.append(temp[count])
print(temp)
print(temp_new)

total = 0
for data in temp_new:
    if isinstance(data,float):
        total += data
print(total/len(temp_new)-1)

# %%
#4-6
numbers = [1,1]
i =0
while numbers[i+1] <= 1000:
    numbers.append(numbers[i]+numbers[i+1])
    i += 1
print(numbers)

ratios = list()
for i in range(len(numbers)):
    if i == len(numbers)-1:
        break
    n = (numbers[i+1]/numbers[i])
    ratios.append(n)
print(ratios)

for i in range(len(ratios)):
    ratios[i] = int(ratios[i]*1000)/1000
print(ratios)

