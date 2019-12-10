from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
# Create your views here.
from django.urls import reverse
import json


def index(request):
    """
    视图
    :param request:
    :return:
    """
    # print("index")
    # i = 1 / 0
    url = reverse("user:ind")
    print(url)
    return HttpResponse("你好中国")


def sq(request):
    """
    获取查询字符串参数
    :param request:
    :return:
    """
    querydict = request.GET
    a = querydict.get('a')
    b = querydict.get('b')
    lista = querydict.getlist('a')
    print(a)
    print(b)
    print(lista)
    return HttpResponse('200 OK')


def weather(request, city, year):
    """
    接收路径(路由)参数
    :param request:
    :param city:
    :param year:
    :return:
    """
    print(city)
    print(year)
    return HttpResponse("路由参数测试")


def get_body(request):
    """
    请求体传参
    :param request:
    :return:
    """
    querydict = request.POST
    a = querydict.get('a')
    b = querydict.get('b')
    listc = querydict.getlist('a')
    print(a)
    print(b)
    print(listc)
    return HttpResponse('请求体传参')


def get_body_json(request):
    """
    非表单请求体传参
    :param request:
    :return:
    """
    json_bytes = request.body
    json_str = json_bytes.decode()
    req_data = json.loads(json_str)
    print(req_data['a'])
    print(req_data['b'])
    return HttpResponse('非表单传参')


def get_headers(request):
    """
    获取请求头信息
    :param request:
    :return:
    """
    dict = request.META
    value = dict.get("CONTENT_LENGTH")
    print(value)
    return HttpResponse(value)


def others(request):
    """
    获取其他信息
    :param request:
    :return:
    """
    print(request.method)
    print(request.user)
    print(request.path)
    print(request.encoding)
    return HttpResponse("获取其他信息")


def response(request):
    """
    返回相应对象
    :param request:
    :return:
    """
    json_str = '{"name": "张三", "age": 18}'  # 整体是个字符串
    response =  HttpResponse(json_str,
                        content_type="application/json",
                        status=200)
    response["dev"] = "aGrass0825"  # 向响应头中添加内容
    return response


def subresponse(request):
    """
    返回HttpResponse子类
    :param request:
    :return:
    """
    return HttpResponseNotFound()


def jsonresponse(request):
    """
    返回jsonresponse对象
    :param request:
    :return:
    """
    dict = {"name": "lisi", "age": 20}  # 用JsonResponse类不用手动转换成字符串，会自动帮我们转换
    return JsonResponse(dict)


def demo_views(request):
    """
    重定向
    :param request:
    :return:
    """
    # url = reverse("user:ind")  # reverse反解析和redirect重定向配合使用
    # return redirect(url)
    return redirect("/user/jsonresponse/")


def cook(request):
    """
    设置和读取cookie值
    :param request:
    :return:
    """
    response = HttpResponse("cook值创建")
    response.set_cookie("name", "zhangsan", max_age=3600)

    # 读取cookie值
    value = request.COOKIES.get("name")
    print(value)
    return response

def sessiondemo(request):
    """
    session的操作
    :param request:
    :return:
    """
    # request.session['name'] = '张三'

    # request.session.clear()
    request.session.flush()
    # del request.session['name']

    # request.session.set_expiry(0)

    values = request.session.get('name')
    print(values)

    return HttpResponse('session操作')