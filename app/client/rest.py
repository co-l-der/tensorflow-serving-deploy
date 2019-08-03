#!/usr/bin/env python
# encoding: utf-8
import json
import numpy as np
import requests

__author__ = "han"


def predict(input_x):

    payload = {
        "instances": [{"input_x": input_x.tolist()}]
    }
    response = {}
    try:
        # TODO: 模型服务版本如何控制
        req = requests.post("http://localhost:8501/v1/models/mnist-copy:predict", json=payload)

        response = json.loads(req.content.decode())
    except Exception:
        # 抛请求出错异常
        print("error!")
        return

    result = response.get("predictions", None)

    if not result:
        # 抛没有结果异常
        print(response)
        return

    result = np.array(result).flatten()
    result = result.tolist()
    result = result.index(max(result))
    print(result)
