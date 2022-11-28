# 一、项目介绍

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7bf9cee8308940448d621604a45cce90)](https://app.codacy.com/gh/462548187/fastApiFramework?utm_source=github.com&utm_medium=referral&utm_content=462548187/fastApiFramework&utm_campaign=Badge_Grade_Settings)

- 名称：FastAPIFramework
- 版本：0.0.1
- 作者：Yingqing Shan
- 邮箱：yshan20@su.edu
- 描述：FastAPIFramework

### 说明：
    最近公司上班发觉Python 在Web上没有特别健全的框架，大部分框架只解决部分功能，没有将异常、日志、中间件等等包装到框架中。
    为解决以上问题，开发一套类似Java的Spring的解决方案的框架，参照多位作者，整合并开发出这个FastApiFramework的框架，希望能解决像我困扰的同学。
    如果你什么好的建议，欢迎一起学习交流！

# 二、 项目结构





# 三、项目运行
## 1. 安装依赖
```shell
pip install -r requirements.txt
```
## 2. 运行项目
```shell
python main.py
```


# 四、软件架构
### 1、主要功能点有:

    项目配置文件处理

    API日志记录处理

    异步redis缓存处理

    同步数据库整合使用

    异步数据库的整合和使用

    全局错误异常处理

    全局的Http请求响应报文的处理

    扩展第三方插件-限流器

    扩展第三方的插件-错误统计处理

    扩展-第三方插件-全局的认证JWT

    扩展-第三方插件-消息队列的整合


# 五、项目参考
1、 [fastapi_skeletons](https://gitee.com/xiaozhong1988/fastapi_skeletons)

2、[pity](https://github.com/wuranxu/pity)


# 六、版权
### 1、要求
    使用该项目请遵守 Apache-2.0 许可证，不得在未同意下使用商业行为；