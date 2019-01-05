import urllib.request
import json
from hashlib import md5
import csv


def create_anno(text, tags, canvas_id, area, color, manifest, anno_uri):
  resource = dict()

  resource["@context"] = "http://iiif.io/api/presentation/2/context.json"
  resource["@type"] = "oa:Annotation"
  resource["motivation"] = "oa:commenting"
  resource["resource"] = []

  r = dict()
  resource["resource"].append(r)

  r["@type"] = "dctypes:Text"
  r["format"] = "text/html"
  r["chars"] = text

  for tag in tags:
    r = dict()
    resource["resource"].append(r)
    r["@type"] = "oa:Tag"
    r["chars"] = tag

  on = dict()
  resource["on"] = []
  resource["on"].append(on)

  on["@type"] = "oa:SpecificResource"

  on["full"] = canvas_id
  selector = dict()
  selector["@type"] = "oa:Choice"

  default = dict()
  default["@type"] = "oa:FragmentSelector"

  default["value"] = "xywh=" + area
  selector["default"] = default

  item = dict()
  item["@type"] = "oa:SvgSelector"

  xywh = area.split(",")
  x = xywh[0]
  y = xywh[1]
  dx = xywh[2]
  dy = xywh[3]

  max_x = int(x) + int(dx)
  max_y = int(y) + int(dy)

  d = "M" + str(max_x) + "," + str(max_y) + "h-" + str(dx) + "v-" + str(dy) + "h" + str(dx) + "v" + str(
    int(dy) / 2) + "z"

  item["value"] = "<svg xmlns='http://www.w3.org/2000/svg'>" \
                  "<path " \
                  "xmlns=\"http://www.w3.org/2000/svg\" " \
                  "d=\"" + d + "\" " \
                               "data-paper-data=\"{&quot;strokeWidth&quot;:1,&quot;rotation&quot;:0,&quot;annotation&quot;:null,&quot;nonHoverStrokeColor&quot;:[&quot;Color&quot;,0,0.74902,1],&quot;editable&quot;:true,&quot;deleteIcon&quot;:null,&quot;rotationIcon&quot;:null,&quot;group&quot;:null}\" " \
                               "id=\"rectangle_62389b77-19f2-4d12-aa7c-0ca7c788b5c3\" " \
                               "fill-opacity=\"0.2\" " \
                               "fill=\"" + color + "\" " \
                                                   "fill-rule=\"nonzero\" " \
                                                   "stroke=\"" + color + "\" " \
                                                                         "stroke-width=\"121.89861\" " \
                                                                         "stroke-linecap=\"butt\" " \
                                                                         "stroke-linejoin=\"miter\" " \
                                                                         "stroke-miterlimit=\"10\" " \
                                                                         "stroke-dasharray=\"\" " \
                                                                         "stroke-dashoffset=\"0\" " \
                                                                         "font-family=\"none\" " \
                                                                         "font-weight=\"none\" " \
                                                                         "font-size=\"none\" " \
                                                                         "text-anchor=\"none\" " \
                                                                         "style=\"mix-blend-mode: normal\"/>" \
                                                                         "</svg>"
  selector["item"] = item

  on["selector"] = selector

  within = dict()
  within["@id"] = manifest
  within["@type"] = "sc:Manifest"

  on["within"] = within

  resource["@id"] = anno_uri

  return resource


def read_curation(curation_json_path):
  file = open(curation_json_path, 'r')
  data = json.load(file)

  selection = data["selections"][0]

  members = selection["members"]

  canvases = dict()

  for i in range(len(members)):
    member = members[i]

    uri = member["@id"]
    tmp = uri.split("#")
    canvas_id = tmp[0]
    area = tmp[1].split("=")[1]

    label = member["label"]

    if canvas_id not in canvases:
      canvases[canvas_id] = []

    arr = canvases[canvas_id]

    obj = dict()
    obj["label"] = label
    obj["area"] = area
    arr.append(obj)

  file.close()

  return canvases


def create_annotation_list(canvas_id, index):
  al = dict()
  al["@id"] = oc["@id"]
  al["@context"] = "http://www.shared-canvas.org/ns/context.json"
  al["@type"] = "sc:AnnotationList"

  resources = []
  al["resources"] = resources

  if canvas_id in curations:

    anno_list = curations[canvas_id]

    for anno in anno_list:
      # def create_anno(text, tags, canvas_id, area, color, manifest, anno_uri):
      resources.append(create_anno(anno["label"], [], canvas_id, anno["area"], "red", manifest_uri, oc["@id"]))

  with open("../docs/annotation/anno_list/" + hash + "_" + index + ".json", 'w') as outfile:
    json.dump(al, outfile, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


fi = open("data/manifest_list2.csv", 'r')

reader = csv.reader(fi)
header = next(reader)

for row in reader:
  manifest_uri = row[1]
  print(manifest_uri)

  response = urllib.request.urlopen(manifest_uri)
  response_body = response.read().decode("utf-8")
  data = json.loads(response_body)
  canvases = data["sequences"][0]["canvases"]

  hash = md5(manifest_uri.encode('utf-8')).hexdigest()

  new_uri = "https://nakamura196.github.io/lire/annotation/" + hash + ".json"
  data["@id"] = new_uri

  curations = read_curation("../docs/curation/" + hash + ".json")

  for i in range(len(canvases)):
    index = str(i + 1)

    canvas = canvases[i]

    canvas_id = canvas["@id"]

    otherContent = []
    oc = dict()
    otherContent.append(oc)
    oc["@id"] = "https://nakamura196.github.io/lire/annotation/anno_list/" + hash + "_" + index + ".json"
    oc["@type"] = "sc:AnnotationList"
    canvas["otherContent"] = otherContent

    create_annotation_list(canvas_id, index)

  with open("../docs/annotation/"+hash+".json", 'w') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
