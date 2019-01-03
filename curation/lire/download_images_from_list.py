import urllib.request
import csv
import json
import os
from hashlib import md5

file_o = open('infile.txt', 'w')  # 書き込みモードでオープン

fi = open("../data/manifest_list2.csv", 'r')

image_dir = "images"

reader = csv.reader(fi)
header = next(reader)
for row in reader:
    manifest_uri = row[1]
    print(manifest_uri)

    hash = md5(manifest_uri.encode('utf-8')).hexdigest()

    path = "../../docs/curation/"+hash+".json"

    file_i = open(path, 'r')
    data = json.load(file_i)

    selection = data["selections"][0]

    members = selection["members"]

    for i in range(len(members)):
      member = members[i]
      url = member["thumbnail"].replace(",300/0/", ",600/0/")
      path = image_dir + "/" + hash + "_" + str(i+1) + ".jpg"

      file_o.write(path + "\n")

      if not os.path.exists(path):
        urllib.request.urlretrieve(url, path)

    file_i.close()
file_o.close()
