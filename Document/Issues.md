### 1.在Eclipse+Django一系列的编码之后，编译器会报错，可忽略。

### 2.在虚拟环境下的命令窗口输入代码“from django.db import models”，无报错信息。在models.py文件中运行该代码是出现报错。
A：Eclipse未配置好Django<br>  
S：报错无模块Django，重新pip install 安装即可，再在Eclipse→Window→Preference→PyDev→PythonIntepreter→library，检查是否已成功安装

### 3.Django shell测试项目和排除故障的交互式终端会话。但是如果要用到每次修改模型需要重启Shell，操作方式为Ctrl+Z 加回车。

### 4.向网站注册两个Topic： Chess和Rock Climbing 点击save完成后，生成的不是Chess 和 Rock Climbing而是object(1)和object(2)
S:检查class Entry(models.Model):的def __str__(self):是否拼写错误

### 5.因为Django 1.8 和2.0之后的url变成了path，接下来我放出两种写法
S:
5.1 learning_log/urls.py
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include( 'learning_logs.urls',namespace='learning_logs')),
]
```

5.2 learning_logs/urls.py
```python
from django.urls import path
from . import views

app_name='learning_logs'
urlpatterns = [
    path('', views.index,name='index'),
]
```
### 6.当加入中文注释时，eclipse不支持，并且运行程序报错： 
#### 6.1设置编辑器编码。
![image](https://github.com/Inpurple/Django-web/blob/master/Document/Pictures/editor.png)
#### 6.2设置工作空间编码。
![image](https://github.com/Inpurple/Django-web/blob/master/Document/Pictures/workspaceencode.png)
#### 6.3设置配置编码。
打开eclipse安装目录->eclipse.ini，末行加上-Dfile.encoding=UTF-8
#### 6.4修改python文件编码编码。
在Python脚本文件的第一行或第二行添加一句：
#coding:gbk　或
#coding:utf-8　或
##-*- coding : gbk -*-
