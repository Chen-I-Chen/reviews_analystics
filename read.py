data = []
count = 0
with open('reviews.txt', 'r') as x:
	for line in x:
		data.append(line)

sum_string = 0
for word in data: #檢視DATA中的每一筆資料
	sum_string = sum_string + len(word) #輪到下一行評論字數時，跟前面的總和加在一起
	answer = sum_string/len(data)
print('留言的平均長度為', answer)