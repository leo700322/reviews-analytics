data = []
count = 0
with open('reviews.txt', 'r', encoding='utf-8') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0: # % 主要用來求餘數
            print(len(data))
            
        
print('檔案讀取完畢，共有:', len(data), '筆資料')

# 求平均留言數量
sum_len = 0
for d in data:
    sum_len += len(d)
    # print(sum_len)
print(sum_len)
print(sum_len / len(data))