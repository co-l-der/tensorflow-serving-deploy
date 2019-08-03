#!/usr/bin/env python
# encoding: utf-8

import cv2

from client.constant import Flag

__author__ = "han"


def img_to_mnist_input(img_path, serving_type=Flag.REST.value):
    """
    功能： 将image抓换成模型可识别的输入
    :param img_path:
    :param serving_type:
    :return:
    """
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
    img = cv2.bitwise_not(img)
    # 注意这里的输入和keras输入不一样, keras shape(1,28,28,1)分别代表样本数量, 像素28*28, 通道
    # 而tensorflow shape(28,28,1)分别代表像素28*28, 通道
    # TODO： why?
    if serving_type == Flag.REST.value:
        img = img.reshape((28, 28, 1))
    elif serving_type == Flag.GRPC.value:
        img = img.reshape((1, 28, 28, 1))

    img = img.astype("float32")
    standard_input = img/255
    return standard_input

