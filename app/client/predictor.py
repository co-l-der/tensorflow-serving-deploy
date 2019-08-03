#!/usr/bin/env python
# encoding: utf-8
import json

import requests

import grpc
import tensorflow as tf
from tensorflow_serving.apis import prediction_service_pb2_grpc, predict_pb2

__author__ = "han"


class Prediction(object):

    def __init__(self, **kwargs):
        self.model_name = kwargs.get("model_name", None)
        self.version = kwargs.get("version", "v1")
        self.channel = kwargs.get("channel", None)
        self.domain = kwargs.get("domain", None)

    def predict_by_rest(self, input_x):
        """
        功能： 通过restful方式调用tensorflow serving模型服务
        :param input_x: 模型输入
        :return: 模型输出
        """
        if not self.domain:
            raise Exception("domain can not be none")
        if not self.model_name:
            raise Exception("model_name can not be none")

        # domain 如： ”http://localhost:8501“
        url = "{domain}/{version}/models/{model_name}:predict".format(
            domain=self.domain,
            version=self.version,
            model_name=self.model_name
        )

        payload = {
            "instances": [{"input_x": input_x.tolist()}]
        }
        try:
            req = requests.post(url, json=payload)
            response = json.loads(req.content.decode())
        except Exception:
            raise Exception("request encounted an error.")

        result = response.get("predictions", None)

        if not result:
            # 抛没有结果异常
            print(response)
            raise Exception("can not get predictions")

        return result

    def predict_by_grpc(self, input_x):
        """
        功能: 通过grpc方式调用tensorflow serving模型服务
        :param input_x: 模型输入
        :return:
        """
        if not self.channel:
            raise Exception("channel can not be none.")
        if not self.model_name:
            raise Exception("model_name can not be none.")
        # channel 如 "localhost:8500"
        channel = grpc.insecure_channel(self.channel)
        stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
        request = predict_pb2.PredictRequest()
        request.model_spec.name = self.model_name
        request.inputs["input_x"].CopyFrom(
            tf.compat.v1.make_tensor_proto(input_x)
        )
        result = stub.Predict(request)

        # TODO： result需层层解析

        return result

