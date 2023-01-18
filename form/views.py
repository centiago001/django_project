from django.http import HttpResponse
from django.shortcuts import render,redirect
from form.models import Information
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def form(request):
    return render(request,'form.html')


def s_mail(lst):
    #variable sections
            #data={
                #'name':lst[0],
                #'desig':lst[1],
                #'qual':lst[2],
                #'exp':lst[3],
                #'expert':lst[4],
                #'email':lst[5],
                #'mob':lst[6]
                # }
    subject='New Entry In Database'
    form_mail='testing8854mail@gmail.com'
    to='mayuradhayge@gmail.com'
    #rendering the html file msg
    msg=get_template('display_mail.html').render({
                                                    'name':lst[0],
                                                    'desig':lst[1],
                                                    'qual':lst[2],
                                                    'exp':lst[3],
                                                    'expert':lst[4],
                                                    'email':lst[5],
                                                    'mob':lst[6],
                                                    'image':lst[7],
                                                    'pdf':lst[8]
                                                 })
    #############
    ms=EmailMultiAlternatives(subject,msg,form_mail,[to])
    ms.content_subtype='html'
    ms.attach_file(str(lst[7]))
    ms.attach_file(str(lst[8]))
    ms.send()


def f_submits(request):
    try:
        if request.method=="POST":
                print("data is here")
                en= Information()
                en.name=request.POST.get("FIRSTNAME")
                en.designation=request.POST.get("desigination")
                en.qualification=request.POST.get("qulification")
                en.experiance=request.POST.get("experince")
                en.expetarea=request.POST.get("expertarea")
                en.mob=request.POST.get("mob")
                en.email=request.POST.get("email")
                en.image=request.FILES.get('image')
                en.pdf=request.FILES.get('profile')


                #profile=request.FILES['profile']
                #en= Information(
                    #name= m_name,
                    #designation= m_desigination,
                    #qualification= m_qulification,
                    #experiance= m_experiance,
                    #expetarea= m_expertarea,
                    #email= m_email,
                    #mob= m_mob)
                en.save()
                l=[en.name,en.designation,en.qualification,en.experiance,en.expetarea,en.email,en.mob,en.image,en.pdf]
                s_mail(l)
                return redirect('/')
    except Exception as e:
        return redirect('/')



def login_page(request):
    return render(request,'login_page.html')




def admin_login(request):

        try:
            
            if request.method =="POST" :
                username= request.POST.get('username')
                password= request.POST.get('password')
                user_obj= User.objects.filter(username= username)
                if not user_obj.exists():
                    return render(request,'login_page.html')

                user_obj=authenticate(username= username ,password= password)


                if user_obj:   #and user_obj.is_superuser:
                    login(request,user_obj)
                    return admin_panal(request,user_obj)
                else:
                    return render(request,'login_page.html')
        except Exception as e:
             pass






@login_required(login_url='pan/')
def admin_panal(request,val):
        
        dta=Information.objects.all()


        con={'d': dta,'user':val}

        return render(request,'database_with_button.html',con)

def delete_data(request):
    if request.method=="POST":
        ids=request.POST.get('ids')
    info=Information.objects.filter(id=ids)
    info.delete()
    if request.POST.get('ids'):
        return admin_panal(request)
    return redirect('/')

def admin_logout(request):
        logout(request)
        return redirect('/pan/')