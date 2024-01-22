# from flask import Flask, jsonify
# import os

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


# if __name__ == '__main__':
#     app.run(debug=True, port=os.getenv("PORT", default=5000))

from flask import Flask, request, jsonify
from flask_cors import CORS
import io, base64
from PIL import Image
import json
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {'origins': '*'}})

@app.route('/home')
def index():
    os.system("python detect.py --conf-thres=0.65 --weights ./runs/train/exp5/weights/best.pt --source ./555.jpg")
    f = open('Products.json')
    data = json.load(f)
    print(data)
    return jsonify(data)

@app.route('/imgpost', methods=['POST']) 
def foo():
    data = request.json

    img = Image.open(io.BytesIO(base64.decodebytes(bytes(data['data'], "utf-8"))))
    img.save('123123.jpg')

    # SOURCE DA CAMERA 
    # os.system("python detect.py --conf-thres=0.65 --weights ./runs/train/exp5/weights/best.pt --source ./123123.png")
    # os.system("python detect.py --second-run true --conf-thres=0.35 --weights ./runs/train/exp4/weights/best.pt")
    
    # SOURCE MOCADA, IMAGEM 555.jpg 
    
    os.system("python detect.py --conf-thres=0.65 --weights ./runs/train/exp5/weights/best.pt --source ./555.jpg")
    os.system("python detect.py --second-run true --conf-thres=0.65 --weights ./runs/train/exp4/weights/best.pt")

    f = open('Products.json')

    data = json.load(f)

    print(data)

    return data

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))


    # with open("imagessss.png", "wb") as fh:
    #     fh.write(base64.urlsafe_b64decode(data.data))
    # data = 'copy_your_raw_data_here'
    # you need to remove the prefix 'data:image/png;base64,'
    # bytes_decoded = base64.b64decode(data)
    # img = Image.open(BytesIO(bytes_decoded))
    # img.show()
    # # to jpg
    # out_jpg = img.convert("RGB")
    # # save file
    # out_jpg.save("saved_img.jpg")
# def image_processor():
#     json = {
#         'image1': 'teste'
#     }

#     return json
# detect("--conf-thres=0.65 --weights ./runs/train/exp5/weights/best.pt --source ./3.jpg")
