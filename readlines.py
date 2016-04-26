import sys # 匯入 sys 模組
file = open(sys.argv[1], 'r') #將檔案設定為執行此 Python Script 後的第一個命令列參數，必須為檔案
for line in file.readlines(): #一次讀取檔案內所有內容，並將其 list 中的每個元素指定給 line
    print(line, end = '') # 印出每一行，最後一行以空白字元作結尾
file.close() # 關閉檔案
