import sys # 匯入 sys 模組
file = open(sys.argv[1], 'w') # 將檔案設定為隨後的第一個參數，並設定為擁有寫入權限
file.write('test') # 寫入檔案
file.close() # 關閉檔案
