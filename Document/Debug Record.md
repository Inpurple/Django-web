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
```python
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
```
应改为

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
urlpatterns = [
    # Home page.
    url(r'^$', views.index, name='index'),
]
```

应改为
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


### 12.虚拟环境处于活动状态时，才能正常打开项目的URL。
项目目录+python manage.py runserver 查看项目，其中有项目的URL

### 13.HTML 界面显示导航栏无topics。
![image](https://github.com/Inpurple/Django-web/blob/master/Document/Pictures/ISSUE.png)


打开网页，点击F12定位。
![image](https://github.com/Inpurple/Django-web/blob/master/Document/Pictures/F12.png)


修改HTML文件是否有拼写错误。

### 14.什么情况下在html文件前要写{% load bootstrap3 %}

### 15.Windows 创建 .gitignore 提示必须键入文件名
当我们需要将一个项目提交到Git时，并不是所有的文件都需要提交，比如一些自动生成的文件，这时候就可以使用.gitignore来忽略一些不需要提交的文件， 
在Windows中不能创建以”.”开头文件,直接创建 .gitignore 提示必须键入文件名。

### 16.项目部署后，使用浏览器打开部署后的URL，报错 app crash
使用命令heroku logs --tail

![image](https://github.com/Inpurple/Django-web/blob/master/Document/Pictures/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190806171651.png)

解决方法：在Heroku上建立数据库成功后再打开

### 17.项目部署的网站无法登陆在本地的任何账户
如果访问这个部署的应用程序，将能够像本地系统上一样使用它。然而看不到在本地部署的任何数据，因为没有复制到在线服务器。一种通常的做法是不将本地数据复制到在线部署中，因为本地数据通常是测试数据。

通过在Heroku上创建超级用户来改进部署。

### 18.本地访问项目报错，报错信息为显示无效主机头
在setting.py中关闭 debug 报错为求因 HTTP 状态 400 失败：Bad Request。 
说明: 执行当前 Web 请求期间，出现未处理的异常。请检查堆栈跟踪信息，以了解有关该错误以及代码中导致错误的出处的详细信息

在setting.py中开启 debug开关 报错为如图所示
![image](https://github.com/Inpurple/Django-web/blob/master/Document/Pictures/%E6%97%A0%E6%95%88%E4%B8%BB%E6%9C%BA.png)

解决方法，将本地环境的setting部分 Allow_hosts 加入主机的地址

```python
DEBUG = False
ALLOWED_HOSTS = ['localhost']
```
改为 

```python
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1','localhost']
```

### 19.git push heroku master 报错 Could not resolve host: git.heroku.com
fatal: unable to access 'https://git.heroku.com/chuanlegequan-learning-log.git/
: Could not resolve host: git.heroku.com

解决方法1：
检查自己的状态 Git remote -v

(mm_env) F:\Django\Virutal Environment\learning_log>Git remote -v <br>  
heroku  https://git.heroku.com/chuanlegequan-learning-log.git (fetch)<br>  
heroku  https://git.heroku.com/chuanlegequan-learning-log.git (push)<br>  

输入命令 git remote set-url --add heroku  https://git.heroku.com/chuanlegequan-learning-log.git 

后面是提交目标地址。就OK了

解决方法2：再试一遍

### 20.Git: bash: cd: too many arguments 
打开git-bash想新建一个仓库的时候，出现too many arguments 
这个原因是因为路径名或者变量中间有空格，这个时候需要用双引号括起来 

### 21.git push 到 github            $  git push -u origin master 报错

hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

提示:更新被拒绝，因为当前分支的提示位于远程分支的后面。在再次推送之前集成远程更改(例如“git pull…”)。
详情请参阅“git push -help”中的“关于快进的说明”。


hint: Updates were rejected because the remote contains work that you do
not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

更新被拒绝，因为远程包含您所做的工作在本地没有。这通常是由另一个存储库推送引起的
您可能希望首先集成远程更改
提示:(例如，“git pull…”)然后再推。
提示:详情请参阅“git push -help”中的“关于快进的说明”。

解决方法：
push前先将远程repository修改pull下来

$ git pull origin master

$ git push -u origin master

