#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
  系统工具类
'''
import os

__author__ = 'daoyi'


def getSystemEnv(key, defaultValue):
    return os.getenv(key, defaultValue)


if __name__ == '__main__':
    print(getSystemEnv('systemEnvKey1', 'test'))
