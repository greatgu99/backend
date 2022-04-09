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
    "action":"diagnose",
    "data":{
        'explicit_inform_slots': {'Burning sensation behind the breastbone': True}, 
        'implicit_inform_slots': {'Fever':False,'Diplopia':True}
    },
    "num":2
}
response = requests.post('http://localhost:8080/backend/diagnose',json=payload)
print(response)


pprint.pprint(response.json())

# from pathlib import Path
# import os

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
# print(MEDIA_ROOT)
