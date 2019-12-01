import re
import os
import collections
import pickle


stopwords = open('stopwords.txt').readlines()
stopwords = [word.strip() for word in stopwords]
N = 100
topwords = {}
pdfs = ['content/' + x for x in os.listdir("content") if x.endswith(".pdf")]  #all paper
#pdfs = ['content/'+str(i)+'.pdf' for i in range(1001,1101)]   # a subset ,for test
for pdf in pdfs:
	paper_id = int(pdf.split('/')[1].split('.')[0])
	cmd = 'pdftotext ' + pdf + ' out.txt'
	os.system(cmd)
	txt = open("out.txt").read().lower().split()
	words = [x for x in  txt if re.match('^[\w-]+$', x) is not None]  
	words = [x for x in words if len(x)>2 and (not x in stopwords)]
	counter = collections.Counter(words).most_common(N)
	sorted_counter = sorted(counter,key=lambda x:x[1],reverse= True)
	topwords[paper_id] = sorted_counter
pickle.dump(topwords,open("topwords.pickle","wb"))


python3 lda.py -f allpapers.txt -k 7 --alpha=0.5 --beta=0.5 -i 10 