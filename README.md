ssapi使用文档
==========

*******

|Author|Jeff Yang|
|---|---
|email|yjf1970231893@gmail.com|
|comment|north drift! Come on!|

********

## 下载源码
git clone https://github.com/vangietech/ssapi.git 或者 <br>
git clone git://github.com/vangietech/ssapi.git

## 启动程序：
```
cd ssapi
chmod +x setup.sh
source setup.sh 或 ./setup.sh
```
## API解释
```
1. 获取/创建用户
  GET  http://\<host ip:8100\>/polls/134Ef234sfaDsdY/user/
2. 列出本代理服务器上的所有用户
  GET  http://\<host ip:8100\>/polls/134Ef234sfaDsdY/user/all <br>
3. 删除指定用户
  DELETE  http://\<host ip:8100\>/polls/134Ef234sfaDsdY/user/\<port\>
4. 禁用用户
  GET http://\<host ip:8100\>/polls/134Ef234sfaDsdY/user/disable/\<port\>
5. 使能用户
  GET http://\<host ip:8100\>/polls/134Ef234sfaDsdY/user/enable/\<port\>
```
