### 1. python 装饰器
装饰器(decorator)是放在函数定义前面的指令，Python在函数运行前，根据它来修改函数代码的行为。

### 2. 查询数据库
```python
topics = Topic.objects.order_by('date_added')
```
请求提供Topic对象，并按属性date_added来对他们进行排序。我们将返回的查询集存储在topics中。

### 2. render()函数
 render()函数根据视图函数提供的数据，渲染响应。
 render()提供了两个实参：原始请求对象以及一个可以用于创建网页的模板。
 
### 3.定义将要发送给模板的上下文
```python
context = {'topics':topics}
```
上下文是一个字典，其中键是模板中用来访问数据的名称，值是我们要发送给模板的数据。

