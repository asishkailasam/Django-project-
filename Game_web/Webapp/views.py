from django.shortcuts import render,redirect
from django.http import HttpResponse
from Myapp.models import Game_catdb,Game_prodb
from Webapp.models import login_db,contact
# Create your views here.
def index(request):
    return HttpResponse("HI")

def webpage(request):
    data = Game_catdb.objects.all()
    return render(request, "webindex.html",{'data':data})


def categoryonlyFN(request,itemcatg):
    data=Game_catdb.objects.all()
    print("===itemcatg===",itemcatg)
    cname=itemcatg.upper()
    products= Game_prodb.objects.filter(cname=itemcatg)
    context={
        'products' : products,
        'category' :cname,
        'dat'     :data



    }
    return render(request,"catdisplay.html",context)

def prodetails(request,dataid):
    data=Game_prodb.objects.get(id=dataid)
    da =Game_catdb.objects.all()
    return render(request,"productdetails.html",{'dat':data ,'da':da})

def pro2_page(request):

    data=Game_prodb.objects.all()
    da = Game_catdb.objects.all()
    return render(request, "product.html",{'data':data,'da':da})

def datafill_page(request):
    return render(request,"datafill.html")

def savelogin(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        em = request.POST.get('email')
        ps = request.POST.get('pwd')
        cs = request.POST.get('cpwd')
        if ps == cs:
            obj = login_db( Name=un, Email=em, Password=ps, Cpassword=cs)
            obj.save()
            return redirect(datafill_page)
        else:
            return render(request, 'datafill.html', {'msg': "Password Not Matched"})



def customerlogin(request):
    if request.method == 'POST':
        username_r = request.POST.get("uname")
        password_r = request.POST.get("pwd")
        if login_db.objects.filter(Name=username_r,Password=password_r).exists():
            data = login_db.objects.filter(Name=username_r,Password=password_r).values('id').first()
            request.session['uname'] = username_r
            request.session['pwd'] = password_r
            # request.session['email'] =data['email']
            request.session['userid']=data['id']

            return redirect(webpage)
        else:
            return render(request,'datafill.html',{'msg':"Invalid Username or password"})


def contactpage(request):
    data = Game_catdb.objects.all()
    return render(request,"contact.html",{'data':data})

def savedata_a(request):
    if request.method == "POST":
        con = request.POST.get('name')
        e = request.POST.get('email')
        s = request.POST.get('subject')
        ms = request.POST.get('message')
        obj = contact(Name=con,Email=e,Subject=s,Message=ms)
        obj.save()
        return redirect(contactpage)

def clogout(request):
    del request.session['uname']
    del request.session['pwd']
    return redirect(webpage)
