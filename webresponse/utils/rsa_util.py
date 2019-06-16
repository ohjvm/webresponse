#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
 RSA 工具类
 证书使用pkcs1
'''

from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from io import BytesIO
from Crypto.PublicKey import RSA
import base64

from webresponse.constants import system_constants

__author__ = 'daoyi'


def rsa_sign_with_path(content, key_path):
    signature = ''
    try:
        signature = rsa_sign(content, _load_key_file(key_path))
    except Exception as err:
        print('导入rsa私钥出错', key_path, err)
    return signature


def rsa_sign(content, private_key):
    '''
    生成签名
    :param content: 待生成签名内容
    :param private_key: 私钥
    :return: 签名
    '''
    signature = ''
    try:
        h = SHA256.new(content.encode('UTF-8'))
        signature = pkcs1_15.new(private_key).sign(h)
    except Exception as err:
        print('rsa加签出错', err)
    return base64.b64encode(signature).decode(system_constants.DEFAULT_CHARSET)


def rsa_verify_with_path(content, sign, key_path):
    try:
        return rsa_verify(content, sign, _load_key_file(key_path))
    except Exception as err:
        print('导入rsa私钥出错', key_path, err)
    return False


def rsa_verify(content, sign, public_key):
    '''
    验证签名
    :param content: 待验签内容
    :param sign: 签名
    :param public_key: 公钥
    :return: 验签结果
    '''
    try:
        h = SHA256.new(content.encode(system_constants.DEFAULT_CHARSET))
        pkcs1_15.new(public_key).verify(h, base64.b64decode(sign.encode(system_constants.DEFAULT_CHARSET)))
        return True
    except Exception as err:
        print('rsa验签出错', err)
    return False


def _load_key_file(key_path):

    with open(key_path, 'rb') as input_stream:
        bytes = BytesIO()
        buff = input_stream.read(10)
        i = 0
        while len(buff) > 0:
            bytes.write(buff)
            buff = input_stream.read(10)
            i = i + 1
        return RSA.import_key(bytes.getvalue())


if __name__ == '__main__':
    signature = rsa_sign_with_path('1233', '/Users/Mark/Projects/Documenmts/certificate/demo/private_key_pkcs1.pem')
    print('生成的签名为：%s' % signature)
    base64.b64encode(signature.encode())
    verify_result = rsa_verify_with_path('1233', signature,
                               '/Users/Mark/Projects/Documenmts/certificate/demo/rsa_public_key.pem')
    print('验签结果：', verify_result)
