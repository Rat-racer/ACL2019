import os

pdfs = [x for x in os.listdir('content') if x.endswith(".pdf")]
thumbs = [x[:-4]for x in os.listdir('thumbs') if x.endswith(".jpg")]
for pdf in pdfs:
	if pdf[:-4] in thumbs:
		continue
	fullpath = 'content/' + pdf
	print("thumbing",pdf)
	# this is a mouthful... 
	# take first 8 pages of the pdf ([0-7]), since 9th page are references
	# tile them horizontally, use JPEG compression 80, trim the borders for each image
	# colorspace was added because a few PDFs displayed with a black background
	cmd = "montage %s[0-7] -mode Concatenate -colorspace sRGB -tile x1 -quality 80 -resize x345 -trim %s" % (fullpath, "thumbs/" + pdf[:-4] + ".jpg")
	#print("EXEC: " + cmd)
	os.system(cmd)






	