# ## for serialization through url displaying details or the list of student
# # import requests

# # #url of the api
# # url = 'http://127.0.0.1:8000/appie/studentlist'

# # response = requests.get(url)
# # data = response.json()
# # print(data)


# ### for creating new student
# import requests
# import json

# # URL = 'http://127.0.0.1:8000/appie/studentcreate/'
# # def create_data():
# #     data = {
# #         'name':"Jung Kumar Mahishmati",
# #         'roll':124,
# #         'city':'Raja Pyuthan',
# #     }
# #     json_data = json.dumps(data)
# #     response = requests.post(url = URL, data = json_data)
# #     data = response.json()
# #     print(data)
# # # create_data()
 


# ####for updating the student

# url = 'http://127.0.0.1:8000/appie/student_api/'

# def get_data(id = None):
#     data = {}
#     if id is not None:
#         data = {
#             'id':id,
#         }
#     json_data = json.dumps(data)

#     headers = {'Content-type':'application/json'}
#     response = requests.get(url=url,headers=headers, data=json_data)
#     # response = requests.get(url=url,headers=headers,params=data)

#     data = response.json()
#     print(data)
# get_data()
# ## pass with id or none

# def post_data():
#     data = {
#         'name' : 'Mikash',
#         'roll' : 226,
#         'city' : "Lalitkot",
#     }
#     print(data)
#     json_data = json.dumps(data)
#     print(json_data)
#     headers = {'Content-type':'application/json'}
#     response = requests.post(url = url,headers=headers,data=json_data)
#     print(response)
#     data = response.json()
#     print(data)

# post_data()




# def update_data():
#     data = {
#         'id' : 34,
#         'name' : 'raajfal4w3t45ykjfabin Kumal',
#         'roll' : 24,

#         'city' : 'Kathmandy ',
#     }
#     json_data = json.dumps(data)
#     headers = {'Content-type':'application/json'}
#     response = requests.put(url = url,data = json_data,headers=headers)
#     data = response.json()
#     print(data)
# update_data()

# def partial_update_data():
#     data = {
#         'id' : 34,
#         'name' : 'raajfal4w3t45ykjfabin Kumal',
#         'roll' : 24,
#     }
#     json_data = json.dumps(data)
#     headers = {'Content-type':'application/json'}
#     response = requests.patch(url = url,data = json_data,headers=headers)
#     data = response.json()
#     print(data)
# partial_update_data()

# def delete_data():
#     data = {
#         'id' :34,
 
#     }
#     json_data = json.dumps(data)
#     headers = {'Content-type':'application/json'}
#     response = requests.delete(url = url,data = json_data,headers=headers)
#     data = response.json()
#     print(data)
# delete_data()

