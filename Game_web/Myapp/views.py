from django.shortcuts import render,redirect
from django.http import HttpResponse
from Myapp.models import Game_admindb,Game_catdb,Game_prodb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from Webapp.models import contact
# Create your views here.
def index(request):
    return HttpResponse("HI")

def indexpage(request):
    return render(request,"index.html")

def adminpage(request):
    return render(request, "addadmin.html")

def displaypage(request):
    data = Game_admindb.objects.all()

    return render(request, "displayadmin.html",{'data':data})

def editpage(request):


    return render(request)

def cat_page(request):
    return render(request, "category.html")

def cat_save(request):
    if request.method == "POST":
        cn=request.POST.get('name')
        info=request.POST.get('info')
        images=request.FILES['image']
        obj =Game_catdb(cname=cn,info=info,image=images)
        obj.save()
        return redirect(cat_page)

def category_display(request):
    data=Game_catdb.objects.all()
    return render(request, "displaycategory.html",{'data':data})


def deletedata(request,dataid):
    data=Game_admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaypage)

def pro_page(request):
    data=Game_catdb.objects.all()
    return render(request, "addproduct.html",{'data':data})




def  adminpage_save(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        image=request.FILES['image']
        p=request.POST.get('password')
        sp=request.POST.get('cpassword')
        obj=Game_admindb(uname=na,email=em,image=image, password=p,cpassword=sp)
        obj.save()
        return redirect(adminpage)

def pro_save(request):
    if request.method == "POST":
        cn = request.POST.get('procat')
        pn = request.POST.get('name')
        price = request.POST.get('price')
        qun = request.POST.get('quantity')
        info = request.POST.get('info')
        images = request.FILES['image']
        obj=Game_prodb(cname=cn,pname=pn,price=price,quantity=qun,info=info,image=images)
        obj.save()
        return redirect(pro_page)

def pro_display(request):
    data=Game_prodb.objects.all()
    return render(request,"displayproduct.html",{'data':data})

def delete_cat(request,dataid):
    data =Game_catdb.objects.filter(id=dataid)
    data.delete()
    return redirect(category_display)

def delete_pro(request,dataid):
    data=Game_prodb.objects.filter(id=dataid)
    data.delete()
    return redirect(pro_display)

def update_2data(request,dataid):
    if request.method=="POST":
        cna = request.POST.get('name')
        inf = request.POST.get('info')
        try:
           imge = request.FILES['image']
           fs = FileSystemStorage()
           file = fs.save(imge)
        except MultiValueDictKeyError:
            file = Game_catdb.objects.get(id=dataid).image
        Game_catdb.objects.filter(id=dataid).update(cname=cna,info= inf,image = file)
        return redirect(category_display)

def editcat_page1(request,dataid):
    data = Game_catdb.objects.get(id=dataid)
    print(data)
    return render(request, "editcat.html",{'data':data} )

def signpage(request):
    return render(request, "signin.html")

def adminlogin(request):
    if request.method == "POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user= authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(signpage)
        else:
            return redirect(signpage)








def edit_pro(request,dataid):
    data = Game_prodb.objects.get(id=dataid)
    da = Game_catdb.objects.all()
    print(data)
    return render(request, "editpro.html",{'data': data,'da':da})

def updateproduct(request,dataid):
    if request.method == "POST":
        cate = request.POST.get('procat')
        pn = request.POST.get('name')
        pp = request.POST.get('price')
        pq = request.POST.get('quantity')
        ol =request.POST.get('info')

        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Game_prodb.objects.get(id=dataid).image
        Game_prodb.objects.filter(id=dataid).update(cname =cate,pname =pn, price=pp,quantity=pq,info=ol, image=file)
        return redirect(pro_display)

def edit_ad(request,dataid):
    data = Game_admindb.objects.get(id=dataid)
    print(data)
    return render(request,"editad.html",{'data':data})


def update_1data(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        ps = request.POST.get('password')
        cp = request.POST.get('cpassword')
        try:
           imge = request.FILES['image']
           fs = FileSystemStorage()
           file = fs.save(imge)
        except MultiValueDictKeyError:
            file = Game_admindb.objects.get(id=dataid).image
        Game_admindb.objects.filter(id=dataid).update(uname=na,email= em,image = file,password=ps,cpassword=cp )
        return redirect(displaypage)

def acontactpage(request):
    data = contact.objects.all()
    return render(request,"contact1.html",{'data':data})

def deletecontactdata(request, dataid):
    data = contact.objects.filter(id=dataid)
    data.delete()
    return redirect(acontactpage)

def customerlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(signpage)
