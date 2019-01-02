import urllib.request
import csv
import json
import os

file_o = open('infile.txt', 'w')  # 書き込みモードでオープン

path = "../../docs/curation/8fe0cd41f53022eca27fc4c04229dfa2.json"

image_dir = "images"

file_i = open(path, 'r')
data = json.load(file_i)

selection = data["selections"][0]

members = selection["members"]

hash = selection["within"]["label"]

for i in range(len(members)):
  member = members[i]
  url = member["thumbnail"].replace(",300/0/", ",600/0/")
  path = image_dir + "/" + hash + "_" + str(i+1) + ".jpg"

  file_o.write(path + "\n")

  if not os.path.exists(path):
    urllib.request.urlretrieve(url, path)

file_i.close()
file_o.close()
