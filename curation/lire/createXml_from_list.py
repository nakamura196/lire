import csv
from hashlib import md5
import xml.etree.ElementTree as ET
import json
import xml.dom.minidom as md

fi = open("../data/manifest_list.csv", 'r')

reader = csv.reader(fi)
header = next(reader)

file_path2 = "template.xml"

tree2 = ET.parse(file_path2)
root2 = tree2.getroot()

for row in reader:
  manifest_uri = row[1]
  hash = md5(manifest_uri.encode('utf-8')).hexdigest()

  path = "../../docs/curation/" + hash + ".json"

  file_i = open(path, 'r')
  data = json.load(file_i)

  selection = data["selections"][0]

  members = selection["members"]

  hash = selection["within"]["label"]

  for i in range(len(members)):
    member = members[i]
    url = member["thumbnail"]
    index = str(i + 1)

    id = "https://nakamura196.github.io/lire/curation/" + hash + ".json#" + index

    file = "images/" + hash + "_" + index + ".jpg_solr.xml"

    tree = ET.parse(file)
    root = tree.getroot()

    authorw = ET.Element("field")
    root.append(authorw)
    authorw.set("name", "imgurl")
    authorw.text = url

    root.find(".//field[@name='title']").text = "[" + index + "]"
    root.find(".//field[@name='id']").text = id

    root2.append(root)

file_o = open('out.xml', 'w')  # 書き込みモードでオープン

document = md.parseString(ET.tostring(root2, 'utf-8'))

file_o.write(document.toprettyxml(indent="  "))

file_o.close()
