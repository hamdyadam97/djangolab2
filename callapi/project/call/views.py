from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
app_name = 'call'


def listapi(request):
    url = "http://127.0.0.1:9000/trainee/list"
    head = {'contnet-type': 'application/json'}
    res = requests.get(url=url, headers=head)
    print(res.status_code)
    trainees = res.json()
    context = {'trainees': trainees}
    return render(request,'call/listapi.html',context)