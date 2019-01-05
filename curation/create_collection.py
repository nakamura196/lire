import json
import urllib.request
import csv
from hashlib import md5


fi = open("data/manifest_list2.csv", 'r')

filename = "kunshujo"

manifests = []

collection = dict()
collection["@context"] = "http://iiif.io/api/presentation/2/context.json"
collection["@id"] = "https://nakamura196.github.io/lire/collection/"+filename+".json"
collection["@collection_name"] = "sc:Collection"
collection["manifests"] = manifests

output_path = "../docs/collection/"+filename+".json"

reader = csv.reader(fi)
header = next(reader)
for row in reader:
    num = row[0]
    manifest_uri = row[1]
    hash = md5(manifest_uri.encode('utf-8')).hexdigest()

    manifest_obj = dict()
    manifests.append(manifest_obj)
    manifest_obj["@id"] = "https://nakamura196.github.io/lire/annotation/" + hash + ".json"
    manifest_obj["@collection_name"] = "sc:Manifest"

    response = urllib.request.urlopen(manifest_uri)
    response_body = response.read().decode("utf-8")
    data = json.loads(response_body)

    manifest_obj["label"] = data["label"]

fw = open(output_path, 'w')
json.dump(collection, fw, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
