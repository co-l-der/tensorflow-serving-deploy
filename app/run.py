#!/usr/bin/env python
# encoding: utf-8
from client import rest, grpc
from tools import converter

__author__ = "han"

if __name__ == "__main__":

    input_x = converter.img_to_mnist_input("../test/test02.jpeg", serving_type="restful")
    rest.predict(input_x)
    input_x = converter.img_to_mnist_input("../test/test02.jpeg", serving_type="grpc")
    grpc.predict(input_x)
