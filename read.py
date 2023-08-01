data = []
count = 0
with open('reviews.txt', 'r') as x:
	for line in x:
		data.append(line)
		count += 1
		if count % 1000 == 0: #讓數量每隔1000筆印一次
			print(len(data))

print(data[0])
print('-----------') #分隔線
print(data[1])