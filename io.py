import sys # 匯入 sys 模組
file = open(sys.argv[1], 'r') # 將檔案設定為執行此 Python Script 後的第一個命令列參數，必須為檔案
content = file.read() # 讀入前述檔案並存到 content 這個變數中
file.close() # 關閉檔案
print(content) # 印出檔案內容
