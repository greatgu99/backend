import  requests,pprint
#
# payload = {
#     "action":"addcat",
#     "data":{
#         "CatName":"白猫",
#         "CatLocation":"打篮球",
#         "CatColor":"黄"
#     }
# }
# response = requests.post('http://localhost:8080/test/',json=payload)
# print(response)
#
#
# pprint.pprint(response.json())
#
#
payload = {
    "action":"addhistory",
    "data":{
        'explicit_inform_slot': {'abc':True,'def':False},
        'implicit_inform_slot': {'dfg':True,'sdf':False},
        'disease_tag':'oo123'
    },
    "token":"greatgu"
}

payload = {
    "action":"gethistory",
    "token":"greatgu"
}
response = requests.post('http://localhost:8080/api/backend/history',json=payload)
print(response.json()['data'][0]['explicit_symptom']['abc'])



# from pathlib import Path
# import os

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
# print(MEDIA_ROOT)
