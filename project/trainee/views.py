from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .models import Trainee
from cource.models import Course


def the_list(request):
    the_trainees = Trainee.objects.all()
    the_course = Course.objects.all()
    context={
        'the_trainees':the_trainees,
        'the_course':the_course
             }
    print(the_course)
    return render(request, 'trainee/list.html', context)


def insert(request):
    if request.session.get('username') is not None:
        if request.method == 'GET':
            return render(request,'trainee/insert.html',{})
        else:
            the_user = Trainee()
            the_user.name = request.POST['username']
            the_user.national_num = request.POST['national']
            the_user.sex = request.POST['sex']
            the_user.save()
            return HttpResponseRedirect('/trainee')
    return render(request,'trainee/insert.html',{})


def trainee_update(request, id):
    if request.session.get('username') is not None:
        context = {}
        if request.method == 'GET':
            context['user'] = Trainee.objects.get(id=id)
            return render(request, 'trainee/update.html', context)
        else:
            Trainee.objects.filter(id=id).update(name=request.POST['username'], national_num=request.POST['national'], sex=request.POST['sex'])
            return HttpResponseRedirect('/trainee')
    else:
        return HttpResponseRedirect('/trainee')

def trainee_delete(request,id):
    if request.session.get('username') is not None:
        x = Trainee.objects.filter(id=id).delete()
        return HttpResponseRedirect('/trainee/')
    else:
        return HttpResponseRedirect('trainee')

