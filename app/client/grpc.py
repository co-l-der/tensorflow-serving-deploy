#!/usr/bin/env python
# encoding: utf-8
import grpc
import tensorflow as tf
from tensorflow_serving.apis import prediction_service_pb2_grpc, predict_pb2

__author__ = "han"


def predict(input_x):
    """
    功能： 以grpc方式调模型服务, response内容难以解析, 建议使用restful方式调用
    :param input_x:
    :return:
    """

    channel = grpc.insecure_channel("localhost:8500")
    stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
    request = predict_pb2.PredictRequest()
    request.model_spec.name = "mnist-copy"
    request.inputs["input_x"].CopyFrom(
        tf.compat.v1.make_tensor_proto(input_x)
    )
    result = stub.Predict(request)
    print(result)
