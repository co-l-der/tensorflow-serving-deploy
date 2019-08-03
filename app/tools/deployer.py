#!/usr/bin/env python
# encoding: utf-8
import os

import tensorflow as tf
from keras import Model as keras_model
from tensorflow.python.keras import Model as tf_keras_model
from tensorflow.python.keras.engine.training import Model as keras_train_model

__author__ = "han"


def export_tensorflow_serving_model(model, version=0, export_path=None):
    """
    功能： 将keras训练保存的.h5 model转换成tensorflow serving可部署的模型
    :param model: 模型路径或已经加载的Model
    :param version:
    :param export_path:
    :return:
    """

    # The learning phase flag is a bool tensor (0 = test, 1 = train)
    tf.keras.backend.set_learning_phase(0)
    if isinstance(model, str) and model.endswith(".h5"):
        load_model = tf.keras.models.load_model(model)
    elif isinstance(model, (tf_keras_model, keras_model, keras_train_model)):
        load_model = model
    else:
        print("model can not be parsed.")
        return

    if not export_path and isinstance(model, str):
        export_path = os.path.join(tf.compat.as_bytes(os.path.dirname(model)),
                                   tf.compat.as_bytes(str(version)))
    elif not export_path and isinstance(model, (tf_keras_model, keras_model, keras_train_model)):
        print("export path can not be none.")
        return
    else:
        export_path = os.path.join(tf.compat.as_bytes(export_path),
                                   tf.compat.as_bytes(str(version)))

    with tf.keras.backend.get_session() as sess:
        tf.saved_model.simple_save(
            sess,
            export_path,
            inputs={"input_x": load_model.input},
            outputs={t.name: t for t in load_model.outputs}
        )


if __name__ == "__main__":
    export_tensorflow_serving_model(model="../../models/mnist.h5",
                                    version=2)
