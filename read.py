# 從 reviews.txt 檔案內取出資料，這邊設定為 data，每取出一筆就計數一次(計數設定為 count)
data = []
count = 0
with open('reviews.txt', 'r', encoding='utf-8') as f:
    for line in f: # 從 f 檔案中用 For 迴圈取出 line (every line 這邊當作每筆資料)
        data.append(line) # 每筆加入 data 的 list
        count += 1 # 計數加一次
        if count % 10000 == 0: # % 主要用來求餘數，餘數為零的時候用來計算每幾次為一個單位，這邊使用每一萬次
            print(len(data)) # 列印data的筆數
            
        
print('檔案讀取完畢，共有:', len(data), '筆資料')

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