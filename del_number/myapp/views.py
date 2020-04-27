from django.shortcuts import render
# from .models import PpdName
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators import csrf
import pymysql
# from .xhqb.db_server import db_server
from myapp.xhqb2.cif_customer_base import base_check_phone
from myapp.xhqb2.del_mober2 import base_check_update
from myapp.xhqb2.msg_send import send_msg

# Create your views here.
#
# # 添加index函数，用于返回index.html页面
# def index(request):
#     addlist=PpdName.objects
#     print(addlist)
#     for i in addlist:
#         print(i.customer_name)
#         print(i.identity_no)
#     return render(request, 'index.html')
#
# # Get请求
# def search_from(request):
#     return render_to_response("search_from.html")
# # 重定向的页面
# def search(request):
#     request.encoding = 'utf-8'
#     if 'q' in request.GET and request.GET['q']:
#         message = '你搜索的内容为: ' + request.GET['q']
#     else:
#         message = '你提交了空表单'
#     return HttpResponse(message)
#
#
# # Post请求
# def search_post(request):
#     ctx={}
#     if request.POST:
#         print(request.POST)
#         ctx["rlt"]=request.POST["q"]
#     return render(request,"post.html",ctx)
#
# def mobler_data(request):
#     buss=base_check_phone("18973599071")
#     print(buss)
#     return render(request,"mobler_data.html",buss)


"""--小花后台-----------------"""
def xhqb_index(request):
    return render(request,"xhqb_index.html")

def mobler_find(request):
    ctx={}
    if request.POST:
        print(request.POST)
        ctx=base_check_phone(request.POST["find"])
        print(ctx)
    return render(request,"post_data.html",ctx)

def update_mobler(request):
    if request.POST:
        print(request.POST)
        masg=base_check_update(request.POST["article_id"])
        print(masg)
        return HttpResponse(masg)

def msg_find(request):
    mas={}
    if request.POST:
        print(request.POST)
        mas=send_msg(request.POST["number"])
    return  render(request,"msg.html",mas)


if __name__=="__main__":
    update_mobler("as",1210000005)