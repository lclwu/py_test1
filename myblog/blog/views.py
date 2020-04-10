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

def index1(request):
    user=Test.objects.all()
    for user_name in user:
        print(user_name.aticel)
    return render(request,"blog/index.html",{"users":user})

def aticel(request,articel_id):
    articel=Test.objects.get(pk=articel_id)
    print(articel)
    return  render(request,'blog/aticle.html',{"articel":articel})

def edit_page(request,articel_id):
    if str(articel_id)=="0":
        return render(request,'blog/edit_page.html')
    articel = Test.objects.get(pk=articel_id)
    return render(request, 'blog/edit_page.html', {"articel": articel})

def edit_action(request):
    titil=request.POST.get("title",'null')
    content=request.POST.get("content",'null')
    articel_id=request.POST.get("article_id",'0')
    if articel_id=='0':
        Test.objects.create(titel_name=titil,aticel=content)
        user=Test.objects.all()
        return render(request, "blog/index.html", {"users": user})
    articel=Test.objects.get(pk=articel_id)
    articel.titel_name=titil
    articel.aticel = content
    articel.save()
    return render(request,'blog/aticle.html',{"articel":articel})