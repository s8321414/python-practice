import sys # 匯入 sys 模組
file = open(sys.argv[1], 'r') # 將檔案設定為執行此 Python Script 後的第一個命令列參數，必須為檔案
while True: # while 迴圈
    line = file.readline() # 逐行讀入檔案
    if not line: break # 到最後一行時停止
    print(line, end = '') # 印出每一行
file.close() # 關閉檔案
