from urllib.request import urlretrieve
import os
import pickle
import time

paperdict = pickle.load(open( "papers.pickle", "rb" ))
downloaded_pdfs = [int(x[:-4]) for x in os.listdir('content') if x.endswith('pdf')]
for paper_id in paperdict.keys():
	if paper_id not in downloaded_pdfs:
		print(paper_id)
		pdf_url = paperdict[paper_id][2]
		start_time = time.time()
		try:
			urlretrieve(pdf_url,'content/'+str(paper_id)+'.pdf')
		except :
			raise		
		else:			
			pass
		end_time = time.time()
		print(str(end_time-start_time)+' seconds to downloading ',paper_id)
	downloaded_pdfs = [int(x[:-4]) for x in os.listdir('content') if x.endswith('pdf')]