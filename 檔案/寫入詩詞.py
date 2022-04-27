file1 = open('poem.txt', 'a+')
file1.write('靜夜思')
file1.write('\n床前明月光，')
file1.write('\n疑是地上霜。')
file1.write('\n舉頭望明月，')
file1.write('\n低頭思故鄉。')
file1.flush() # 缓冲?

file1.seek(0) # 重頭開始讀
print(file1.readlines())
file1.close()