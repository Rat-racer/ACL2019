from urllib.request import urlretrieve
import os
import pickle
import time
import requests


# class download(object):
#     """docstring for download"""
#     def __init__(self, arg):
#         super(download, self).__init__()
#         self.arg = arg
#     def self.getPaperDict():



def GetPaperDict():
    # res = requests.get('https://www.aclweb.org/anthology/events/acl-2019/')
    # with open('acl2019.htm','w') as f:
    #          f.write(res.text)
    #read acl2019.htm
    #extract titles , authors , and abstact
    #url pattern id unique number
    html = open('ACL2019.htm').read()
    out_dict = {}
    for paper_id in range(1001,1661):
        paper_head = html.find('href=/anthology/P19-'+str(paper_id)+'/>')
        paper_url = 'https://www.aclweb.org/anthology/P19-'+str(paper_id)
        pdf_url = 'https://www.aclweb.org/anthology/P19-'+str(paper_id)+'.pdf'
        html = html[paper_head:]
        paper_tail = html.find('class="d-sm-flex align-items-stretch"')
        paper_block = html[:paper_tail]
        abstract_head = paper_block.rfind('class="card-body p-3 small">')
        abstract = paper_block[abstract_head+28:-15]
        if paper_id ==1660:
            abstract = abstract[:abstract.find('</div>')]
        paper_title = paper_block[paper_block.find('/>')+2:paper_block.find('</a')]
        paper_title= paper_title.replace('<span class=acl-fixed-case>','').replace('</span>','')
        author_tail = paper_block.find('</a></span></p><div class="card bg-light mb-2 mb-lg-3 collapse abstract-collapse"')
        authors = paper_block[paper_block.find('/anthology/people/'):author_tail].split('</a>\n|\n<a href=')
        author_dict = {}
        for author in authors:
            author_name,author_home = author.split('>')[1], author.split('>')[0]
            author_dict[author_name] = author_home
        out_dict[paper_id] = [paper_url,paper_title,pdf_url,abstract,author_dict]
    pickle.dump(out_dict, open("papers.pickle", "wb"))
def download_pdfs():
    #download all ACL2019 papers to content directory
    paperdict = pickle.load(open( "papers.pickle", "rb" ))
    downloaded_pdfs = [int(x[:-4]) for x in os.listdir('content') if x.endswith('pdf')]
    for paper_id in range(1150,1250):#paperdict.keys():
        if paper_id not in downloaded_pdfs:
            pdf_url = paperdict[paper_id][2]
            start_time = time.time()
            try:
                urlretrieve(pdf_url,'content/'+str(paper_id)+'.pdf')
            except :
                raise       
            else:           
                pass
            end_time = time.time()
            print(str(end_time-start.time)+' seconds to downloading ',paper_id)
        downloaded_pdfs = [int(x[:-4]) for x in os.listdir('content') if x.endswith('pdf')]
    #some maybe inconsistent

if __name__ == '__main__':
    GetPaperDict()
    #download_pdfs()
