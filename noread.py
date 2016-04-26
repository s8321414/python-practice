import sys # 匯入 sys 模組
for line in open(sys.argv[1], 'r'): #將檔案設定為執行此 Python Script 後的第一個命令列參數，必須為檔案，且直接開啟檔案中的每一行
    print(line, end = '') # 印出每一行，最後一行以空白字元作結尾
