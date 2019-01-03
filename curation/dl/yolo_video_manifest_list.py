import sys
import argparse
from yolo_manifest import YOLO, detect_video
from PIL import Image
import requests
from io import BytesIO
import os
import urllib.request
import json
import csv
from hashlib import md5


def detect_img(yolo):
    res = urllib.request.urlopen(manifest)
    # json_loads() でPythonオブジェクトに変換
    data = json.loads(res.read().decode('utf-8'))

    canvases = data["sequences"][0]["canvases"]

    # A005935-01のようなIDを取得する
    cn = data["@id"].split("/")[5]

    for i in range(0, len(canvases)):
        canvas = canvases[i]
        # []を削除する
        label = canvas["label"].replace("[", "").replace("]", "")
        img_url = canvas["images"][0]["resource"]["service"]["@id"] + "/full/,600/0/default.jpg"

        try:
            response = requests.get(img_url)
            image = Image.open(BytesIO(response.content))
        except:
            print('Open Error! Try again!')
            # continue
        else:
            r_image, result = yolo.detect_image(image)
            filename = str(i).zfill(3) + ".jpg"
            print(filename)
            r_image.save(output_dir + "/" + filename)

            if len(result) > 0:

                for obj in result:
                    list = []
                    list.append(i)
                    list.append(obj["x"])
                    list.append(obj["y"])
                    list.append(obj["w"])
                    list.append(obj["h"])
                    list.append(obj["score"])
                    list.append(manifest)

                    writer.writerow(list)


FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

    FLAGS = parser.parse_args()

    FLAGS.image = True

    fi = open("output/manifest_list.csv", 'r')

    reader = csv.reader(fi)
    header = next(reader)
    for row in reader:
        num = row[0]
        manifest = row[1]
        hash = md5(manifest.encode('utf-8')).hexdigest()

        output_dir = "output/" + num + "_" + hash
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        f = open(output_dir + "/list.csv", 'w')

        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(["index", "x", "y", "w", "h", "score", "manifest"])

        detect_img(YOLO(**vars(FLAGS)))

        f.close()

    fi.close()
    yolo.close_session()
