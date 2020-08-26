from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    return render(request,'index.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        password2 = request.POST['psw-repeat']
        if password==password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                print('user created') 
                return redirect('login')
        else:
            print('password not matching')    
        return redirect('register')
    else:
        return render(request,'register.html')
def create(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        password2 = request.POST['psw-repeat']
        if password==password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                print('user created') 
                return redirect('create')
        else:
            print('password not matching')    
        return redirect('create')
    else:
        auth_user = User.objects.all()
        return render(request,'panel.html',{'auth_user':auth_user})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        print(username)
        print(password)
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('logged in')
            return redirect('/')
        else:
            print('login successfully')
            return render(request,'home.html')
    else:
        return render(request,'login.html')                 



# def panel(request):
#     return render(request,'panel.html')        