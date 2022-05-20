from dataclasses import dataclass
from unittest import result
from warnings import catch_warnings
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from .models import User
import jwt
import time
def loginUser(request):
    data = request.params['data']
    UserAccount = data['username']
    UserPassword = data['password']
    try: 
        res =  model_to_dict(User.objects.get(UserAccount=UserAccount))
    except BaseException:
        print(132321132)
        return JsonResponse({'result':False})
    else:
        if (res['UserPassword'] == UserPassword):
            token = jwt.encode({'username':UserAccount,'date':time.time()}, 'secret', algorithm='HS256')
            return JsonResponse({'result':True,'token':token})
        else:
            return JsonResponse({'result':False})

def registerUser(request):
    data = request.params['data']
    UserAccount = data['username']
    try: 
        res =  model_to_dict(User.objects.get(UserAccount=UserAccount))
    except BaseException:
        user = User()
        user.UserAccount = data['username']
        user.UserPassword = data['password']
        user.save()
        return JsonResponse({'result':True})
    else :
        return JsonResponse({'result':False})


def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)
    action = request.params['action']

    print((request.params))

    if action=='login':
        return loginUser(request)
    elif action=='register':
        return registerUser(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})

