#### 项目描述

一、 通过tensorflow saved_model转换由keras训练的模型

二、 使用tensorflow serving部署转换后的mnist模型

三、 说明：

    1. tesorflow serving目前仅支持由tensorflow训练，由tf.saved_model保存的格式为pb的模型
    
    3. tensorflow和keras保存模型的机制不同，前者采用protobuf协议序列化模型结构与参数，后者采用HDF5技术保存模型
    
    2. tensorflow 2.0将推出直接转换由keras训练好的模型， 不需要再使用野生的方法进行转换


#### tensorflow serving部署多模型教程

一、 部署说明

 1. tensorFlow serving部署多模型方式有两种：docker和ubuntu deb包安装, 且redhat机器暂时不支持第二种部署方式
 
 2. 关于docker, 可以阅读以下两篇博客, 如果对docker很熟悉, 可以跳过这部分
 
    1). dockerfile与docker-compose
        
      [https://blog.csdn.net/ddffr/article/details/77049118]
    
    2). docker容器和镜像区别
        
      [https://www.cnblogs.com/bethal/p/5942369.html]
    
 
二、 docker+tensorflow serving部署多模型
 
 1. 将该项目下的models内容拷贝到本机固定文件夹中, 如/home/han/self/tensorflow-serving-models/, 配置models.config
    
 2. 启动容器docker container
    
    1). 启动命令
    
        sudo docker run -p 8500:8500 -p 8501:8501 --mount type=bind,source=/home/han/self/tensorflow-serving-models/,target=/models -t tensorflow/serving --model_config_file=/models/models.config
        
    2). 命令解释
        
        8500： gprc服务端口
        8501： restful服务端口
        挂载信息： 将本机source挂载到容器target上
        模型配置： 挂载完成后, 配置直接指向容器内/models/models.config
 
 3. 验证模型加载情况
 
    1). 验证mnist或mnist-copy加载情况
        
        curl http://localhost:8501/v1/models/mnist
        curl http://localhost:8501/v1/models/mnist-copy
        
 4. 模型服务日志记录
 
 5. 模型服务版本管理        
    

三、 ubuntu deb包方式安装tensorflow serving

四、 如何使用tensorflow serving部署的模型

 1. 通过restful调用, 见client/rest
 
 2. 通过grpc调用, 间client/grpc


五、 本项目中的docker常用命令和解释
    
 1. 获取container元数据
 
    1). 命令
        
        docker inspect containerID
        
    2). 元数据解释, 以tensorflow serving container为例
    
        直接run imageID后的container元信息, 见info/730f165d6795-original.txt
        
        执行如下命令后， 查看container元信息， 见info/8b882918cc3a-run.txt：
        sudo docker run -p 8500:8500 -p 8501:8501 --mount type=bind,source=/home/han/self/tensorflow-serving-models/,target=/models -t tensorflow/serving --model_config_file=/models/models.config
        
        其中包含的端口信息和挂载信息如下：
        "PortBindings": {
                "8500/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "8500"
                    }
                ],
                "8501/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "8501"
                    }
                ]
            },
        "Mounts": [
                {
                    "Type": "bind",
                    "Source": "/home/han/self/tensorflow-serving-models/",
                    "Target": "/models"
                }
            ],
    
 2. todo: 待完善
        
        
        
        
    
        