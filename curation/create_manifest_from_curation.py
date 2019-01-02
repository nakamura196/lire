import json
import urllib.request
import csv


def format_size(a):
  a = int(a)
  a = int(a * r)
  return str(a)


def get_yolo_list(path):
  with open(path, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダーを読み飛ばしたい時

    for row in reader:
      obj = dict()
      obj["index"] = row[0]
      obj["x"] = row[1]
      obj["y"] = row[2]
      obj["w"] = row[3]
      obj["h"] = row[4]
      obj["score"] = row[5]
      yolo_list.append(obj)


def get_canvases(manifest_uri):
  response = urllib.request.urlopen(manifest_uri)
  response_body = response.read().decode("utf-8")
  data = json.loads(response_body)
  canvases_ = data["sequences"][0]["canvases"]

  for canvas in canvases_:
    obj = dict()
    canvas_id = canvas["@id"]
    height = canvas["images"][0]["resource"]["height"]
    obj["canvas_id"] = canvas_id
    obj["h"] = height
    obj["image_api"] = canvas["images"][0]["resource"]["service"]["@id"]
    canvases.append(obj)


canvases = []

num = "2"
hash = "8fe0cd41f53022eca27fc4c04229dfa2"
manifest_uri = "https://www.dl.ndl.go.jp/api/iiif/2586693/manifest.json"

get_canvases(manifest_uri)

yolo_list = []

path = "/Users/satoru/git/keras-yolo3/output/" + num + "_" + hash + "/list.csv"

get_yolo_list(path)

rate = 600

with open('data/template.json') as f:
  df = json.load(f)

df["selections"] = []

selection = {}
df["selections"].append(selection)

df["@id"] = "https://nakamura196.github.io/lire/curation/" + hash + ".json"
selection["@id"] = df["@id"] + "/range" + str(1)

selection["@type"] = "sc:Range"
selection["label"] = "Manual curation by IIIF Curation Viewer"

manifest = dict()
selection["within"] = manifest
manifest["@id"] = manifest_uri
manifest["@type"] = "sc:Manifest"
manifest["label"] = hash

selection["members"] = []


for i in range(len(yolo_list)):
  obj = yolo_list[i]
  index = int(obj["index"])

  canvas = canvases[index]
  canvas_id = canvas["canvas_id"]
  h = canvas["h"]
  r = h / rate

  member = {}

  selection["members"].append(member)

  area = format_size(obj["x"]) + "," + format_size(obj["y"]) + "," + format_size(
    obj["w"]) + "," + format_size(obj["h"])

  member["@id"] = canvas_id + "#xywh=" + area
  member["@type"] = "sc:Canvas"
  member["label"] = "["+str(i+1)+"]"
  member["thumbnail"] = canvas["image_api"]+"/"+area+"/,300/0/default.jpg"

  metadata = []
  member["metadata"] = metadata

  m = {}
  metadata.append(m)
  m["label"] = "Score"
  m["value"] = obj["score"]

with open("../docs/curation/" + hash + ".json", 'w') as outfile:
  json.dump(df, outfile, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
