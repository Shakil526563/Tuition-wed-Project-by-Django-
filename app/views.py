from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact,guardian_info
from django.contrib.auth  import authenticate,  login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):
    return render(request,'home.html')
def Notice(request):
    return render(request,'Notice.html')
def Contact_me(request):
    return render(request,'Contact_Us.html')    
    
def student_information(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        edu = request.POST.get('Education')
        area = request.POST.get('Area')
        email = request.POST.get('Email')
        message = request.POST.get('Text')
        student_information = Contact()
        student_information.Name = name
        student_information.Education=edu
        student_information.Area=area
        student_information.Email = email
        student_information.Text = message
        student_information.save()
        return HttpResponse('<h1> Thanks for Contact with us</h1>')
    return render(request,'Student_contact.html')
    

def showdata(request):
    contacts = Contact.objects.all()
    # for i in contacts:
    #     print(i.id,i.name,i.email,i.message)
    data = {'Contact':contacts}
    return render(request,'Student_information.html',data)

def guardian_information(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        clas=request.POST.get('Class')
        sub = request.POST.get('Subject')
        teacher = request.POST.get('Teacher')
        area = request.POST.get('Area')
        email = request.POST.get('Email')
        message = request.POST.get('Text')

        guardian_information=guardian_info()

        guardian_information.Name = name
        guardian_information.Class=clas

        guardian_information.Subject = sub
        guardian_information.Teacher = teacher
        guardian_information.Area = area
        guardian_information.Email = email
        guardian_information.Text = message
        guardian_information.save()
        return HttpResponse('<h1> Thanks for Contact with us</h1>')
    return render(request,'Guardian_reg.html')

def Gshowdata(request):
    contacts = guardian_info.objects.all()
    # for i in contacts:
    #     print(i.id,i.name,i.email,i.message)
    data = {'guardian_info':contacts}
    return render(request,'guardian_infor.html',data)


def Register(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/register')
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'login.html')   
    return render(request, "register.html")

def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/Notice/")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'home.html')   
    return render(request, "login.html")

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')
def upload(request):
    if request.method == 'POST' and request.FILES['/upload']:
        upload = request.FILES['/upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'upload.html', {'file_url': file_url})
    return render(request, 'upload.html')   