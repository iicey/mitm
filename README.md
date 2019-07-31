# 快速获取微信文章的标题及链接导出到xlsx

> 起因：关注了几个优质的公众号进行学习，发现PC端的微信在翻阅历史文章的操作上验证缺乏用户体验。
>
> 目的：将作者所有的历史文章的标题及链接保存到xlsx方便查阅

## 项目地址

https://github.com/iicey/mitm

## 使用说明

### 安装第三方库(Python3)

```
pip install openpyxl
pip install mitmproxy
```

### 设置代理(127.0.0.1:8080)

![1564572090441](C:\Users\Zhaoyang.Wei\AppData\Roaming\Typora\typora-user-images\1564572090441.png)

![1564572149417](C:\Users\Zhaoyang.Wei\AppData\Roaming\Typora\typora-user-images\1564572149417.png)

### 安装证书

访问http://mitm.it/，安装Windows证书

### 启动脚本

开启cmd切换到mitm目录下，执行下面这段代码

```
mitmdump -s script.py
```

### 最后一步

点开PC微信里微信公众号的列表页，向下滑动即可

![1564572879319](C:\Users\Zhaoyang.Wei\AppData\Roaming\Typora\typora-user-images\1564572879319.png)