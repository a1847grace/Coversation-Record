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
	Allen = 0
	Viki = 0
	for line in records:
		s = line.split(' ')
		if len(s) >= 4:
			while len(s) != 3:
				s[2] = s[2] + s[x]
				s.remove(s[x])
		time = s[0]
		name = s[1]
		if name == 'Allen':
			Allen = Allen + len(s[2]) 
			print ('Allen說了', Allen, '字')
		elif name == 'Viki':
			Viki = Viki + len(s[2])
			print ('Viki說了', Viki, '字')
	return 處理後檔案

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