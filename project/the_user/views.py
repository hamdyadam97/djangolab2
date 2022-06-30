from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from .forms import RegisterFrom
from .models import The_User
from trainee.decorators import logout_required


def register(request):
    if request.method == 'GET':
        return render(request, 'the_user/register.html', {})
    else:
        the_user = The_User()
        the_user.username = request.POST['username']
        the_user.email = request.POST['email']
        the_user.password = request.POST['psw']
        the_user.confirm_password = request.POST['psw-repeat']
        the_user.save()
        User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['psw'],
                                 is_superuser=True, is_staff=True)
        return HttpResponseRedirect('login')

@logout_required
def registerform(request):
    form = RegisterFrom()
    print(form)
    context = {'form' : form}
    if request.method == 'GET':
        return render(request, 'the_user/registerfrom.html', context)
    else:
        the_user = The_User()
        the_user.username = request.POST['username']
        the_user.email = request.POST['email']
        the_user.password = request.POST['password']
        the_user.confirm_password = request.POST['confirm_password']
        form = RegisterFrom(request.POST)
        # The_User.objects.create(username=request.POST['username'],email=request.POST['email'],
        #                         password=request.POST['password'],confirm_password=request.POST['confirm_password'])
        if form.is_valid():
            the_user.save()
        User.objects.create_user(username=request.POST['username'], email=request.POST['email'],
                                 password=request.POST['password'],
                                 is_superuser=True, is_staff=True)
        return HttpResponseRedirect('login')


def login_user(request):
    if request.session.get('username') is None:
        if request.method == 'GET':
            return render(request, 'the_user/login.html')
        else:
            myuserobject = The_User.objects.filter(username=request.POST['username'], password=request.POST['psw'])
            authuserobject = authenticate(username=request.POST['username'], password=request.POST['psw'])
            print(len(myuserobject))
            # print(authuserobject)
            if len(myuserobject) > 0 and authuserobject is not None:
                request.session['username'] = myuserobject[0].username
                login(request, authuserobject)
                return HttpResponseRedirect('trainee')
            else:
                print('errrrro')
                context = {}
                context['error'] = 'invalid cred.'
                return render(request, 'the_user/login.html', context)
    else:
        return HttpResponseRedirect('trainee')


def logout_user(request):
    print(request.user.is_authenticated)
    if request.session.get('username') is not None and request.user.is_authenticated:
        request.session.clear()
        logout(request)
        messages.success(request, 'تم تسجيل الخروج')
    return HttpResponseRedirect('login')

