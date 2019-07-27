Django开发常见问题总结
====

### 1.在Eclipse+Django一系列的编码之后，编译器会报错，可忽略。

### 2.Eclipse未配置好Django
P:在虚拟环境下的命令窗口输入代码“from django.db import models”，无报错信息。在models.py文件中运行该代码是出现报错。<br>  
A：Eclipse未配置好Django<br>  
S：报错无模块Django，重新pip install 安装即可，再在Eclipse→Window→Preference→PyDev→PythonIntepreter→library，检查是否已成功安装

### 3.常见debug工具
3.1Django shell测试项目和排除故障的交互式终端会话。但是如果要用到每次修改模型需要重启Shell，操作方式为Ctrl+Z 加回车。<br>  
3.2Django启动服务器，查看系统中的项目 python manage.py runserver

### 4.生成的模型网页显示有误 object(1)和object(2)
P:向网站注册两个Topic： Chess和Rock Climbing 点击save完成后，生成的不是Chess 和 Rock Climbing而是object(1)和object(2)<br>  
S:检查class Entry(models.Model):的str文件:是否拼写错误

### 5.Django 1.8 和2.0之后的url变成了path，改写方法
S:
5.1 learning_log/urls.py

![image](https://github.com/Inpurple/Django-web/blob/master/Document/Pictures/Django1.8_learning_log_urls.png)

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include( 'learning_logs.urls',namespace='learning_logs')),
]
```

5.2 learning_logs/urls.py


![image](https://github.com/Inpurple/Django-web/blob/master/Document/Pictures/Django1.8_learning_logs_urls.png)

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

### 7.报错No module named 'django.core.urlresolvers'
django2.0 把原来的 django.core.urlresolvers 包 更改为了 django.urls包，所以我们需要把导入的包都修改一下就可以了

### 8.在浏览器中输入正确的URL地址之后，页面显示为空白
检查html文件编辑后是否保存

### 9.NoReverseMatch
|信息|描述|
|:---|:---|
|Request Method|GET|
|Request URL|http://localhost:8000/new_entry/(%3FP3%5Cd+)/ |
|Django Version:|2.2.3|
|Exception Type:|NoReverseMatch|
|Exception Value:|Reverse for 'new_entry' with no arguments not found. 1 pattern(s) tried: ['new_entry\\/\\(\\?P(?P<topic_id>[^/]+)\\\\d\\+\\)\\/$']Exception Location:	F:\Django\Virutal Environment\learning_log\ll_env\lib\site-packages\django\urls\resolvers.py in _reverse_with_prefix, line 668|
|Python Executable:|F:\Django\Virutal Environment\learning_log\ll_env\Scripts\python.exe|
|Python Version:|3.6.6|

![image](https://github.com/Inpurple/Django-web/blob/master/Document/Pictures/NoReverseMatch.png)

### 10. 无编写的视图函数，使用默认视图login的改写方法：

Django 1.11
```python
from django.conf.urls import url
from django.contrib.auth.views import login
 
from . import views
 
urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'},name='login'),
]
```

Django 2.2.3
```python

"""为应用程序users定义URL模式"""
 
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views
# 修改模板路径
 
LoginView.template_name = 'users/login.html'
urlpatterns = [
    # 登录界面
    path('login/', LoginView.as_view(),
         name='login'),
]
app_name = 'users'

```

### 11. The current path, users/login/, didn't match any of these.：
在topics函数前加入装饰器，login_required()之后，修改settings.py实现重新定向，但是打开相应网页出现报错。

![image](https://github.com/Inpurple/Django-web/blob/master/Document/Pictures/pagenotfound.png)

bug：我的设置与实际的URL不匹配，将url前加入“/”即可。
![image](https://github.com/Inpurple/Django-web/blob/master/Document/Pictures/settings.png)

![image](https://github.com/Inpurple/Django-web/blob/master/Document/Pictures/url_py.png)

![image](https://github.com/Inpurple/Django-web/blob/master/Document/Pictures/website.png)


