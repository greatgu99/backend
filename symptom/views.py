from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Symptom
from django.forms.models import model_to_dict

def getAllSymptom(request):
    symptom_list=Symptom.objects.all()
    res=[]
    for i in symptom_list:
        res.append(model_to_dict(i))
    return JsonResponse({'ret':0,'symptom_list':res})

def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)
    action = request.params['action']

    print((request.params))

    if action=='get_all_symptom':
        return getAllSymptom(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})
