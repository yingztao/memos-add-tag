import os
import requests
from flask import Flask, request

app = Flask(__name__)

API_KEY = 'your_api_key' # 用于验证的 API key

@app.route('/', methods=['POST'])
def receive_data():
    api_key = request.args.get('api_key') # 获取请求参数中的 API key
    if api_key != API_KEY: 
        return 'Unauthorized', 401  # 如果 API key 不正确，返回 401 Unauthorized

    data = request.get_json()
    content_value = data['content'] + ' #交易记录'

    url = f'https://memos.yingz.cc:1121/api/memo?openId={api_key}'

    headers = {'Content-Type': 'application/json'}
    payload = {'content': content_value}
    response = requests.post(url, headers=headers, json=payload)

    print(response.status_code, response.content)
    
    return '' 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
