1.DIV标签，称为区隔标记。作用是设定字、画、表格等的摆放位置。

2.<nav>元素，表示页面的导航链接部分。
  
3.<a>标签的全称叫anchor(锚)，现在网页中一般用来定义一个超链接
  
4.<li> 标签定义列表项目。

<li> 标签可用在有序列表（<ol>）、无序列表（<ul>）和菜单列表（<menu>）中。

5.<title>Learning Log</title> 包含了一个<title>元素，在浏览器中打开学习笔记的页面时，浏览器的标题栏将显示该元素的内容。
  
6.<form action="{% url 'learning_logs:new_topic' %}" method='POST'>
  定义 HTML表单。
  实参action告诉服务器将提交的表单数据发送到哪里，这里我们将它发送给视图函数new_topic()
  实参method让浏览器以POST请求方式提交数据。
