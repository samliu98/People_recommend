# -*- coding : utf-8 -*-
import re
import jieba
from collections import Counter

with open('stops.txt', 'r') as f:
	stops = f.read().split('\n')

stops.append('\n')
stops.append('[')
stops.append(']')
stops.append(' ')
done = []
data = dict()

youtubers = ['subtitles/A_Di_English.txt', 'subtitles/CYFIT.txt', 'subtitles/Dodo_Village.txt', 'subtitles/Empty_Bottle_King.txt',
'subtitles/Gamker.txt', 'subtitles/Hello_Catie.txt', 'subtitles/Huan.txt', 'subtitles/Little_Hot_Sing.txt',
'subtitles/Lulu.txt', 'subtitles/Table_Games_Taichung.txt']
# with open('text/CYFIT.txt', 'r') as input:
for youtuber in youtubers:
	temp = youtuber.split('/')
	print(temp)
	data[temp[1]] = []
	with open(youtuber) as input1:
		
		# item_now = ''
		for i, item in enumerate(input1):
			data[temp[1]] += [t for t in jieba.cut_for_search(item) if t not in stops]
			# if re.match(r'(.*?).wav', item):
			# 	#print(item)
			# 	item_now = item.strip()
			# 	data[item_now] = [t for t in jieba.cut_for_search(item) if t not in stops] + [t for t in jieba.cut_for_search(item) if t not in stops]
			# 	#print(data)
			# else:
			# 	#print(item)
			# 	data[item_now] += [t for t in jieba.cut_for_search(item) if t not in stops]
				#terms = [t for t in jieba.cut_for_search(item) if t not in stops]
			# print(sorted(Counter(terms).items(), key=lambda x:x[1], reverse=True))
				#print(data)
				#break
			# if(terms != []):
				# done += terms
	# for key in data:
	# 	path = 'documents_movie/' + key + '.txt'
	# 	with open(path, 'w', encoding='utf8') as out:
	# 		# doc = key + '\n'
	# 		doc = ''
	# 		for word in data[key]:
	# 			if not re.match(r'[\u4E00-\u9FBF]+', word):
	# 				continue
	# 			doc = doc + word + ' '
	# 		#print(doc)
	# 		out.write(doc)

	# print(len(data))
for key in data:
	path = 'documents_youtubers/' + key
	print(path)
	with open(path, 'w', encoding='utf8') as out:
		doc = ''
		for word in data[key]:
			if not re.match(r'[\u4E00-\u9FBF]+', word):
				continue
			doc = doc + word + ' '
		out.write(doc)
# print(done)


#print(sorted(Counter(done).items(), key=lambda x:x[1], reverse=True))