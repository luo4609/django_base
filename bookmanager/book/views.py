from django.shortcuts import render

# Create your views here.

#request
from django .http import HttpRequest
from django.http import HttpResponse
#我们期望用户输入http://127.0.0.1:8000/index/
# #来访问视图函数
def index ( request) :
    return HttpResponse('ok')
