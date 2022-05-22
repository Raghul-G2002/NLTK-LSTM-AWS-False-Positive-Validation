import nltk
from nltk.corpus import words
from nltk.corpus import stopwords

words_list = words.words()
stop_words = list(stopwords.words('english'))
# print(len(words_list))
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in alphabets:
	try:
		words_list.remove(i)
	except:
		pass
# print(len(words_list))

for i in stop_words:
	try:
		words_list.remove(i)
	except ValueError:
		pass
# print(len(words_list))

for i in words_list:
	if(len(i) == 2 or len(i) == 3 or len(i) == 4):
		try:
			words_list.remove(i)
		except ValueError:
			pass
			
with open("new2.txt","w+") as f:
	for i in words_list:
		f.write("%s\n" % i)

## Test data can be given as a list to check the output