from django.shortcuts import render
from .models import PpdName
from myapp.xhqb.data_sql import cif_base
# from .models import City

# Create your views here.

# 添加index函数，用于返回index.html页面
def index(request):
    addlist=PpdName.objects.filter(id=1)
    print(addlist)
    for i in addlist:
        print(i.customer_name)
        print(i.identity_no)
    # bblist=City.objects.filter(id=1)
    # for i in bblist:
    #     print(i.Name)
    i=cif_base('18973599071')
    print(i)


    return render(request, 'index.html')