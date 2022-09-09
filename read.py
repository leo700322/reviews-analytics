# 從 reviews.txt 檔案內取出資料，這邊設定為 data，每取出一筆就計數一次(計數設定為 count)
data = []
count = 0
with open('reviews.txt', 'r', encoding='utf-8') as f:
    for line in f: # 從 f 檔案中用 For 迴圈取出 line (every line 這邊當作每筆資料)
        data.append(line) # 每筆加入 data 的 list
        count += 1 # 計數加一次
        if count % 100000 == 0: # % 主要用來求餘數，餘數為零的時候用來計算每幾次為一個單位，這邊使用每一萬次
            print(len(data)) # 列印data的筆數
            
        
print('檔案讀取完畢，共有:', len(data), '筆資料')

print(data[0])


# 100萬筆留言最常出現的字
wc = {} # word_count 字的計數
for d in data:
    words = d.split() # 將每筆資料去掉空格存成 words，但是會殘留空字串；預設值也是分割空白字元，但是不會殘留空字串!
    for word in words:
        if word in wc:
            wc[word] += 1 # 將字的值+1
        else:
            wc[word] = 1 # 新增至wc字典內


# 印出大於1000000萬次的value
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc)) # 總共有多少字在 wc 字典裡


#查詢功能
while True:
    word = input('請問你想查甚麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('這個字沒有出現過喔!')

print('感謝使用本查詢功能。')


# 求平均留言數量
sum_len = 0
for d in data: # 用For迴圈取出總資料 data 的每一筆留言 d (從第一筆到最後一筆)
    sum_len += len(d) # 將取出的每一筆留言長度(每一筆留言長度 = 每一筆留言有多少字串) d 加入 sum_len 裡
    '''
    print(sum_len) # 印出 sum_len 加入 len(d) 之後的結果
    '''
    
print(sum_len) # sum_len 經過上面的 For loop 後變為已加總的總留言長度(每一筆留言字串數量的總和)
print(sum_len / len(data)) # 總留言長度(字數) / 總留言筆數 = 平均每筆留言約為多長(約為多少字串)


# list 篩選功能
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有: ', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])


'''
# 篩選每筆留言中有 good 字串的留言
good = []
for d in data:
    if 'good' in d: # if a in b: (假如 a 在 b 之中)； if a == "某字串": (假如變數 a (完全)等於 "某字串") 
        good.append(d)
print('一共有: ', len(good), '筆留言長度提到good')
print(good[0])
'''

good = [1 for d in data if 'good' in d]
print(good)

'''
35-39快寫法:
good = [d for d in data if 'good' in d]
說明快寫法
1. 從 line 35 取出"good = []"
2. 從 line 38 取出 運算的結果 "good.append(d)" 的變數 "d" 放到 [] 內的第一個位置
3. 從 line 36 取出"for d in data" 不要 ":"
4. 從 line 37 取出"if 'good' in d" 不要 ":" 符號
'''

'''
bad = ['bad' in d for d in data]
print(bad)
'''

'''
bad = []
for d in data:
    bad.append(d)
    if 'bad' in d:
'''
