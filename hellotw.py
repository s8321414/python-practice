filename = input('檔名：')

file = open(filename, 'r', encoding='UTF-8')
content = file.read()
file.close()

print(content)                                 # 直接印出內容
print(content.encode('UTF-8'))                 # 以 UTF-8 編碼顯示
print(content.encode('UTF-8').decode('UTF-8')) # 先以 UTF-8 編碼後，再以 UTF-8 解碼後顯示
