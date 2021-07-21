#讀取檔案
def 讀取檔案(filename):
	records = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			records.append(line.strip())
	return records

#處理檔案
def 處理檔案(records):
	處理後檔案 = []
	x = 3
	Allen_字數 = 0
	Allen_圖片 = 0
	Allen_貼圖 = 0
	Viki_字數 = 0
	Viki_圖片 = 0
	Viki_貼圖 = 0
	for line in records:
		s = line.split(' ')
		if len(s) >= 4:
			while len(s) != 3:
				s[2] = s[2] + s[x]
				s.remove(s[x])
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '圖片':
				Allen_圖片 = Allen_圖片 + 1
			elif s[2] == '貼圖':
				Allen_貼圖 = Allen_貼圖 + 1
			else:
				Allen_字數 = Allen_字數 + len(s[2]) 

		elif name == 'Viki':
			if s[2] == '圖片':
				Viki_圖片 = Viki_圖片 + 1
			elif s[2] == '貼圖':
				Viki_貼圖 = Viki_貼圖 + 1
			else:
				Viki_字數 = Viki_字數 + len(s[2]) 

	print ('Allen說了', Allen_字數, '字')
	print ('Allen傳了', Allen_圖片,'張圖片')
	print ('Allen傳了', Allen_貼圖,'張貼圖')
	print ('Viki說了', Viki_字數, '字')	
	print ('Viki傳了', Viki_圖片,'張圖片')
	print ('Viki傳了', Viki_貼圖,'張貼圖')


#寫出處理後程式
def 寫完檔案(filename, 處理後檔案):	
	with open(filename, 'w',encoding = 'utf-8-sig') as f:
		for line in 處理後檔案:
			f.write(line + '\n')


#主程式
def main():
	records = 讀取檔案('LINE-Viki.txt')
	處理後檔案 = 處理檔案(records)

	#寫完檔案('output自己寫2.txt', 處理後檔案)

main()