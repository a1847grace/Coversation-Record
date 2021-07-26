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
	for line in records:
		if line[5:9] == 'Alle':
			處理後檔案.append(line[5:10])
		else:
			處理後檔案.append(line[5:9])
	print (處理後檔案)


#寫出處理後程式
def 寫完檔案(filename, 處理後檔案):	
	with open(filename, 'w',encoding = 'utf-8-sig') as f:
		for line in 處理後檔案:
			f.write(line + '\n')


#主程式
def main():
	records = 讀取檔案('3.txt')
	處理後檔案 = 處理檔案(records)

	#寫完檔案('output自己寫2.txt', 處理後檔案)

main()