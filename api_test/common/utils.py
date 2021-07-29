#!/usr/bin/python
# -*- coding:utf-8 _*- 
"""
@author:TXU
@file:utils.py
@time:2021/07/29
@email:xutao@dustess.com
@description:
"""
import hashlib
import hmac
from base64 import b64encode

from api_test.config.DingConfig import APPSECRET


def signature(code):
    """
    hmacsha256算法
    :param code:
    :return:
    """
    app_key = APPSECRET  # miyao

    # hmac_sha256加密
    sgn = hmac.new(bytes(app_key, encoding='utf-8'), bytes(code, encoding='utf-8'),
                         digestmod=hashlib.sha256).digest()

    # 二进制转为HEX
    _hex = str(b64encode(sgn), encoding='utf-8')
    return _hex


if __name__ == '__main__':
    print(signature('1234567890123'))
