# -*- coding: utf-8 -*-
import base64
import hashlib
import hmac
import json
import os
import time
import requests
import urllib
from json_paser import parse, read_json

lfasr_host = 'https://raasr.xfyun.cn/v2/api'
# 请求的接口名
api_upload = '/upload'
api_get_result = '/getResult'


class RequestApi(object):
    def __init__(self, appid, secret_key, upload_file_path):
        self.appid = appid
        self.secret_key = secret_key
        self.upload_file_path = upload_file_path
        self.ts = str(int(time.time()))
        self.signa = self.get_signa()

    def get_signa(self):
        appid = self.appid
        secret_key = self.secret_key
        m2 = hashlib.md5()
        m2.update((appid + self.ts).encode('utf-8'))
        md5 = m2.hexdigest()
        md5 = bytes(md5, encoding='utf-8')
        # 以secret_key为key, 上面的md5为msg， 使用hashlib.sha1加密结果为signa
        signa = hmac.new(secret_key.encode('utf-8'), md5, hashlib.sha1).digest()
        signa = base64.b64encode(signa)
        signa = str(signa, 'utf-8')
        return signa

    def upload(self):
        # print("上传部分：")
        upload_file_path = self.upload_file_path
        file_len = os.path.getsize(upload_file_path)
        file_name = os.path.basename(upload_file_path)

        # 添加领域参数 pd
        param_dict = {'appId': self.appid,
                      'signa': self.signa,
                      'ts': self.ts,
                      "fileSize": file_len,
                      "fileName": file_name,
                      "duration": "200",
                      "pd": "life"}

        # print("[debug] upload参数：", param_dict)
        data = open(upload_file_path, 'rb').read(file_len)

        url = lfasr_host + api_upload + "?" + urllib.parse.urlencode(param_dict)
        response = requests.post(url=url, headers={"Content-type": "application/json"}, data=data)

        # print("upload_url:", url)
        result = json.loads(response.text)
        # print("[debug] upload resp:", result)
        return result

    def get_result(self) -> str:
        print("[info] {} upload start!".format(self.upload_file_path))
        uploadresp = self.upload()

        # 检测是否正常上传
        if uploadresp["code"] != '000000':
            print("[error] upload fail: ", uploadresp["descInfo"])
            return ""

        print("[info] {} upload success!".format(self.upload_file_path))
        print("[info] transcript start!")

        orderId = uploadresp['content']['orderId']
        param_dict = {}
        param_dict['appId'] = self.appid
        param_dict['signa'] = self.signa
        param_dict['ts'] = self.ts
        param_dict['orderId'] = orderId
        param_dict['resultType'] = "transfer,predict"
        # print("")
        # print("查询部分：")
        # print("get result参数：", param_dict)

        status = 3
        # 建议使用回调的方式查询结果，查询接口有请求频率限制
        while status == 3:
            response = requests.post(url=lfasr_host + api_get_result + "?" + urllib.parse.urlencode(param_dict),
                                     headers={"Content-type": "application/json"})
            # print("get_result_url:",response.request.url)
            result = json.loads(response.text)
            status = result['content']['orderInfo']['status']
            # print("status=", status)
            if status == 4:
                break
            time.sleep(5)
        # print("[debug] get_result resp:", result)
        print("[info] transcript success!")

        return result["content"]["orderResult"]


def print_result(result: dict):
    text = parse(result["content"]["orderResult"])
    print("Result: ", text)


# 读取配置文件
def read_config():
    config_path = "../config.json"

    config_json = read_json(config_path)

    return {
        "appid": config_json["appid"],
        "secret_key": config_json["secret_key"]
    }


# 输入讯飞开放平台的appid，secret_key和待转写的文件路径
def transcript(file_path: str):
    # file_path = "output/sound/2.wav"
    config = read_config()

    api = RequestApi(appid=config["appid"],
                     secret_key=config["secret_key"],
                     upload_file_path=file_path)

    # 返回订单结果的JSON
    order_result = api.get_result()
    # print_result(order_result)
    return order_result

