# prints all papers into file one per line with words separated by space, to be used with LDA




import pickle
topwords = pickle.load(open("topwords.pickle","rb"))
outf = open("allpapers.txt", "w")
for paperid in topwords.keys():
	words = topwords[paperid]
	words = [word[0] for word in words if word[1] > 3]
	outf.write(" ".join(words))
	outf.write("\n")
outf.close()

