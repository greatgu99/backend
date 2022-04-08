from django.shortcuts import render
from django.http import JsonResponse
import sys 
sys.path.append("..") 
from baseline_a2c import train_and_test
# from baseline_a2c import testconnect


def diagnose(request):
    data = request.params['data']
    num = request.params['num']
    data['disease_tag']='Esophagitis'
    train_and_test.reload(data)
    print(data)
    one_dic = {"symptom": [], "disease":""}
    with open('save.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if "symptom" in line:
                one_dic['symptom'].append(line.split('@@@')[1].strip())
            if "disease" in line:
                one_dic['disease'] = line.split('@@@')[1].strip()

    print(one_dic['symptom'])
    print(one_dic['disease'])
    if (num == len(one_dic['symptom'])):
        return JsonResponse({'ret':0,'result':True,'disease':one_dic['disease']})
    else:
        return JsonResponse({'ret':0,'result':False,'symptom':one_dic['symptom'][num]})


def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)
    action = request.params['action']

    print((request.params))

    if action=='diagnose':
        return diagnose(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})