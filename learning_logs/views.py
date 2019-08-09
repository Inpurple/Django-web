from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.shortcuts import render,get_object_or_404
from django.http.response import Http404

#from pip._vendor.requests.api import post
#from code import args
# Create your views here.

def index(request):
    """home"""
    return render(request,'learning_logs/index.html')

@login_required
def topics(request):
    """显示所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    """显示单个主题及所有的条目"""
    topic=get_object_or_404(Topic,id=topic_id)
    #确认请求的主题属于当前用户
    if topic.owner!=request.user:
        raise Http404
    
    entries=topic.entry_set.order_by('date_added')
    context={'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    """增加新主题"""
    if request.method!='POST':
        #未提交数据，创建一个表单
        form=TopicForm()
        
    else:
        #POST提交的数据，对数据进行处理
        form=TopicForm(request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    
    context={'form':form}
    return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    """在特定的主题中增加条目"""
    topic=Topic.objects.get(id=topic_id)
    
    if request.method!='POST':
        #未提交数据，创建一个新表单
        form=EntryForm()
    else:
        #POST 提交的数据，对数据进行处理
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
        
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    
    context={'form':form,'topic':topic,}
    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    """编辑既有条目"""
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    if topic.owner!=request.user:
        raise Http404
    
    if request.method!='POST':
        #初次请求，使用当前条目填充表单
        form=EntryForm(instance=entry)
        
    else:
        #POST提交的数据，对数据进行处理
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    context={'form':form,'topic':topic,'entry':entry,}
    return render(request,'learning_logs/edit_entry.html',context)
            

    
        