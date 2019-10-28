# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 15:02
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com

import requests
import json

# f = open("demo2.json","r", encoding="utf-8")  # 文件中有中文需要指定编码
# f_dict = json.load(f) # 反序列化将文件句柄转化为字典
# print(f_dict['url']) # 读取其中参数
#
#
# #res = requests.post(url=json.dump(f_dict)
# res = requests.request('post',url=f_dict['url'],data=json.dumps(f_dict['data']))
# f.close()
# print(json.loads(res.text))
import requests
import json

app_key = 'kPoFYw85FXsnojsy5bB9hu6x'
secret_key = 'l7SuGBkDQHkjiTPU3m6NaNddD6SCvDMC'
img_url = 'http://upload-images.jianshu.io/upload_images/7575721-40c847532432e852.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
# 获取token
get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(app_key,secret_key)
print(get_token_url)
token = requests.get(url=get_token_url).json().get("access_token")  # 从获取token接口的响应中取得token值
# 识别图片文字
orc_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token={}'.format(token)
data = {"url": img_url}
res = requests.post(url=orc_url, data=data)
print(json.dumps(res.json(), indent=2, ensure_ascii=False)) # 格式化输出
