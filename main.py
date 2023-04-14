# coding:utf-8
'''
@version: python3
@author: ‘eric‘
@license: Apache Licence
@contact: steinven@qq.com
@software: PyCharm
@file: main.py.py
@time: 2023/4/14 14:27
'''
import json

import requests
import urllib3
from flask import Flask, request
from waitress import serve

urllib3.disable_warnings()

app = Flask(__name__)

latitude = "31.38475"
longitude = "120.98181"


@app.route('/4f5635c9-5a5e-4b17-8b4d-68d3b3d87c5a')
def my_follow_list():
    try:
        my_stName = request.args['my_stName']
        logger.debug('【my_stName】:%s'%my_stName)
        u = 'https://mini.wxposinda.com/api/UserAndLock/GetMapInfos'
        p = {
            "latitude": latitude,
            "longitude": longitude
        }
        h = {
            "Host": "mini.wxposinda.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
            "content-type": "application/json",
            "Referer": "https://servicewechat.com/wx2b5369075a2bxxxx/39/page-frame.html",
            "Accept-Encoding": "gzip, deflate, br"
        }
        '''
        {'id': 158, 'iconPath': '/Images/st_mark.png', 'latitude': 31.292701, 'longitude': 121.126683, 'totalNum': 28, 'stName': '徐公桥花园', 'bikeNum': 8, 'cityId': 4, 'lockEmptyNum': 20}
        '''
        r = requests.get(u, headers=h, params=p, verify=False)
        logger.debug('【response】:%s' % r.text)
        if my_stName == 'all':
            return json.loads(r.json()['content'])
        my_follow = [x for x in json.loads(r.json()['content']) if my_stName in str(x)]
        return my_follow
    except:
        logger.exception('')
        return 'server err!'


if __name__ == '__main__':
    import sys

    from loguru import logger

    app_name = 'query_ls_bike'
    logger.remove()

    logger.add(sys.stdout, level="INFO")  # WARNING/INFO/ERROR/DEBUG,控制台只会输出比该等级高的日志，但在文件日志中会全部写入
    log_name = "logs/%s-{time}.log" % app_name  # 配置文件路径，自动创建日志目录，{time}为内置变量，保证 日志文件的唯一性
    logger.add(log_name, encoding='utf-8', retention="10 days")

    serve(app, host='0.0.0.0', port=3212)