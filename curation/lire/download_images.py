import urllib.request

import csv

file = open('infile.txt', 'w')  #書き込みモードでオープン

curation_uri = "https://mp.ex.nii.ac.jp/api/curation/json/9231722d-d609-452c-94b8-cde14eb2afef"



with open('../data/member.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        url = row[1]
        name = row[0]

        path = "images/"+name+".jpg"

        file.write(path+"\n")

        '''
        if not os.path.exists(path):

            urllib.request.urlretrieve(url.replace(",300", ",600"), path)
        '''

file.close()
