#!/usr/bin/env python
# encoding: utf-8
from enum import Enum

__author__ = "han"


class Flag(Enum):
    # 使用restful方式调用模型服务
    REST = "restful"
    # 使用grpc方式调用模型服务
    GRPC = "grpc"

