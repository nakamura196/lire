import uuid
import xml.etree.ElementTree as ET
import json
import xml.dom.minidom as md

path = "../../docs/curation/8fe0cd41f53022eca27fc4c04229dfa2.json"

file_i = open(path, 'r')
data = json.load(file_i)

selection = data["selections"][0]

members = selection["members"]

hash = selection["within"]["label"]

file_path2 = "template.xml"

tree2 = ET.parse(file_path2)
root2 = tree2.getroot()

for i in range(len(members)):
  member = members[i]
  url = member["thumbnail"]
  index = str(i+1)

  id = "https://nakamura196.github.io/lire/curation/" + hash + ".json#" + index

  file = "images/"+hash+"_"+index+".jpg_solr.xml"

  tree = ET.parse(file)
  root = tree.getroot()

  authorw = ET.Element("field")
  root.append(authorw)
  authorw.set("name", "imgurl")
  authorw.text = url

  root.find(".//field[@name='title']").text = "["+index+"]"
  root.find(".//field[@name='id']").text = id

  root2.append(root)

file_o = open('out.xml', 'w')  # 書き込みモードでオープン

document = md.parseString(ET.tostring(root2, 'utf-8'))

file_o.write(document.toprettyxml(indent="  "))

file_o.close()

#tree2.write("out.xml", encoding="utf-8")
