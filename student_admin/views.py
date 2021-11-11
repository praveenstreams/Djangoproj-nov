from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import re
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from django.conf import settings
from student_admin.models import student_model,admin_model
def homepage(request):
    return render(request,'home.html')

def student_reg_home(request):
    return render(request,'register_form.html')

def admin_reg_home(request):
    return render(request,'admin_register.html')

def std_register(request):
    name=request.POST.get('name')
    dob = request.POST.get('dob')
    phone= request.POST.get('phone')
    pass1=request.POST.get('pass1')
    pass2 = request.POST.get('pass2')

    if len(name) == 0 or len(dob) == 0 or len(phone) == 0 or len(pass1) == 0 or len(pass2) == 0:
        return render(request, "register_form.html", {'patt': "empty fields"})
    elif pass1 == pass2:
        r_p = re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
        res = re.search(r_p, pass1)
        if res:

            obj = student_model(name=name, dob=dob, phone=phone, password=pass1)
            obj.save()

            data = request.FILES["file"]

            path = default_storage.save('tmp/' + phone + ".jpg", ContentFile(data.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            return render(request, 'home.html', {'txt': "Login Here"})
        else:
            return render(request, 'register_form.html',
                          {'patt': "Password must contain 8 char, upper case, lowercase and number"})
    else:
        return render(request, 'register_form.html', {"patt": "password not match"})

def admin_register(request):
    name = request.POST.get('name')
    dob = request.POST.get('dob')
    phone = request.POST.get('phone')
    pass1 = request.POST.get('pass1')
    pass2 = request.POST.get('pass2')
    if len(name) == 0 or len(dob) == 0 or len(phone) == 0 or len(pass1) == 0 or len(pass2) == 0:
        return render(request,"admin_register.html",{'patt':"empty fields"})
    elif pass1==pass2:
        r_p = re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
        res = re.search(r_p, pass1)
        if res:


            obj = admin_model(name=name, dob=dob, phone=phone, password=pass1)
            obj.save()

            data = request.FILES["file"]

            path = default_storage.save('tmp/' + phone + ".jpg", ContentFile(data.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            return render(request, 'home.html',{'txt':"Login Here"})
        else:
            return render(request,'admin_register.html',{'patt':"Password must contain 8 char, upper case, lowercase and number"})
    else:
        return render(request,'admin_register.html', {"patt": "password not match"})
def login(request):
    phone=request.POST.get('phone')
    password=request.POST.get('password')
    li=[]
    flag=0

    obj=student_model.objects.filter(phone=phone,password=password).values()
    obj1=admin_model.objects.filter(phone=phone,password=password).values()
    if len(obj)!=0:
        flag=1
    elif len(obj1)!=0:
        flag=2
    if flag==0:
        return HttpResponse("Invalid")

    # if len(obj) !=0:
    #     request.session['session_name'] = obj[0]['name']
    # else:
    #         request.session['session_name'] = obj1[0]['name']
    #     else:
    #         HttpResponse("Invalid")

    if flag==1:
        request.session['session_name'] = obj[0]['name']
        data = student_model.objects.filter(name=request.session['session_name'])
        print(data, "//////////////////")
        return render(request, 'student_dashboard.html', {'students': data})




    elif flag==2:
        request.session['session_name'] = obj1[0]['name']
        #request.session['session_phone'] = obj[0]['phone']

        data=student_model.objects.all()
        print(data,"//////////////////")
        return render(request,'admin_dashboard.html',{'students':data})



def delete_student(request):
    id=request.GET.get('uid')
    student_model.objects.filter(id=id).delete()
    return render(request,'admin_dashboard.html')
def go_profile(request):
    name = request.session['session_name']

    ob=admin_model.objects.filter(name=name).all()
    print(ob,"///////////////////////////")





    return render(request,'adminprofile.html',{"data":ob})


def delete_admin_session(request):
    request.session.delete()
    return render(request, 'home.html',{'txt':"Session terminated"})




