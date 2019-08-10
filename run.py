#!/usr/bin/env python
# encoding: utf-8

from app import Prediction

__author__ = "han"

if __name__ == "__main__":

    kw = dict(
        model_name="mnist-copy",
        version=3,
        channel="localhost:8500",
        domain="http://localhost:8501"
    )
    client = Prediction(**kw)
    result = client.predict_by_rest("test/test02.jpeg")
    print(result)
    result = client.predict_by_grpc("test/test02.jpeg")
    print(result)

