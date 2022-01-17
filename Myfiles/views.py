from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import translation

from Myfiles.models import *
from .forms import RegisterUser
from django.contrib.auth import  login,authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def index(request):
    uzunlik = Product.objects.all()
    u = len(uzunlik)-4
    yangi_maxsulotlar = Product.objects.all()[u:]
    telefonlar = Product.objects.filter(tur=1)[0:4]
    akses = Product.objects.filter(tur=2)[0:4]
    oshxona = Product.objects.filter(tur=3)[0:4]
    kitob = Product.objects.filter(tur=4)[0:3]
    toy = Product.objects.filter(tur=6)[0:3]
    kons = Product.objects.filter(tur=7)[0:3]
    rozgor = Product.objects.filter(tur=8)[0:3]
    komp = Product.objects.filter(tur=9)[0:3]
    kiyimlar = Product.objects.filter(tur=10)[0:3]
    suviner = Product.objects.filter(tur=11)[0:3]

    contents={'phones':telefonlar,'akses':akses,'oshxona':oshxona,'kitob':kitob,
              'toy':toy,'kons':kons,'rozgor':rozgor,'komp':komp,'kiyimlar':kiyimlar,
              'suviner':suviner,'newww':yangi_maxsulotlar}
    if 'ddd' in request.POST:

        if   request.user.is_authenticated:
            nomi = request.POST.get('w3ls_item')
            narxi = request.POST.get('amount')
            miqdor = request.POST.get('add')
            miqdor = int(miqdor)
            narxi = int(narxi)

            user_id = request.user.id
            username = User.objects.get(id=user_id)
            username = str(username)
            nomlar = []
            nom = Sotib_olingan_maxsulotlar.objects.filter(mijoz_id = user_id)

            for i in nom:
                nomlar.append(i.nomi)

            if nomi in nomlar:
                id = request.POST.get('idd')
                max_nomi = Sotib_olingan_maxsulotlar.objects.get(id =id)
                max_miqdori = max_nomi.miqdori
                max_miqdori += 1

                narxi = narxi*max_miqdori
                Sotib_olingan_maxsulotlar(id, nomi, narxi, max_miqdori, username, user_id).save()
            else:
                ids = [0]
                mobiles = Sotib_olingan_maxsulotlar.objects.all()
                for mobile in mobiles:
                    ids.append(mobile.id)

                Sotib_olingan_maxsulotlar(max(ids)+1,nomi,narxi,miqdor,username,user_id).save()
        else:
            return render(request,'sign in.html')



    contents['new_products'] = yangi_maxsulotlar


    return render(request,'index.html',contents)
def maxsulotlar(request):

    telefonlar = Product.objects.filter(tur=1)
    akses = Product.objects.filter(tur=2)
    oshxona = Product.objects.filter(tur=3)
    kitob = Product.objects.filter(tur=4)
    toy = Product.objects.filter(tur=6)
    kons = Product.objects.filter(tur=7)
    rozgor = Product.objects.filter(tur=8)
    komp = Product.objects.filter(tur=9)
    kiyimlar = Product.objects.filter(tur=10)
    suviner = Product.objects.filter(tur=11)
    contents={'phones':telefonlar,'akses':akses,'oshxona':oshxona,'kitob':kitob,
              'toy':toy,'kons':kons,'rozgor':rozgor,'komp':komp,'kiyimlar':kiyimlar,
              'suviner':suviner}
    if 'cmd'  in request.POST :

        if request.user.is_authenticated :
            nomi = request.POST.get('w3ls_item')
            narxi = request.POST.get('amount')
            miqdor = request.POST.get('add')

            user_id = request.user.id
            usernames = User.objects.get(id=user_id)
            usernames = str(usernames)


            ids = [0]
            mobiles = Sotib_olingan_maxsulotlar.objects.all()
            for mobile in mobiles:
                ids.append(mobile.id)

            Sotib_olingan_maxsulotlar(max(ids)+1,nomi,narxi,miqdor,usernames,user_id).save()
        else:
            return render(request,'sign in.html')


    return render(request,'products.html',contents)
def boglanish(request):
    if 'Name' in request.POST:
        ism = request.POST.get('Name')
        mail = request.POST.get('Email')
        tel = request.POST.get('Telephone')
        matn = request.POST.get('message')
        idlar = [0]
        textt = Murojatlar.objects.all()

        for i in textt:
            idlar.append(i.id)

        Murojatlar(max(idlar)+1,ism,mail,tel,matn).save()
    return render(request,'mail.html')
def about(request):
    return render(request,'about.html')
def korzinka(request):
    user_id = request.user.id
    basket = Sotib_olingan_maxsulotlar.objects.filter(mijoz_id = user_id)
    return render(request,'korzinka.html',{'basket':basket})
def signin(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,message="Ro'yxatdan o'tdiz")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, message='')
    else:
        form = UserCreationForm()

    return render(request,'sign in.html',{'form':form})





    # else:
    #     form = UserCreationForm()
    #
    #
    #
    # return render(request, 'sign in.html',{'form':form})
    #
    #
    #



def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Error !! Username or Password is incorrect")
            return HttpResponseRedirect('/login')
    else:
        form = AuthenticationForm()
    return render(request,'log in.html',{"form":form})
def logoutt(request):
    logout(request)
    return HttpResponseRedirect('/')
def single(request,id):

    if 'Name' in request.POST:
        ism = request.POST.get('Name')
        mail = request.POST.get('Email')
        tel = request.POST.get('Telephone')
        matn = request.POST.get('Review')
        tur = request.POST.get('tur')
        idlar = [0]
        textt = Comment.objects.all()

        for i in textt:
            idlar.append(i.id)

        Comment(max(idlar) + 1, ism, mail, tel, matn,tur).save()
    maxsulot = Product.objects.get(id=id)
    rasm2  =maxsulot.rasm2.url
    print('**********************************************************')
    print(rasm2)
    max_tur = maxsulot.tur
    commentlar = Comment.objects.filter(tur=max_tur)[:2]
    return render(request,'single.html',{"maxsulot":maxsulot,'comments':commentlar})

def delete_max(request,id):
    idlar = [0]
    user_id = request.user.id
    maxx = Sotib_olingan_maxsulotlar.objects.filter(mijoz_id=user_id)
    for i in maxx:
        idlar.append(i.id)

    if id in idlar:
        maxsulot = Sotib_olingan_maxsulotlar.objects.get(id=id)
        if maxsulot.miqdori>1:
            max_nomi = Sotib_olingan_maxsulotlar.objects.get(id=id)
            max_miqdori = max_nomi.miqdori
            max_miqdori -= 1
            nomi = maxsulot.nomi
            user_id = request.user.id
            username = User.objects.get(id=user_id)
            username = str(username)
            narxi = maxsulot.narxi/maxsulot.miqdori * max_miqdori

            Sotib_olingan_maxsulotlar(id, nomi, narxi, max_miqdori, username, user_id).save()
            maxsulot = Sotib_olingan_maxsulotlar.objects.get(id=id).delete()

    user_id = request.user.id

    maxx = Sotib_olingan_maxsulotlar.objects.filter(mijoz_id = user_id)
    return render(request,'korzinka.html',{'basket':maxx})



