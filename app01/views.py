from django.shortcuts import render,HttpResponse,redirect
# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')

        obj = models.UserInfo.objects.filter(username=u, password=p).first()
        if obj:
            return redirect('/cmdb/index/')
        else:
            return render(request,'login.html')
    else:
        return redirect('cmdb/index/')

def index(request):
    return render(request,'index.html')

def user_info(request):

    if request.method == 'GET':
        user_list = models.UserInfo.objects.all()
        group_list = models.UserGroup.objects.all()
        return render(request, 'user_info.html',{'user_list':user_list,'group_list':group_list})

    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        models.UserInfo.objects.create(username=u,password=p)

        return redirect('cmdb/user_info/')



def user_detail(request,nid):

    obj = models.UserInfo.objects.filter(id=nid).first()

    return render(request,'user_detail.html',{'obj': obj})

def user_del(request,nid):

   models.UserInfo.objects.filter(id=nid).delete()
   return redirect('/cmdb/user_info/')

def user_edit(request,nid):
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'user_edit.html',{'obj': obj})
    elif request.method == "POST":
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.UserInfo.objects.filter(id=nid).update(username=u,password=p)
        return redirect('/cmdb/user_info/')


def user_group(request):
    return render(request, 'user_group.html')

from app01 import models


def orm(request):
    # models.UserGroup.objects.create(caption='DBA')

    models.UserInfo.objects.create(
        username='root',
        password='123',
        email='dffdsfdsfd',
        test='dfasdfasdf',
        user_group_id=1,
    )


    return HttpResponse('orm')

def orm2(request):
    models.UserGroup.objects.create(caption='CEO')
    models.UserGroup.objects.create(caption='SA')
    return HttpResponse('orm2')



