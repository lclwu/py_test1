from django.shortcuts import render
from blog.models import Test
from django.http import HttpResponse
# Create your views here.

# def index(requset):
#     user=Test.objects.all()
#     # user1=Test.objects.filter(id_name=1)
#     for user_name in user:
#         print(user_name.aticel)
#     # for i in user1:
#     #     print(i.aticel)
#     return HttpResponse("你好")

def index1(requset):
    user=Test.objects.all()
    # user1=Test.objects.filter(id_name=1)
    for user_name in user:
        print(user_name.aticel)
    # for i in user1:
    #     print(i.aticel)
    return render(requset,"blog/index.html",{"users":user})