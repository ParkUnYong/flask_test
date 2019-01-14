from flask import Flask, render_template, request
import json
import sys
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/park',methods = ['POST'])
def name():
    data = {'name' : 'wangtwo Lee','age' : 25}
    result = json.dumps(data)
    return result

@app.route('/describe_image',methods=['POST'])
def describe_image():
    data = request.data
    image_url = data.decode('utf-8')
    described_text = use_describe_image_api(image_url)
    return described_text


def use_describe_image_api(image_url):
    params = {
       'visualFeatures': 'Description',
       'language': 'en'
             }

##https://[location].api.cognitive.microsoft.com/vision/v1.0/analyze[?visualFeatures][&details][&language]
## 이런식으로 옵션 넣어줘야함. 비주얼 퓨처로 
    headers = {
    # Request headers
       'Content-Type': 'application/json', ## 제이슨 쓰니까 제이슨임 아니면 바꿔줘야함.
       'Ocp-Apim-Subscription-Key': '12e457e85bb8497d88333dae3fb8d759', ## 에저 클라우드에서 이걸 지원해줘서 쓰는것.
    }

    data = {
        'url':image_url
    ## 이미지 부분임.
    }

    res = requests.post('https://koreacentral.api.cognitive.microsoft.com/vision/v1.0/analyze',
                            params= params, headers=headers, json =data)


    res_dict = json.loads(res.text)
    subscribed_text = res_dict['description']['captions'][0]['text']
    return subscribed_text



if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)

