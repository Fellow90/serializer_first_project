## for serialization through url displaying details or the list of student
# import requests

# #url of the api
# url = 'http://127.0.0.1:8000/appie/studentlist'

# response = requests.get(url)
# data = response.json()
# print(data)


### for creating new student
import requests
import json

URL = 'http://127.0.0.1:8000/appie/studentcreate/'
def create_data():
    data = {
        'name':"Jung Kumar Mahishmati",
        'roll':124,
        'city':'Raja Pyuthan',
    }
    json_data = json.dumps(data)
    response = requests.post(url = URL, data = json_data)
    data = response.json()
    print(data)
# create_data()
 


####for updating the student

url = 'http://127.0.0.1:8000/appie/studentapi/'

def get_data(id = None):
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    json_data = json.dumps(data)
    response = requests.get(url=url,data=json_data)
    data = response.json()
    print(data)
# get_data()

def post_data():
    data = {
        'name' : 'Mahishmati',
        'roll' : 1000,
        'city' : "Callifornia",
    }
    json_data = json.dumps(data)
    response = requests.post(url = url,data = json_data)
    data = response.json()
# post_data()


def update_data():
    data = {
        'id' : 3,
        'name' : 'Harish',
        'roll' : 1000,
        'city' : 'Lalitjung',
    }
    json_data = json.dumps(data)
    response = requests.put(url = url,data = json_data)
    data = response.json()
    print(data)
update_data()

def delete_data():
    data = {
        'id' : 16,
 
    }
    json_data = json.dumps(data)
    response = requests.delete(url = url,data = json_data)
    data = response.json()
    print(data)
# delete_data()