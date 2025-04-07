import time

# 模擬從某資料來源取得的名字清單
full_names = ["john doe", "jane smith", "bob johnson"]

# 計算有效名字的數量（即包含名字與姓氏的名字）
valid_name_count = 0

# 逐一處理每個全名
for full_name in full_names:
    # 使用 split() 將名字拆成名字與姓氏
    name_parts = full_name.split()

    # 檢查名字是否正好有兩個部分（名字與姓氏）
    if len(name_parts) == 2:
        first_name = name_parts[0]
        last_name = name_parts[1]
        print(first_name + " " + last_name)  # 印出名字與姓氏
        valid_name_count += 1  # 計數器加一

    # 暫停一秒，模擬耗時操作（例如 API 呼叫、IO 操作等）
    time.sleep(1)

# 最後印出有效名字的總數
print("Total valid names: " + str(valid_name_count))

