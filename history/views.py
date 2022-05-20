from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import History
from login.models import User
from django.forms.models import model_to_dict

def gethistory(request):
    token = request.params['token']
    try:
        user = User.objects.get(UserAccount=token)
    except BaseException:
        return JsonResponse({'ret':1})
    else:
        res = []
        historylist = History.objects.filter(user=user)
        for i in range(len(historylist)):
            res.append(model_to_dict(historylist[i]))
            res[i]['explicit_symptom'] = eval(res[i]['explicit_symptom'])
            res[i]['implicit_symptom'] = eval(res[i]['implicit_symptom'])
        return JsonResponse({'ret':0,'data':res})

def addhistory(request):
    data = request.params['data']
    explicit_symptom = data['explicit_inform_slot']
    implicit_symptom = data['implicit_inform_slot']
    disease_tag = data['disease_tag']
    token = request.params['token']
    try: 
        user = User.objects.get(UserAccount=token)
    except BaseException:
        return JsonResponse({'ret': 1})
    else:
        history = History()
        history.user = user
        history.explicit_symptom = str(explicit_symptom)
        history.implicit_symptom = str(implicit_symptom)
        history.disease_tag = disease_tag
        history.save()
        return JsonResponse({'ret': 0})

def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)
    action = request.params['action']

    print((request.params))

    if action=='gethistory':
        return gethistory(request)
    elif action == 'addhistory':
        return addhistory(request)      
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})
