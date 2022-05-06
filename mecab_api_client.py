# import requests
# import json

# def get_url(url):
#     return requests.get(url)


# def post_url(url, sentence):
#     headers = {'Content-Type': 'application/json; charset=utf-8'}
#     body2 = {
#         "sentence": sentence
#     }

#     response = requests.request("POST", url, headers=headers,
#                                 data=json.dumps(body2, ensure_ascii=False).encode('utf-8'))
#     # print(response.text)
#     return response.text




# list_of_urls = ["http://127.0.0.1:5001/mecab"]*10

# for url in list_of_urls:
#     print(post_url(url, "머리가 아파요"))


import requests
import json
import datetime
from concurrent.futures import ThreadPoolExecutor
import time

def post_url(url):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    body2 = {
        "sentence": "머리가 아파요"
    }

    response = requests.request("POST", url, headers=headers,
                                data=json.dumps(body2, ensure_ascii=False).encode('utf-8'))
    # print(response.text)
    return response.text

# list_of_urls = ["http://127.0.0.1:5001/mecab"]*800
list_of_urls = ["http://3.35.128.86:5001/mecab"]*600


for i in range(1,51):
    start = datetime.datetime.now()
    with ThreadPoolExecutor(max_workers=2000) as pool:
        response_list = list(pool.map(post_url,list_of_urls))
    end = datetime.datetime.now()
    time.sleep(1)
    print("time : ",i,end-start)

# for response in response_list:
#     print(response)

# print("start time : {}",start)
# print("end time : {}",end)
# print("time : {}",end-start)
