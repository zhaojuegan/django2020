import datetime

from django.shortcuts import render,reverse,redirect
from django.http.response import HttpResponse
# Create your views here.
def hello():
    return 'django'
class Fruites:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def say(self):
        return 'HAHAHAHA'
dc = {
    "name":"xiaohong",
    "age":18
}
def view_fun(request):
    url = reverse('v1')
    return redirect(url)
    # print(request.POST['username'])
    # print(request.POST['password'])
    return HttpResponse(content="hello world!~")
def view_fun2(request):
    return HttpResponse(content="hell0 mysql!~")
def view_re_fun(request):
    return HttpResponse(content="hello re_world!~")
def templates(request):
    return render(request,'form.html',context={
        'zh_uce':'请注册',
        'd_l': '立即登录',
        'phone': '请输入手机号',
        'yzm': '请输入短信验证码',
        'send':'发送验证码',
        'username':'请输入用户名',
        'password':'请输入密码',
        're_password':'请再次输入密码',
        'tx_yzm': '请输入图形验证码',
        'sub_mit':'立即注册'
    })
def view_templ(request):
    return render(request,'form2.html',context={
        'name':"",
        'test':"",
        'phone':"请输入手机号",
        'password':"",
        'xs':"",
        'wj':"",
        'dl':"登录",
    })
def view_temp2(request):
    return render(request,'img.html')
def view_temp3(request):
    print("您输入的手机号为:%s" % request.POST['phone'])
    print("您输入的验证码为:%s" % request.POST['yzm'])
    print("您输入的用户名为:%s" % request.POST['username'])
    print("您输入的密码为:%s" % request.POST['password'])
    print("您再次输入的密码为:%s" % request.POST['repassword'])
    print("您输入的图形验证码为:%s" % request.POST['txyzm'])

    return HttpResponse(content="hello KT!~")


def form_reg(request):
    print(request.POST)
    return HttpResponse(content="form view")