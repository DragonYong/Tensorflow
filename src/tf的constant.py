#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2021-10-31 17:01
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    tf的constant.py
# @Project: Tensorflow
# @Package:

import tensorflow as tf

t = tf.constant([[1, 2, 3], [4, 5, 6]])
print(t)


print(t+10)

tf.square(t)

print(t.numpy())
